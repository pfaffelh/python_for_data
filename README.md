These are the course notes for a course on python for data analysis in Summer 2026 at the University of Freiburg, Germany.

The notes use `quarto`. This means, after install [`quarto`](https://quarto.org/docs/get-started/), you can render one file of the course notes (pdf and ipnyb) by typing
```
quarto render 00_Getting_started.qmd
```
If you want all in one go, type
```
quarto render
```
This takes a few minutes. 
If you enter
```
python -m http.server
```
you will find yourself be able to click on the files you would like to see. 


TODOs: 
* Added to basics (marked _claude generated_): string formatting (Ch 02), type hints/assertions (Ch 03), file I/O (Ch 03).
* Chapter 11 has been moved to `archive/` (excluded via `.gitignore`).
* Make 5 suggestions what else could be covered in 10 misc
* Add a remark on what you just did in the section on AI usage.
* Please add 11_Exercises.qmd, where you list several more exercises, from easy to hard, with one header for each section. For each section, add 4 exercises. 
* Add a folder solutions, and add it to .gitignore. In this folder, solve all exercises in the chapter which were already there, and also your new exercises. 


For worldbank data:

from pandas_datareader import wb

Maybe add?

PCA / dimensionality reduction — mentioned in the index as a goal but not covered yet. A natural fit for chapter 09 given you already have np.linalg and linear regression.
Reshaping data (pivot, melt, pivot_table) — very common in practice, missing from chapter 07.
Window/rolling functions in pandas (moving averages, cumulative sums) — useful for time series in the example project.