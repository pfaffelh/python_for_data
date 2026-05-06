# Exam: Python Basics (Chapters 2–5)

**Format**: 10-15 from the questions below will be selected.
**Duration:** 45 minutes.
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

**14.** What is the result of `10 / 4` in Python?

- (a) `2`
- (b) `2.5`
- (c) `2.0`
- (d) `3`

**15.** What is the result of `10 / 2` in Python?

- (a) `5`
- (b) `5.0`
- (c) `5.5`
- (d) Error

**16.** What is the result of `-7 // 2`?

- (a) `-3`
- (b) `-4`
- (c) `-3.5`
- (d) `3`

**17.** What does `abs(-5.5)` return?

- (a) `-5.5`
- (b) `5`
- (c) `5.5`
- (d) Error

**18.** What does `round(3.14159, 2)` return?

- (a) `3.14`
- (b) `3.15`
- (c) `3.1`
- (d) `3`

**19.** What is `0.1 + 0.2 == 0.3` in Python?

- (a) `True`
- (b) `False`
- (c) Error
- (d) `None`

**20.** What does `type(3 == 3)` return?

- (a) `<class 'int'>`
- (b) `<class 'bool'>`
- (c) `<class 'str'>`
- (d) `<class 'NoneType'>`

**21.** What is the value of `True + True + False`?

- (a) `2`
- (b) `True`
- (c) `3`
- (d) Error

**22.** What does `bool(0)` return?

- (a) `True`
- (b) `False`
- (c) `0`
- (d) Error

**23.** What does `bool("")` return?

- (a) `True`
- (b) `False`
- (c) `""`
- (d) Error

**24.** What does `bool([])` return?

- (a) `True`
- (b) `False`
- (c) `[]`
- (d) Error

**25.** Which expression evaluates to `True`?

- (a) `1 == "1"`
- (b) `1 == 1.0`
- (c) `"1" == 1.0`
- (d) `None == 0`

**26.** What is the value of `"Python"[0]`?

- (a) `"P"`
- (b) `"y"`
- (c) `0`
- (d) Error

**27.** What is the value of `"Python"[-1]`?

- (a) `"P"`
- (b) `"n"`
- (c) `"y"`
- (d) Error

**28.** What is the value of `"Python"[1:4]`?

- (a) `"Pyt"`
- (b) `"yth"`
- (c) `"ytho"`
- (d) `"Pyth"`

**29.** What does `len("Python")` return?

- (a) `5`
- (b) `6`
- (c) `7`
- (d) Error

**30.** What does `"hello".upper()` return?

- (a) `"hello"`
- (b) `"HELLO"`
- (c) `"Hello"`
- (d) Error

**31.** What does `"HELLO".lower()` return?

- (a) `"hello"`
- (b) `"HELLO"`
- (c) `"Hello"`
- (d) Error

**32.** What does `"  hello  ".strip()` return?

- (a) `"hello"`
- (b) `"  hello  "`
- (c) `"hello  "`
- (d) `"  hello"`

**33.** What does `"a,b,c".split(",")` return?

- (a) `"a b c"`
- (b) `["a", "b", "c"]`
- (c) `("a", "b", "c")`
- (d) `"abc"`

**34.** What does `",".join(["a", "b", "c"])` return?

- (a) `"a,b,c"`
- (b) `["a,b,c"]`
- (c) `"a, b, c"`
- (d) Error

**35.** What does `"Python".replace("P", "J")` return?

- (a) `"Python"`
- (b) `"Jython"`
- (c) `"Pjthon"`
- (d) Error

**36.** What does `"Python".endswith("py")` return?

- (a) `True`
- (b) `False`
- (c) `"py"`
- (d) Error

**37.** What does `"abc".isalpha()` return?

- (a) `True`
- (b) `False`
- (c) `"abc"`
- (d) Error

**38.** What does `"123".isdigit()` return?

- (a) `True`
- (b) `False`
- (c) `123`
- (d) Error

**39.** What does `str(42)` return?

- (a) `42`
- (b) `"42"`
- (c) `"'42'"`
- (d) Error

**40.** What does `int("42")` return?

- (a) `"42"`
- (b) `42`
- (c) `42.0`
- (d) Error

**41.** What does `float("3.14")` return?

