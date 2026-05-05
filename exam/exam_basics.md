# Exam: Python Basics (Chapters 2–5)

**Duration:** 30 minutes.
**No computers, books, or notes.**
**Instructions:** Each question has exactly one correct answer. Mark it clearly.

---

## Chapter 2 — Simple data types

**1.** What is the type of the value `3.0` in Python?

- (a) `int`
- (b) `float`
- (c) `double`
- (d) `decimal`

**2.** What does the expression `7 // 2` evaluate to?

- (a) `3.5`
- (b) `3`
- (c) `4`
- (d) `3.0`

**3.** What does `7 % 3` evaluate to?

- (a) `2`
- (b) `1`
- (c) `0`
- (d) `2.3333`

**4.** What is the result of `2 ** 10`?

- (a) `20`
- (b) `100`
- (c) `1024`
- (d) `512`

**5.** Which of the following is `True`?

- (a) `True and False`
- (b) `not (1 == 1)`
- (c) `True ^ False`
- (d) `False or False`

**6.** Let `z = float("nan")`. What is the value of `z == z`?

- (a) `True`
- (b) `False`
- (c) `None`
- (d) It raises an error.

**7.** What does `"ab" * 3` evaluate to?

- (a) `"ababab"`
- (b) `"ab ab ab"`
- (c) `"abababab"`
- (d) Error: strings cannot be multiplied.

**8.** Let `name = "Alice"`. Which expression produces the string `"Hello, Alice!"`?

- (a) `"Hello, name!"`
- (b) `"Hello, " + name + "!"`
- (c) `"Hello, {name}!"`
- (d) `f"Hello, {"name"}!"`

**9.** What is the value of `"th" in "Python"`?

- (a) `True`
- (b) `False`
- (c) `"th"`
- (d) Error: `in` does not work on strings.

**10.** Which of the following is the correct way to check whether a variable `x` is `None`?

- (a) `x == None`
- (b) `x is None`
- (c) `x = None`
- (d) `None(x)`

**11.** What does the f-string `f"{3.14159:.2f}"` produce?

- (a) `"3.14"`
- (b) `"3.14159"`
- (c) `"3.1"`
- (d) `"3.14e+00"`

**12.** What is the value of `int(3.8)`?

- (a) `4`
- (b) `3.8`
- (c) `3`
- (d) Error: cannot convert float to int.

**13.** Which statement about Python integers is correct?

- (a) They are limited to 32 bits.
- (b) They are limited to 64 bits.
- (c) Their size is limited only by available memory.
- (d) They cannot be negative.

---

## Chapter 3 — Control flow: conditions, loops, functions

**14.** What does `range(5)` represent?

- (a) The numbers `1, 2, 3, 4, 5`
- (b) The numbers `0, 1, 2, 3, 4`
- (c) The numbers `0, 1, 2, 3, 4, 5`
- (d) A single integer `5`

**15.** What does `list(range(1, 10, 3))` evaluate to?

- (a) `[1, 4, 7]`
- (b) `[1, 4, 7, 10]`
- (c) `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- (d) `[3, 6, 9]`

**16.** Which keyword immediately stops the execution of a `for`-loop?

- (a) `continue`
- (b) `stop`
- (c) `break`
- (d) `return`

**17.** What is printed by the following code?

```python
for i in range(4):
    if i == 2:
        continue
    print(i, end=" ")
```

- (a) `0 1 2 3`
- (b) `0 1 3`
- (c) `0 1`
- (d) `0 1 2`

**18.** Consider the function

```python
def greeting(name, prefix="Hello"):
    print(f"{prefix}, {name}!")
```

Which call prints `Hi, Bob!`?

- (a) `greeting("Hi", "Bob")`
- (b) `greeting(name="Bob", prefix="Hi")`
- (c) `greeting("Bob")`
- (d) `greeting(prefix="Bob", name="Hi")`

**19.** What is a **docstring**?

- (a) A comment starting with `#`.
- (b) A multiline string placed right after the `def`-line, describing what the function does.
- (c) A special `print` statement inside a function.
- (d) A file with `.doc` extension containing documentation.

