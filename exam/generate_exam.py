#!/usr/bin/env python3
"""Generate a multiple-choice exam from exam_questions.md.

Picks 14 of the 152 questions at random, with at least 3 questions per
chapter, and writes a complete LaTeX document (cover page + questions).
The corresponding answer key is written next to the .tex file.

Usage:
    python generate_exam.py [--seed N] [--out exam.tex]
"""

import argparse
import random
import re
from pathlib import Path

HERE = Path(__file__).parent
QUESTIONS_FILE = HERE / "exam_questions.md"
TOTAL_QUESTIONS = 14
MIN_PER_CHAPTER = 3


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def parse_questions(md_text):
    main, _, key_section = md_text.partition("## Answer key")
    answers = parse_answer_key(key_section)

    chapter_pattern = re.compile(r"^## (Chapter \d+ — [^\n]+)", re.MULTILINE)
    matches = list(chapter_pattern.finditer(main))

    chapters = {}
    for i, match in enumerate(matches):
        name = match.group(1)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(main)
        chapters[name] = parse_chapter(main[start:end], name, answers)
    return chapters


def parse_answer_key(text):
    answers = {}
    # Each table row has multiple (number | letter) pairs sharing pipes,
    # so use a lookahead on the trailing pipe to avoid consuming it.
    for m in re.finditer(r"\|\s*(\d+)\s*\|\s*([a-d])\s*(?=\|)", text):
        answers[int(m.group(1))] = m.group(2)
    return answers


def parse_chapter(text, chapter_name, answers):
    questions = []
    parts = re.split(r"\n\*\*(\d+)\.\*\* ", "\n" + text)
    for i in range(1, len(parts), 2):
        num = int(parts[i])
        content = parts[i + 1].rstrip()
        content = re.sub(r"\n---\s*$", "", content).rstrip()
        m = re.search(r"\n- \(a\) ", content)
        if m:
            q_text = content[: m.start()].rstrip()
            opts_text = content[m.start():].strip()
        else:
            q_text = content
            opts_text = ""
        options = re.findall(r"^- \(([a-d])\) (.+)$", opts_text, re.MULTILINE)
        questions.append({
            "number": num,
            "text": q_text,
            "options": options,
            "chapter": chapter_name,
            "answer": answers.get(num),
        })
    return questions


# ---------------------------------------------------------------------------
# Selection
# ---------------------------------------------------------------------------

def select_questions(chapters, total, min_per_chapter, rng):
    n = len(chapters)
    if n * min_per_chapter > total:
        raise ValueError(
            f"{n} chapters x {min_per_chapter} = {n * min_per_chapter} > {total}"
        )

    selected = {}
    leftover = []
    for name, qs in chapters.items():
        chosen = rng.sample(qs, min_per_chapter)
        chosen_nums = {q["number"] for q in chosen}
        selected[name] = list(chosen)
        leftover.extend(q for q in qs if q["number"] not in chosen_nums)

    extras = rng.sample(leftover, total - n * min_per_chapter)
    for q in extras:
        selected[q["chapter"]].append(q)

    flat = []
    for name in chapters:
        chapter_qs = selected[name]
        rng.shuffle(chapter_qs)
        flat.extend(chapter_qs)
    return flat


# ---------------------------------------------------------------------------
# Markdown -> LaTeX
# ---------------------------------------------------------------------------

LATEX_ESCAPES = [
    ("\\", r"\textbackslash{}"),
    ("&", r"\&"),
    ("%", r"\%"),
    ("$", r"\$"),
    ("#", r"\#"),
    ("_", r"\_"),
    ("{", r"\{"),
    ("}", r"\}"),
    ("^", r"\textasciicircum{}"),
    ("~", r"\textasciitilde{}"),
]


def escape_latex(text):
    for ch, repl in LATEX_ESCAPES:
        text = text.replace(ch, repl)
    return text


_VERB_DELIMS = '|!@"+/?#'


def _verb(code):
    """Wrap code with \\verb using a delimiter that does not occur in `code`."""
    for d in _VERB_DELIMS:
        if d not in code:
            return f"\\verb{d}{code}{d}"
    # No safe delimiter found: escape and use \texttt.
    return r"\texttt{" + escape_latex(code) + "}"


_P_START = "\x00P"
_P_END = "\x00E"


def md_to_latex(text):
    """Convert markdown subset (code fences, inline code, **bold**) to LaTeX."""
    stash = []

    def protect(latex):
        idx = len(stash)
        stash.append(latex)
        return f"{_P_START}{idx}{_P_END}"

    def code_block(match):
        code = match.group(1).rstrip("\n")
        return protect("\n\\begin{verbatim}\n" + code + "\n\\end{verbatim}\n")

    text = re.sub(r"```(?:python)?\n(.*?)```", code_block, text, flags=re.DOTALL)

    text = re.sub(r"`([^`]+)`", lambda m: protect(_verb(m.group(1))), text)

    # Mark bold with placeholder characters so escape pass leaves it alone.
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: f"\x01{m.group(1)}\x02", text)

    text = escape_latex(text)

    text = text.replace("\x01", r"\textbf{").replace("\x02", "}")

    text = re.sub(
        f"{_P_START}(\\d+){_P_END}",
        lambda m: stash[int(m.group(1))],
        text,
    )
    return text


