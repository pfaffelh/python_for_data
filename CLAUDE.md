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

### Chapter 07 further edits (2026-03-26)

- Added `count`, `mean`, `std`, `min`, `max`, `median`, `quantile`, `sum` to the DataFrame bullet list with code example.
- Added section on iterating through DataFrames (`iterrows`, `itertuples`) with code examples.
- Changed value counts example from department/level to major/BSc+MSc.
- Added `Series` explanation to the introductory paragraph.
- Added `person.db` (SQLite) output to `misc/fake_data.py`; SQL section now connects to `misc/person.db` directly instead of loading CSV into an in-memory database. Download link added alongside `person.csv` and `person.json`.
- Replaced REST Countries API with World Bank API (`api.worldbank.org`) for population data, including filtering out regional aggregates via country metadata.
- Added cross-reference `@sec-datetime` to Chapter 05's dates section; referenced it from the `strftime` bullet point in Chapter 07.
- Added merge exercise (Exercise 6) exploring `pd.merge` with non-unique keys.
- Fixed `render_notebooks.sh`: copies `misc/` into `notebooks/` before rendering (so `person.csv`/`.json`/`.db` are available), cleans up afterwards; also fixed `$file` → `$f` typo.

#### Prompts used

1. "In 07..., line 17-18, I wrote a prompt. Please do this." (the prompt was: "xxx count sum mean")
2. "Add a code example on these functions in line 78ff."
3. "Execute the prompt in l. 281" (the prompt was: "xxx change example department->major, level: BSc and MSc")
4. "In misc/fake_data.py, create also a file which can then be read by sqlite3. Describe how to load it in lines 468ff. Also, provide a download of that file next to person.csv and person.json."
5. "I think, Series is not explained anywhere. Check this and describe what it is."
6. "Please use the api https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2025 instead of restcountries"
7. "Execute the prompt in 07..., l. 426" (the prompt was: "xxx note some more options for pd.to_datetime, e.g. on the formatting of the datetime.") → replaced with cross-reference to `@sec-datetime`.
8. "Add around l. 424, make a remark that dt.strftime is the same or similar to what we covered in 05 libraries..."
9. "In 07..., please add a paragraph with a code example how to iterate through a DataFrame."
10. "Execute the prompt in 07..., l. 515" (the prompt was: "xxx Make a concrete exercise from this here. If you have two DataFrames, both with a column key, which does not have unique values, find out, what pd.merge does.") → added Exercise 6.

### Chapter 08/09 split and file renumbering (2026-03-26)

The old `08_analyzing_data.qmd` was split into two files, and subsequent chapters were renumbered:

- **`08_visualizing_data.qmd`** (new): Python-free introductory section on choosing the right chart type, based on Zelazny's *Wie aus Zahlen Bilder werden* (pp. 21–41). Covers the 3-step framework (message → comparison type → chart form), five comparison types (structure, ranking, time series, frequency distribution, correlation), five chart forms (pie, bar, column, line, scatter), and a summary table. Then the `matplotlib` section from the old Chapter 08, extended with pie chart and horizontal bar chart examples.
- **`09_analyzing_data.qmd`** (new): All statistical content from the old Chapter 08 — descriptive statistics, probability distributions, statistical tests, and maximum likelihood estimation.
- **`10_example_project.qmd`**: renamed from `09_example_project.qmd`.
- **`11_misc.qmd`**: renamed from `10_misc.qmd`.
- **`12_exercises.qmd`**: renamed from `11_exercises.qmd`.
- **`_quarto.yml`**: updated chapter list.
- Download notebook links updated in all renamed files.

#### Prompts used

1. "Execute the prompt in 08..., l 9" (the prompt was: "xxx Split this file in two files, and rename the following files as 10..., 11..., 12... The first of the two files is 08_visualizing_data, the second is 09_analysing_data. In 08_visualizing, start with a Python-free text where you explain the different kinds of plots, circle, barplot (vertical and horizontal, line, scaterplot). Use the pdf in MyFiles/Wie_aus_Zahlen_Bilder_werde.pdf as a source, which you also link in the text (the url is https://link.springer.com/book/10.1007/978-3-658-07452-4), pages 21-69.")

### Notation, cleanup, and chapter 08 examples (2026-03-26)

- Renamed all prose occurrences of "python3"/"Python3" to "Python" across all `.qmd` files. Kept `jupyter: python3` (YAML), `{python3}` (code blocks), and backtick-wrapped command-line invocations (`` `python3 -m venv` `` etc.) unchanged.
- Fixed broken `{#sec-numpy}` cross-reference label in Chapter 06: moved from inline text to the first section heading.
- Executed all `xxx` prompts in chapters 02–06:
  - **Chapters 02–05**: Added **bold** highlighting to key terms (ch02: **type**, **Integers**, **floats**, **exponent**, **mantissa**, **boolean**, **string**; ch03: **condition**, **`for`-loops**, **`while`-loops**, **function**, **private**, **positional**, **keyword arguments**, **docstring**, **Raising**, **catching**, **context manager**; ch04: **container data types**, **Indexing**, **Slicing**, **mutable**, **immutable**, **key-value pairs**, **comprehensions**; ch05: **packages**, **modules**, **submodules**, **regular expression**, **test**).
  - **Chapter 04**: Added explanation of indexing and slicing with two new code examples (negative indexing, sublist extraction).
  - **Chapter 06**: Changed aggregation data so column and row means differ; replaced matplotlib scatter example with text-based `rng.choice`/`rng.permutation` examples; added `result.nfev` output to `minimize_scalar`; deleted nonlinear least squares example.
- Deleted old `08_analyzing_data.qmd` (superseded by the 08/09 split).
- Updated Zelazny reference in Chapter 08: title changed from *Wie aus Zahlen Bilder werden* to *Say It with Charts*, link updated to Amazon.
- Replaced all economic examples in Chapter 08 with everyday topics: revenue/products/companies → sports participants, hobbies, city comparisons (Berlin vs Munich).

#### Prompts used

1. "At the beginning of 6, the references are broken. Please fix."
2. "I am using python3, and Python3 as notation. Change all this to Python. Do not touch, if in curly braces."
3. "In 02, 03, 04, 05, 06, I have added comments starting with xxx. Please do what I wrote there, and delete the comment."
4. "Please get rid of all qmd files not needed in the _quarto."
5. "Wie aus Zahlen Bilder werden heißt offenbar Say it with Charts auf englisch. Bitte alle Textstellen updaten, und die Links auf https://www.amazon.de/Say-Charts-Executivess-Communication-Executives/dp/007136997X setzen."
6. "In Chapter 8, to my taste, the examples are way too economically driven. Please change that by using other fields of normal life (sports, hobbies, traveling) etc."
