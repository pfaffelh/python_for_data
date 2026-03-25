# Project notes for Claude

## Writing style for .qmd chapters

Each section in a chapter file follows this structure:

1. **Header**: `## Topic name (\`keyword\`) {#sec-label}` — backtick-wrapped keywords/syntax, optional cross-reference label.
2. **Short intro text**: 1–3 sentences explaining the concept.
3. **Bullet list of functions/attributes**: Each item is `* \`function_name(args)\`: one or two line explanation.`
4. **Code examples**: Multiple small `{python}` cells, each demonstrating one thing, with comments inside the cell. Separate cells per concept.
5. **Closing remarks**: Optional final paragraph with caveats, tips, or connections to other sections.

See chapters 02–04 for reference.

## Chapter 11 redistribution (2026-03-25)

Chapter 11 (`11_numpy_from_chatgpt.qmd`, originally generated with ChatGPT) was redistributed:

- **Chapter 06 (numerics)**: numpy basics (arrays, indexing, slicing, views/copies, broadcasting, vectorization), linear algebra (`np.linalg`), aggregation/axis, random numbers (`np.random`), optimization (`scipy.optimize`).
- **Chapter 07 (handling data)**: pandas DataFrames (creating, selecting, filtering, groupby, missing values, `to_numpy()`), CSV/JSON loading (built-in modules), online resources (`requests`), SQL (`sqlite3`), dates/times.
- **Chapter 08 (analyzing data)**: visualization (`matplotlib`), descriptive statistics (`scipy.stats`), probability distributions, statistical tests, maximum likelihood estimation (analytical and numerical via `scipy.optimize`).
- **Chapter 11 archived**: Moved to `archive/` folder (in `.gitignore`). The ML-specific content (linear/logistic regression, gradient descent, neural networks, regularization) remains in the archived file.

### Prompts used

1. "Chapter 11 needs to be integrated into chapters 06, 07, 08. In particular, chapter 11 needs to shortened (without loosing content), the basic numpy stuff needs to go into 06, including all basic things for np.array, but also np.optimization. The pandas portion needs to go into 07. Please also extend by some material where you find the headers in 07 already. The material from scipy.stats needs to go in Chapter 08. I also need some maximum likelihood stuff in chapter 8. Do not touch the other files."
2. "My style was 1) header 2) short introductory text 3) items for the functions which belong in this section, with a one or two line explanation. 4) code example 5) final remarks in this section. Please adapt what you have just written in this style."
3. "Let Chapter 11 not appear any more in the final output, but move the file to a new folder 'archive', which you also put in .gitignore."
4. "Add a remark on what you just did in the section on AI usage."

### Chapter 07 extensions (2026-03-25)

Additional pandas content was added to Chapter 07:

- CSV/JSON examples converted from `csv`/`json` modules to pandas (`pd.read_csv`, `pd.read_json`).
- New sections: adding/renaming columns, merging/joining DataFrames, applying custom functions, value counts/unique values, handling duplicates.

#### Prompts used