**20.** Which of the following defines a valid `lambda`-function that squares its argument?

- (a) `lambda x: x ** 2`
- (b) `lambda(x) = x ** 2`
- (c) `def lambda x: x*x`
- (d) `lambda x -> x ** 2`

**21.** Which exception is raised by `int("abc")`?

- (a) `TypeError`
- (b) `NameError`
- (c) `ValueError`
- (d) `SyntaxError`

**22.** Which exception is raised by `1 / 0`?

- (a) `ValueError`
- (b) `ArithmeticError`
- (c) `TypeError`
- (d) `ZeroDivisionError`

**23.** What is the purpose of the `with` statement when opening a file?

- (a) To speed up reading.
- (b) To automatically close the file when the block ends.
- (c) To open the file in read-only mode.
- (d) To encrypt the file.

**24.** Which mode opens a file for appending text at the end?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"x"`

**25.** What is the output of the following code?

```python
res = 5 if 2 > 3 else 10
print(res)
```

- (a) `5`
- (b) `10`
- (c) `True`
- (d) Error

**26.** Inside a function, a variable is assigned a value. After the function returns, what happens to that variable (assuming no `global` or `return`)?

- (a) It keeps its new value outside the function.
- (b) It is deleted and no longer accessible outside.
- (c) It causes an error.
- (d) It overwrites any outer variable of the same name.

---

## Chapter 4 — Container data types

**27.** Given `a = [10, 20, 30, 40, 50]`, what is `a[1:4]`?

- (a) `[10, 20, 30]`
- (b) `[20, 30, 40]`
- (c) `[20, 30, 40, 50]`
- (d) `[10, 20, 30, 40]`

**28.** Given `a = [10, 20, 30, 40]`, what is `a[-1]`?

- (a) `10`
- (b) `40`
- (c) `-1`
- (d) Error

**29.** Which of the following is **immutable**?

- (a) `list`
- (b) `dict`
- (c) `set`
- (d) `tuple`

**30.** What is the type of `(5)` in Python?

- (a) `tuple`
- (b) `int`
- (c) `list`
- (d) `set`

**31.** What is `len({1, 2, 2, 3, 3, 3})`?

- (a) `3`
- (b) `6`
- (c) `1`
- (d) Error: sets cannot contain duplicates.

**32.** Given `s = {1, 2, 3}` and `t = {3, 4, 5}`, what is `s & t`?

- (a) `{1, 2, 3, 4, 5}`
- (b) `{3}`
- (c) `{1, 2}`
- (d) `set()`

**33.** Given `l = [3, 1, 2]`, what does `print(l.sort())` print?

- (a) `[1, 2, 3]`
- (b) `[3, 2, 1]`
- (c) `None`
- (d) `[3, 1, 2]`

**34.** Which expression returns a new sorted list without changing the original list `l`?

- (a) `l.sort()`
- (b) `sorted(l)`
- (c) `l.sorted()`
- (d) `sort(l)`

**35.** Given `d = {"a": 1, "b": 2}`, what does `d.get("c", 0)` return?

- (a) `None`
- (b) `0`
- (c) An error
- (d) `"c"`

**36.** Which of the following cannot be used as a dictionary key?

- (a) `"name"`
- (b) `42`
- (c) `(1, 2)`
- (d) `[1, 2]`

**37.** What does the following code print?

```python
names = ["Alice", "Bob"]
scores = [90, 80]
for n, s in zip(names, scores):
    print(n, s)