- (a) `3.14`
- (b) `"3.14"`
- (c) `3`
- (d) Error

**42.** Which character can start a valid Python variable name?

- (a) A digit
- (b) A space
- (c) A letter or underscore
- (d) A hyphen

**43.** Which of the following is NOT a valid Python variable name?

- (a) `my_var`
- (b) `_x`
- (c) `2nd_value`
- (d) `value2`

**44.** What does `type(5)` return?

- (a) `<class 'int'>`
- (b) `<class 'float'>`
- (c) `<class 'number'>`
- (d) `5`

**45.** What is the result of `not True`?

- (a) `True`
- (b) `False`
- (c) `0`
- (d) Error

**46.** How many bits does a standard Python `float` use internally?

- (a) 32
- (b) 64
- (c) 128
- (d) Unlimited

**47.** In a float, which part stores the precision of the number?

- (a) the exponent
- (b) the mantissa
- (c) the sign bit
- (d) the base

---

## Chapter 3 — Control flow: conditions, loops, functions

**48.** What does `range(5)` represent?

- (a) The numbers `1, 2, 3, 4, 5`
- (b) The numbers `0, 1, 2, 3, 4`
- (c) The numbers `0, 1, 2, 3, 4, 5`
- (d) A single integer `5`

**49.** What does `list(range(1, 10, 3))` evaluate to?

- (a) `[1, 4, 7]`
- (b) `[1, 4, 7, 10]`
- (c) `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- (d) `[3, 6, 9]`

**50.** Which keyword immediately stops the execution of a `for`-loop?

- (a) `continue`
- (b) `stop`
- (c) `break`
- (d) `return`

**51.** What is printed by the following code?

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

**52.** Consider the function

```python
def greeting(name, prefix="Hello"):
    print(f"{prefix}, {name}!")
```

Which call prints `Hi, Bob!`?

- (a) `greeting("Hi", "Bob")`
- (b) `greeting(name="Bob", prefix="Hi")`
- (c) `greeting("Bob")`
- (d) `greeting(prefix="Bob", name="Hi")`

**53.** What is a **docstring**?

- (a) A comment starting with `#`.
- (b) A multiline string placed right after the `def`-line, describing what the function does.
- (c) A special `print` statement inside a function.
- (d) A file with `.doc` extension containing documentation.

**54.** Which of the following defines a valid `lambda`-function that squares its argument?

- (a) `lambda x: x ** 2`
- (b) `lambda(x) = x ** 2`
- (c) `def lambda x: x*x`
- (d) `lambda x -> x ** 2`

**55.** Which exception is raised by `int("abc")`?

- (a) `TypeError`
- (b) `NameError`
- (c) `ValueError`
- (d) `SyntaxError`

**56.** Which exception is raised by `1 / 0`?

- (a) `ValueError`
- (b) `ArithmeticError`
- (c) `TypeError`
- (d) `ZeroDivisionError`

**57.** What is the purpose of the `with` statement when opening a file?

- (a) To speed up reading.
- (b) To automatically close the file when the block ends.
- (c) To open the file in read-only mode.
- (d) To encrypt the file.

**58.** Which mode opens a file for appending text at the end?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"x"`

**59.** What is the output of the following code?

```python
res = 5 if 2 > 3 else 10
print(res)
```

- (a) `5`
- (b) `10`
- (c) `True`
- (d) Error

**60.** Inside a function, a variable is assigned a value. After the function returns, what happens to that variable (assuming no `global` or `return`)?

- (a) It keeps its new value outside the function.
- (b) It is deleted and no longer accessible outside.
- (c) It causes an error.
- (d) It overwrites any outer variable of the same name.

**61.** What is the output of `list(range(5, 0, -1))`?

- (a) `[5, 4, 3, 2, 1]`
- (b) `[5, 4, 3, 2, 1, 0]`
- (c) `[4, 3, 2, 1, 0]`
- (d) `[1, 2, 3, 4, 5]`

**62.** What is the output of `list(range(3, 3))`?

- (a) `[3]`
- (b) `[]`
- (c) `[3, 3]`
- (d) Error

**63.** What does the following code print?

```python
i = 0
while i < 3:
    print(i, end=" ")
    i += 1