1. "In 07...qmd, line 17-18, I wrote a prompt. Please do this." (the prompt was: "xxx change the csv to the pandas version of the commands below / xxx change the json to the pandas version of the commands below")
2. "Describe dataframes in 07..., line 13"
3. "Suggest three things which are missing in Chapter 7" → added: adding/renaming columns, merging/joining DataFrames, applying custom functions.
4. "Would you add even more?" → suggested: reshaping, string operations, value counts, duplicates, index operations.
5. "Please add something on 3. and 4." → added: value counts/unique values, handling duplicates.
6. "Does 07... fit well with the previous chapters?" → identified 6 inconsistencies.
7. "Please correct these points. But do not give exercises at this point." → fixed: added missing `import numpy as np`, removed `@sec-pandas` self-reference, added backtick keywords to section headers (`assign`/`rename`, `to_datetime`/`Timestamp`, `sqlite3`), removed duplicate `pd.read_csv`/`pd.to_datetime` from main bullet list, removed orphaned `ml_dataset.csv` synthetic dataset block.
8. "In the requests section, add a concrete example for an api, from a geographic dataset of world population." → added REST Countries API example (fetching population data, top 10 countries, population by region).
9. "Create an order misc, and a file fake_data.py. ..." → created `misc/` folder, `misc/fake_data.py` (using `faker` library with European locales), generated `misc/person.csv` and `misc/person.json` with 50 fictional persons (names, addresses, dates of birth, hobbies).
10. "In 07, provide person.csv and person.json as download, and use this data in the sections on csv and json." → replaced synthetic string examples with real file examples using the person dataset, added download links, added `misc/*` to `_quarto.yml` resources.
11. "Add exercises to 07, asking for some new columns in the person data for age. Also give a dict of generations..." → added 5 exercises: computing age, extracting birth year, generation mapping with a `generations` dict, filtering by generation, hobby analysis with `explode`.
12. "Please also use the person data in the SQL section." → replaced hand-crafted students table with person dataset loaded via `df.to_sql()`, demonstrated filtering, `pd.read_sql_query`, and SQL aggregation.
13. "Please also use the person data in 'Working with dates and times'." → replaced generic date examples with person dataset: converting `date_of_birth`, extracting year/month, computing age, formatting dates with `strftime`.

### Bold keywords and xxx prompts in chapters 02–06 (2026-03-25)

Executed all `xxx` prompts across chapters 02–06:

- **Chapter 02**: Added **bold** highlighting to key terms (`type`, `variable`, `int`, `float`, `exponent`, `mantissa`, `boolean`, `strings`, `format specifier`, `missing values`).
- **Chapter 03**: Added **bold** highlighting (`condition`, `for-loop`, `while-loop`, `function`, `default values`, `positional variables`, `keyword arguments`, `docstring`, `lambda-functions`, `raising`, `catching`, `context manager`).
- **Chapter 04**: Added **bold** highlighting (`container data types`, `list`, `indexing`, `slicing`, `mutable`, `tuple`, `immutable`, `set`, `dictionaries`, `key-value pairs`, `comprehensions`). Added explanation and two code examples for indexing and slicing.
- **Chapter 05**: Added **bold** highlighting (`packages`, `modules`, `submodules`, `dates`, `times`, `rounding error`, `patterns`, `regular expression`, `pickle`, `tests`, `operating system`).
- **Chapter 06**: Changed aggregation data so column/row means differ; replaced matplotlib scatter example with text-based `rng.choice`/`rng.permutation` example; added `result.nfev` output to `minimize_scalar`; deleted nonlinear least squares example.

#### Prompts used

1. "In 02, 03, 04, 05, 06, I have added comments starting with xxx. Execute these prompts."

### Audit of chapters for unexplained code (2026-03-25)

Audited chapters 02–08 for commands/variables used before being explained. Key findings:

- **Chapter 02**: `^` (XOR) operator unexplained; `str.isalpha()` missing description; `", ".join` fragment incomplete.
- **Chapter 03**: `continue`/`break` mentioned but no code examples; `abs()` used without introduction.
- **Chapter 04**: `len()` used before bullet list; `lambda`/`filter()` used without explanation; `del` keyword unexplained.
- **Chapter 05**: `@sec-loading` cross-reference points to non-existent label; `.endswith()` and `enumerate()` unexplained.
- **Chapter 06**: `np.abs()`, `np.sum()`, `np.max()` used before aggregation section; `result.nfev` and `result.root` attributes not documented.
- **Chapter 08**: 17 issues — matplotlib axis methods (`set_title`, `tight_layout`, `contourf`, `colorbar`) not in bullet list; `np.meshgrid`, `np.zeros_like`, `np.inf` unexplained; `rng.exponential`/`rng.gamma` not in chapter 06 list; distribution parameter conventions not documented.

#### Prompts used

1. "Go through all files line by line. See if every command or variable is explained before it is used. In such a case, either try to simplify the code such that everything is explained, or, if this does not work, mark the place by 'xxx' and say what needs to be introduced."