# ---------------------------------------------------------------------------
# LaTeX rendering
# ---------------------------------------------------------------------------

PREAMBLE = r"""\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{geometry}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{array}

\geometry{margin=2.3cm}
\setlength{\parindent}{0pt}
\pagestyle{empty}
"""


def cover_page(n_questions):
    grading = grading_table(n_questions)
    return rf"""
\begin{{flushleft}}
Peter Pfaffelhuber\\
Samuel Ayomide Adeosun
\end{{flushleft}}
\hfill\begin{{minipage}}{{5cm}}\raggedleft
June 2nd, 2026, 12:15
\end{{minipage}}

\vspace{{1.2cm}}

\begin{{center}}
{{\Large\bfseries Test for the course Python for Data Analysis}}\\[0.4cm]
{{\large University of Freiburg --- Summer Term 2026}}
\end{{center}}

\vspace{{0.8cm}}

\textbf{{Last name:}}\hrulefill\\[0.4cm]
\textbf{{First name:}}\hrulefill\\[0.4cm]
\textbf{{Matriculation number:}}\hrulefill\\[1cm]

\begin{{center}}{{\bfseries\large Instructions}}\end{{center}}

\begin{{itemize}}
  \item This is a \textbf{{multiple-choice}} test. Each question has \textbf{{exactly one}} correct answer. Tick the corresponding box clearly.
  \item \textbf{{Duration:}} 45 minutes.
  \item \textbf{{No}} computers, books, notes, or mobile devices are allowed.
  \item To change an answer, cross out the wrong mark completely and clearly tick the new one. Ambiguous or unreadable markings will be counted as wrong.
  \item Each question is worth \textbf{{1 point}}; there are \textbf{{{n_questions} questions}} in total ({n_questions} points).
  \item Write your \textbf{{name}} and \textbf{{matriculation number}} on every additional sheet you use.
  \item \textbf{{Cheating is penalised with a grade of ``fail'' (5.0).}}
\end{{itemize}}

\vspace{{0.8cm}}

\begin{{center}}
{grading}
\end{{center}}

\vspace{{1cm}}

\begin{{center}}{{\bfseries\Large Good luck!}}\end{{center}}

\newpage
"""


def grading_table(n):
    col_spec = "|" + "c|" * n + "c|"
    head = " & ".join(str(i) for i in range(1, n + 1)) + r" & $\Sigma$"
    points = " & ".join("(1)" for _ in range(n)) + rf" & ({n})"
    return (
        "\\renewcommand{\\arraystretch}{1.4}\n"
        "\\begin{tabular}{" + col_spec + "}\n"
        "\\hline\n"
        + head + " \\\\\n"
        "\\hline\n"
        "\\rule{0pt}{1.2cm}" + " & " * n + "\\\\\n"
        "\\hline\n"
        + points + " \\\\\n"
        "\\hline\n"
        "\\end{tabular}"
    )


def render_question(idx, q):
    q_latex = md_to_latex(q["text"])
    # Wrap each question in a minipage so LaTeX does not split it across pages.
    lines = [
        "\\noindent\\begin{minipage}{\\linewidth}",
        f"\\textbf{{{idx}.}}~~{q_latex}",
        "",
        "\\begin{itemize}[label=$\\square$, leftmargin=2.5em, topsep=0.3em]",
    ]
    for letter, raw in q["options"]:
        opt_latex = md_to_latex(raw)
        lines.append(f"  \\item ({letter})~~{opt_latex}")
    lines.append("\\end{itemize}")
    lines.append("\\end{minipage}")
    lines.append("\\vspace{0.6cm}")
    return "\n".join(lines)


def render_document(selected):
    n = len(selected)
    questions = "\n\n".join(render_question(i, q) for i, q in enumerate(selected, 1))
    body = (
        PREAMBLE
        + "\n\\begin{document}\n"
        + cover_page(n)
        + "\n"
        + questions
        + "\n\\end{document}\n"
    )
    return body


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed for reproducibility")
    parser.add_argument("--out", type=str, default=str(HERE / "exam.tex"),
                        help="Output LaTeX file")
    args = parser.parse_args()

    rng = random.Random(args.seed)

    chapters = parse_questions(QUESTIONS_FILE.read_text())
    print("Parsed chapters:")
    for name, qs in chapters.items():
        print(f"  {name}: {len(qs)} questions")

    selected = select_questions(chapters, TOTAL_QUESTIONS, MIN_PER_CHAPTER, rng)

    out = Path(args.out)
    out.write_text(render_document(selected))
    print(f"\nWrote {out}")

    # Per-chapter counts for sanity.
    counts = {}
    for q in selected:
        counts[q["chapter"]] = counts.get(q["chapter"], 0) + 1
    print("Questions per chapter:")
    for name in chapters:
        print(f"  {name}: {counts.get(name, 0)}")

    # Answer key next to the .tex file.
    key_path = out.with_name(out.stem + "_answers.txt")
    lines = ["Answer key", "=" * 30]
    for i, q in enumerate(selected, 1):
        lines.append(f"{i:2d}. (Q{q['number']:3d}, {q['chapter'].split(' — ')[0]:>9s}): {q['answer']}")
    key_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {key_path}")


if __name__ == "__main__":
    main()