```

- (a) `0 1 2`
- (b) `0 1 2 3`
- (c) `1 2 3`
- (d) Infinite loop

**64.** What does `continue` do inside a loop?

- (a) Exits the loop.
- (b) Skips the remainder of the current iteration and moves to the next.
- (c) Pauses execution.
- (d) Raises an exception.

**65.** What does the following code print?

```python
def f():
    return 1, 2, 3
x = f()
print(type(x))
```

- (a) `<class 'list'>`
- (b) `<class 'tuple'>`
- (c) `<class 'int'>`
- (d) `<class 'set'>`

**66.** A function without a `return` statement implicitly returns:

- (a) `0`
- (b) `False`
- (c) `None`
- (d) An empty string

**67.** Consider the code:

```python
def add(a, b=1):
    return a + b
print(add(3))
```

What is printed?

- (a) `3`
- (b) `4`
- (c) Error: missing argument
- (d) `None`

**68.** What is the output of the following code?

```python
x = 10
def f():
    x = 20
f()
print(x)
```

- (a) `10`
- (b) `20`
- (c) Error
- (d) `None`

**69.** What is a recursive function?

- (a) A function that returns multiple values.
- (b) A function that calls itself.
- (c) A function without parameters.
- (d) A built-in function.

**70.** What is `list(filter(lambda x: x > 2, [1, 2, 3, 4]))`?

- (a) `[1, 2]`
- (b) `[3, 4]`
- (c) `[2, 3, 4]`
- (d) `[True, True]`

**71.** What does `sorted([3, 1, 2], key=lambda x: -x)` return?

- (a) `[1, 2, 3]`
- (b) `[3, 2, 1]`
- (c) `[-3, -2, -1]`
- (d) `[-1, -2, -3]`

**72.** Which statement raises a custom exception?

- (a) `throw ValueError("bad")`
- (b) `raise ValueError("bad")`
- (c) `error ValueError("bad")`
- (d) `except ValueError("bad")`

**73.** Which exception is raised by `[1, 2, 3][10]`?

- (a) `KeyError`
- (b) `IndexError`
- (c) `ValueError`
- (d) `TypeError`

**74.** Which exception is raised by `{"a": 1}["b"]`?

- (a) `KeyError`
- (b) `IndexError`
- (c) `ValueError`
- (d) `AttributeError`

**75.** Which exception is raised when a file cannot be found?

- (a) `IOError`
- (b) `FileNotFoundError`
- (c) `ValueError`
- (d) `NameError`

**76.** Which file mode truncates the file if it already exists?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"r+"`

**77.** Which file mode fails if the file already exists?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"x"`

**78.** What does `f.readlines()` return when called on a file object `f`?

- (a) A single string.
- (b) A list of strings, one per line.
- (c) A generator.
- (d) The number of lines.

**79.** What is the output of the following code?

```python
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(j, end=" ")
    print(".", end=" ")
```

- (a) `0 1 . 0 1 . 0 1 . `
- (b) `0 1 2 . 0 1 2 . 0 1 2 . `
- (c) `0 1 .`
- (d) `0 1`

**80.** Which keyword is used to define a function in Python?

- (a) `function`
- (b) `def`
- (c) `func`
- (d) `lambda`

**81.** What does `match`/`case` in Python (3.10+) implement?

- (a) A regex matcher.
- (b) Structural pattern matching (similar to switch-case).
- (c) A new loop construct.
- (d) A type annotation.

**82.** What is the output of the following code?

```python
def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)
print(f(4))
```

- (a) `24`
- (b) `10`
- (c) `1`
- (d) Error

**83.** What is the value of `sum([1, 2, 3, 4])`?

- (a) `10`
- (b) `[1, 2, 3, 4]`
- (c) `6`
- (d) Error

**84.** What happens when a `while True:` loop has no `break`?

- (a) It runs once.
- (b) It runs forever (infinite loop).
- (c) It raises an error.
- (d) It runs until Python is restarted automatically.

**85.** Which statement is required to exit a function and return a value?

- (a) `exit`
- (b) `return`
- (c) `break`
- (d) `stop`

**86.** What is the output of:

```python
try:
    raise ValueError("bad")
except ValueError as e:
    print(str(e))
