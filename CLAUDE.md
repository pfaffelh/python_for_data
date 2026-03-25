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