```

- (a) `Alice Bob` then `90 80`
- (b) `Alice 90` then `Bob 80`
- (c) `("Alice", 90)` then `("Bob", 80)`
- (d) Error

**38.** What does `[x*x for x in range(4)]` evaluate to?

- (a) `[0, 1, 4, 9]`
- (b) `[1, 4, 9, 16]`
- (c) `[0, 2, 4, 6]`
- (d) `[0, 1, 2, 3]`

**39.** What does `[x for x in range(10) if x % 2 == 0]` evaluate to?

- (a) `[1, 3, 5, 7, 9]`
- (b) `[0, 2, 4, 6, 8]`
- (c) `[0, 2, 4, 6, 8, 10]`
- (d) `[2, 4, 6, 8]`

**40.** Given `l = [True, True, False]`, what does `all(l)` return?

- (a) `True`
- (b) `False`
- (c) `2`
- (d) `None`

**41.** What does `enumerate(["a", "b", "c"])` produce when iterated over?

- (a) `"a", "b", "c"`
- (b) `(0, "a"), (1, "b"), (2, "c")`
- (c) `(1, "a"), (2, "b"), (3, "c")`
- (d) `("a", 0), ("b", 1), ("c", 2)`

**42.** What does the following code print?

```python
l = [1, 2, 3]
l.append([4, 5])
print(len(l))
```

- (a) `3`
- (b) `4`
- (c) `5`
- (d) Error

---

## Chapter 5 — Libraries

**43.** Suppose `one.py` contains a function `myConst()`. In `two.py`, which import statement lets you call it as `myConst()` (without a prefix)?

- (a) `import one`
- (b) `import one as myConst`
- (c) `from one import myConst`
- (d) `import myConst from one`

**44.** Which import gives you access to `math.pi`?

- (a) `import pi`
- (b) `from math import *` only
- (c) `import math`
- (d) `include math`

**45.** You have a string `"21.4.26, 12:15"` and want to convert it into a `datetime` object. Which function do you use?

- (a) `datetime.datetime.strftime`
- (b) `datetime.datetime.strptime`
- (c) `datetime.parse`
- (d) `datetime.convert`

**46.** Given a `datetime` object `dt`, how do you get the date exactly 7 days later?

- (a) `dt + 7`
- (b) `dt + datetime.timedelta(days=7)`
- (c) `dt.add(7)`
- (d) `dt + datetime.date(7)`

**47.** Why does `Decimal('0.1') + Decimal('0.2')` give an exact result, but `0.1 + 0.2` does not?

- (a) `Decimal` uses a base-10 representation, while `float` uses base 2.
- (b) `Decimal` is faster than `float`.
- (c) `float` is deprecated in recent Python versions.
- (d) They both give the same exact result.

**48.** Which library is used to find patterns like email addresses in a string?

- (a) `os`
- (b) `pickle`
- (c) `re`
- (d) `math`

**49.** What is the purpose of the `pickle` library?

- (a) Handling dates and times.
- (b) Serializing Python objects to a file and loading them back.
- (c) Running tests.
- (d) Finding patterns in strings.

**50.** What does `assert 2 + 2 == 5` do when executed?

- (a) Nothing; the line is silently ignored.
- (b) It prints `False`.
- (c) It raises an `AssertionError`.
- (d) It returns `False`.

---

## Answer key

| # | Ans | # | Ans | # | Ans | # | Ans | # | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 11 | a | 21 | c | 31 | a | 41 | b |
| 2 | b | 12 | c | 22 | d | 32 | b | 42 | b |
| 3 | b | 13 | c | 23 | b | 33 | c | 43 | c |
| 4 | c | 14 | b | 24 | c | 34 | b | 44 | c |
| 5 | c | 15 | a | 25 | b | 35 | b | 45 | b |
| 6 | b | 16 | c | 26 | b | 36 | d | 46 | b |
| 7 | a | 17 | b | 27 | b | 37 | b | 47 | a |
| 8 | b | 18 | b | 28 | b | 38 | a | 48 | c |
| 9 | a | 19 | b | 29 | d | 39 | b | 49 | b |
| 10 | b | 20 | a | 30 | b | 40 | b | 50 | c |