```

- (a) `"ValueError"`
- (b) `"bad"`
- (c) `None`
- (d) Error

---

## Chapter 4 — Container data types

**87.** Given `a = [10, 20, 30, 40, 50]`, what is `a[1:4]`?

- (a) `[10, 20, 30]`
- (b) `[20, 30, 40]`
- (c) `[20, 30, 40, 50]`
- (d) `[10, 20, 30, 40]`

**88.** Given `a = [10, 20, 30, 40]`, what is `a[-1]`?

- (a) `10`
- (b) `40`
- (c) `-1`
- (d) Error

**89.** Which of the following is **immutable**?

- (a) `list`
- (b) `dict`
- (c) `set`
- (d) `tuple`

**90.** What is the type of `(5)` in Python?

- (a) `tuple`
- (b) `int`
- (c) `list`
- (d) `set`

**91.** What is `len({1, 2, 2, 3, 3, 3})`?

- (a) `3`
- (b) `6`
- (c) `1`
- (d) Error: sets cannot contain duplicates.

**92.** Given `s = {1, 2, 3}` and `t = {3, 4, 5}`, what is `s & t`?

- (a) `{1, 2, 3, 4, 5}`
- (b) `{3}`
- (c) `{1, 2}`
- (d) `set()`

**93.** Given `l = [3, 1, 2]`, what does `print(l.sort())` print?

- (a) `[1, 2, 3]`
- (b) `[3, 2, 1]`
- (c) `None`
- (d) `[3, 1, 2]`

**94.** Which expression returns a new sorted list without changing the original list `l`?

- (a) `l.sort()`
- (b) `sorted(l)`
- (c) `l.sorted()`
- (d) `sort(l)`

**95.** Given `d = {"a": 1, "b": 2}`, what does `d.get("c", 0)` return?

- (a) `None`
- (b) `0`
- (c) An error
- (d) `"c"`

**96.** Which of the following cannot be used as a dictionary key?

- (a) `"name"`
- (b) `42`
- (c) `(1, 2)`
- (d) `[1, 2]`

**97.** What does the following code print?

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

**98.** What does `[x*x for x in range(4)]` evaluate to?

- (a) `[0, 1, 4, 9]`
- (b) `[1, 4, 9, 16]`
- (c) `[0, 2, 4, 6]`
- (d) `[0, 1, 2, 3]`

**99.** What does `[x for x in range(10) if x % 2 == 0]` evaluate to?

- (a) `[1, 3, 5, 7, 9]`
- (b) `[0, 2, 4, 6, 8]`
- (c) `[0, 2, 4, 6, 8, 10]`
- (d) `[2, 4, 6, 8]`

**100.** Given `l = [True, True, False]`, what does `all(l)` return?

- (a) `True`
- (b) `False`
- (c) `2`
- (d) `None`

**101.** What does `enumerate(["a", "b", "c"])` produce when iterated over?

- (a) `"a", "b", "c"`
- (b) `(0, "a"), (1, "b"), (2, "c")`
- (c) `(1, "a"), (2, "b"), (3, "c")`
- (d) `("a", 0), ("b", 1), ("c", 2)`

**102.** What does the following code print?

```python
l = [1, 2, 3]
l.append([4, 5])
print(len(l))
```

- (a) `3`
- (b) `4`
- (c) `5`
- (d) Error

**103.** What does the following code print?

```python
l = [1, 2, 3]
l.extend([4, 5])
print(len(l))
```

- (a) `3`
- (b) `4`
- (c) `5`
- (d) Error

**104.** What is the difference between `l.append(x)` and `l.extend(x)`?

- (a) They are identical.
- (b) `append` adds `x` as a single element; `extend` adds each element of `x`.
- (c) `extend` adds `x` as a single element; `append` adds each element of `x`.
- (d) Only `extend` modifies the original list.

**105.** Given `l = [1, 2, 3]`, what is `l.pop()`?

- (a) `1`
- (b) `3`
- (c) `[1, 2]`
- (d) `None`

**106.** Given `l = [10, 20, 30]`, what is `l.pop(0)`?

- (a) `10`
- (b) `30`
- (c) `[20, 30]`
- (d) `None`

**107.** Given `l = [1, 2, 3, 2]`, what does `l.remove(2)` do?

- (a) Removes all `2`s.
- (b) Removes the first `2`.
- (c) Removes the last `2`.
- (d) Returns a new list.

**108.** Given `l = [1, 2, 3]`, what is `l.index(2)`?

- (a) `0`
- (b) `1`
- (c) `2`
- (d) `3`

**109.** Given `l = [1, 2, 2, 3, 2]`, what is `l.count(2)`?

- (a) `1`
- (b) `2`
- (c) `3`
- (d) `4`

**110.** What does the following code print?

```python
l = [1, 2, 3]
l.insert(1, 99)
print(l)
```

- (a) `[1, 99, 2, 3]`
- (b) `[99, 1, 2, 3]`
- (c) `[1, 2, 3, 99]`
- (d) `[1, 2, 99, 3]`

**111.** Given `l = [1, 2, 3]`, what does `l.reverse()` return?

- (a) `[3, 2, 1]`
- (b) `[1, 2, 3]`
- (c) `None`
- (d) A new list

**112.** What is the value of `[1, 2] + [3, 4]`?

- (a) `[1, 2, 3, 4]`
- (b) `[4, 6]`
- (c) `[[1, 2], [3, 4]]`
- (d) Error

**113.** What is `"hello"[::2]`?

- (a) `"hlo"`
- (b) `"hello"`
- (c) `"el"`
- (d) `"olleh"`

**114.** What does `3 in [1, 2, 3]` return?

- (a) `True`
- (b) `False`
- (c) `3`
- (d) Error

**115.** Given the assignment `a, b = (1, 2)`, what is `b`?

- (a) `1`
- (b) `2`
- (c) `(1, 2)`
- (d) Error

**116.** What does the assignment `a, b = b, a` do?

- (a) Sets `a` and `b` both to `None`.
- (b) Swaps the values of `a` and `b`.
- (c) Raises a syntax error.
- (d) Creates a tuple `(a, b)`.

**117.** Which of the following creates a tuple with a single element `5`?

- (a) `(5)`
- (b) `[5]`
- (c) `(5,)`
- (d) `{5}`

**118.** What is `()` in Python?

- (a) An empty list
- (b) An empty tuple
- (c) An empty set
- (d) `None`

**119.** What is `{}` in Python?

- (a) An empty set
- (b) An empty dictionary
- (c) An empty list
- (d) `None`

**120.** How can you create an empty set in Python?

- (a) `{}`
- (b) `[]`
- (c) `set()`
- (d) `empty_set()`

**121.** Given `s = {1, 2, 3}` and `t = {3, 4}`, what is `s | t`?

- (a) `{3}`
- (b) `{1, 2, 3, 4}`
- (c) `{1, 2}`
- (d) `set()`

**122.** Given `s = {1, 2, 3}` and `t = {3, 4}`, what is `s - t`?

- (a) `{1, 2}`
- (b) `{3}`
- (c) `{4}`
- (d) `set()`

**123.** Given `d = {"a": 1, "b": 2}`, what does `d["a"]` return?

- (a) `1`
- (b) `"a"`
- (c) `("a", 1)`
- (d) Error

**124.** Given `d = {"a": 1, "b": 2}`, what does `list(d.keys())` return?

- (a) `["a", "b"]`
- (b) `[1, 2]`
- (c) `[("a", 1), ("b", 2)]`
- (d) `[]`

**125.** Given `d = {"a": 1, "b": 2}`, what does `list(d.values())` return?

- (a) `["a", "b"]`
- (b) `[1, 2]`
- (c) `[("a", 1), ("b", 2)]`
- (d) `[]`

**126.** Given `d = {"a": 1, "b": 2}`, what does `list(d.items())` return?

- (a) `[("a", 1), ("b", 2)]`
- (b) `["a", 1, "b", 2]`
- (c) `[{"a": 1}, {"b": 2}]`
- (d) `[]`

**127.** What is `{x: x**2 for x in range(4)}`?

- (a) `{0: 0, 1: 1, 2: 4, 3: 9}`
- (b) `[0, 1, 4, 9]`
- (c) `{0, 1, 4, 9}`
- (d) Error

**128.** What does `d.update({"c": 3})` do to the dictionary `d`?

- (a) Replaces `d` entirely with `{"c": 3}`.
- (b) Adds or updates the key `"c"` in `d`.
- (c) Returns a new dictionary.
- (d) Raises an error.

**129.** What does `del d["a"]` do?

- (a) Deletes the value `"a"` from any key in `d`.
- (b) Removes the key `"a"` (and its value) from `d`.
- (c) Sets `d["a"]` to `None`.
- (d) Deletes the dictionary `d`.

**130.** What does `any([False, 0, None, ""])` return?

- (a) `True`
- (b) `False`
- (c) `None`
- (d) Error

**131.** What does `min([3, 1, 2, 5])` return?

- (a) `1`
- (b) `3`
- (c) `5`
- (d) `2`

**132.** What does `sorted(["banana", "pie", "apple"], key=len)` return?

- (a) `["apple", "banana", "pie"]`
- (b) `["pie", "apple", "banana"]`
- (c) `["banana", "apple", "pie"]`
- (d) `["apple", "pie", "banana"]`

**133.** What does the following code print?

```python
d = {"a": [1, 2], "b": [3, 4]}
for k, v in d.items():
    print(k, sum(v))
```

- (a) `a 3` then `b 7`
- (b) `a [1, 2]` then `b [3, 4]`
- (c) `1 2` then `3 4`
- (d) Error

**134.** Given `t = (1, 2, 3)`, what does `t[0] = 10` do?

- (a) Changes the first element to `10`.
- (b) Raises `TypeError`: tuples are immutable.
- (c) Creates a new tuple.
- (d) Does nothing.

**135.** What does `set([1, 2, 2, 3])` return?

- (a) `{1, 2, 3}`
- (b) `[1, 2, 3]`
- (c) `(1, 2, 3)`
- (d) Error

**136.** Which expression gets every second element of a list `l`?

- (a) `l[0::2]`
- (b) `l[1::2]`
- (c) `l[::2]`
- (d) Both (a) and (c)

**137.** Given `matrix = [[1, 2], [3, 4], [5, 6]]`, what is `matrix[1][0]`?

- (a) `1`
- (b) `2`
- (c) `3`
- (d) `4`

**138.** What does `"".join(["a", "b", "c"])` return?

- (a) `"abc"`
- (b) `"a, b, c"`
- (c) `["abc"]`
- (d) `["a", "b", "c"]`

---

## Chapter 5 — Libraries

**139.** Suppose `one.py` contains a function `myConst()`. In `two.py`, which import statement lets you call it as `myConst()` (without a prefix)?

- (a) `import one`
- (b) `import one as myConst`
- (c) `from one import myConst`
- (d) `import myConst from one`

**140.** Which import gives you access to `math.pi`?

- (a) `import pi`
- (b) `from math import *` only
- (c) `import math`
- (d) `include math`

**141.** You have a string `"21.4.26, 12:15"` and want to convert it into a `datetime` object. Which function do you use?

- (a) `datetime.datetime.strftime`
- (b) `datetime.datetime.strptime`
- (c) `datetime.parse`
- (d) `datetime.convert`

**142.** Given a `datetime` object `dt`, how do you get the date exactly 7 days later?

- (a) `dt + 7`
- (b) `dt + datetime.timedelta(days=7)`
- (c) `dt.add(7)`
- (d) `dt + datetime.date(7)`

**143.** Why does `Decimal('0.1') + Decimal('0.2')` give an exact result, but `0.1 + 0.2` does not?

- (a) `Decimal` uses a base-10 representation, while `float` uses base 2.
- (b) `Decimal` is faster than `float`.
- (c) `float` is deprecated in recent Python versions.
- (d) They both give the same exact result.

**144.** Which library is used to find patterns like email addresses in a string?

- (a) `os`
- (b) `pickle`
- (c) `re`
- (d) `math`

**145.** What is the purpose of the `pickle` library?

- (a) Handling dates and times.
- (b) Serializing Python objects to a file and loading them back.
- (c) Running tests.
- (d) Finding patterns in strings.

**146.** What does `assert 2 + 2 == 5` do when executed?

- (a) Nothing; the line is silently ignored.
- (b) It prints `False`.
- (c) It raises an `AssertionError`.
- (d) It returns `False`.

**147.** What does `math.sqrt(16)` return?

- (a) `4`
- (b) `4.0`
- (c) `16`
- (d) Error

**148.** What is the approximate value of `math.e`?

- (a) `2.718`
- (b) `3.141`
- (c) `1.618`
- (d) `1.414`

**149.** What does `math.log(math.e)` return?

- (a) `0`
- (b) `1.0`
- (c) `2.718`
- (d) Error

**150.** What does `math.sin(math.pi / 2)` return?

- (a) `0.0`
- (b) `1.0`
- (c) `-1.0`
- (d) `math.pi / 2`

**151.** Given `dt = datetime.datetime(2026, 3, 27, 12, 0)`, what does `dt.strftime("%Y-%m-%d")` return?

- (a) `"2026-03-27"`
- (b) `"27-03-2026"`
- (c) `"2026/03/27"`
- (d) `"%Y-%m-%d"`

**152.** Given two `datetime` objects `a` and `b`, what is the type of `a - b`?

- (a) `datetime`
- (b) `timedelta`
- (c) `int`
- (d) `float`

**153.** Which of the following is a regex module function that finds ALL non-overlapping matches?

- (a) `re.match`
- (b) `re.search`
- (c) `re.findall`
- (d) `re.split`

**154.** Which module provides operating-system-level functionality like listing directory contents?

- (a) `os`
- (b) `sys`
- (c) `io`
- (d) `pathlib`

**155.** What does `pickle.dump(obj, f)` do?

- (a) Writes `obj` to the open binary file `f`.
- (b) Prints `obj`.
- (c) Returns `obj` as a string.
- (d) Reads `obj` from `f`.

---

## Answer key

| # | Ans | # | Ans | # | Ans | # | Ans | # | Ans |
|---|-----|---|-----|---|-----|---|-----|---|-----|
| 1 | b | 32 | a | 63 | a | 94 | b | 125 | b |
| 2 | b | 33 | b | 64 | b | 95 | b | 126 | a |
| 3 | b | 34 | a | 65 | b | 96 | d | 127 | a |
| 4 | c | 35 | b | 66 | c | 97 | b | 128 | b |
| 5 | c | 36 | b | 67 | b | 98 | a | 129 | b |
| 6 | b | 37 | a | 68 | a | 99 | b | 130 | b |
| 7 | a | 38 | a | 69 | b | 100 | b | 131 | a |
| 8 | b | 39 | b | 70 | b | 101 | b | 132 | b |
| 9 | a | 40 | b | 71 | b | 102 | b | 133 | a |
| 10 | b | 41 | a | 72 | b | 103 | c | 134 | b |
| 11 | a | 42 | c | 73 | b | 104 | b | 135 | a |
| 12 | c | 43 | c | 74 | a | 105 | b | 136 | d |
| 13 | c | 44 | a | 75 | b | 106 | a | 137 | c |
| 14 | b | 45 | b | 76 | b | 107 | b | 138 | a |
| 15 | b | 46 | b | 77 | d | 108 | b | 139 | c |
| 16 | b | 47 | b | 78 | b | 109 | c | 140 | c |
| 17 | c | 48 | b | 79 | a | 110 | a | 141 | b |
| 18 | a | 49 | a | 80 | b | 111 | c | 142 | b |
| 19 | b | 50 | c | 81 | b | 112 | a | 143 | a |
| 20 | b | 51 | b | 82 | a | 113 | a | 144 | c |
| 21 | a | 52 | b | 83 | a | 114 | a | 145 | b |
| 22 | b | 53 | b | 84 | b | 115 | b | 146 | c |
| 23 | b | 54 | a | 85 | b | 116 | b | 147 | b |
| 24 | b | 55 | c | 86 | b | 117 | c | 148 | a |
| 25 | b | 56 | d | 87 | b | 118 | b | 149 | b |
| 26 | a | 57 | b | 88 | b | 119 | b | 150 | b |
| 27 | b | 58 | c | 89 | d | 120 | c | 151 | a |
| 28 | b | 59 | b | 90 | b | 121 | b | 152 | b |
| 29 | b | 60 | b | 91 | a | 122 | a | 153 | c |
| 30 | b | 61 | a | 92 | b | 123 | a | 154 | a |
| 31 | a | 62 | b | 93 | c | 124 | a | 155 | a |
