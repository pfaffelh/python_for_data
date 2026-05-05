# Exam: Python Basics (Chapters 2–7) — 212 Questions

**Duration:** 150 minutes.
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

**20.** What does `round(3.14159, 2)` return?

- (a) `3.14`
- (b) `3.15`
- (c) `3.1`
- (d) `3`

**21.** What is `0.1 + 0.2 == 0.3` in Python?

- (a) `True`
- (b) `False`
- (c) Error
- (d) `None`

**22.** What does `type(3 == 3)` return?

- (a) `<class 'int'>`
- (b) `<class 'bool'>`
- (c) `<class 'str'>`
- (d) `<class 'NoneType'>`

**23.** What is the value of `True + True + False`?

- (a) `2`
- (b) `True`
- (c) `3`
- (d) Error

**24.** What does `bool(0)` return?

- (a) `True`
- (b) `False`
- (c) `0`
- (d) Error

**25.** What does `bool("")` return?

- (a) `True`
- (b) `False`
- (c) `""`
- (d) Error

**27.** What does `bool([])` return?

- (a) `True`
- (b) `False`
- (c) `[]`
- (d) Error

**28.** Which expression evaluates to `True`?

- (a) `1 == "1"`
- (b) `1 == 1.0`
- (c) `"1" == 1.0`
- (d) `None == 0`

**29.** What is the value of `"Python"[0]`?

- (a) `"P"`
- (b) `"y"`
- (c) `0`
- (d) Error

**30.** What is the value of `"Python"[-1]`?

- (a) `"P"`
- (b) `"n"`
- (c) `"y"`
- (d) Error

**31.** What is the value of `"Python"[1:4]`?

- (a) `"Pyt"`
- (b) `"yth"`
- (c) `"ytho"`
- (d) `"Pyth"`

**33.** What does `len("Python")` return?

- (a) `5`
- (b) `6`
- (c) `7`
- (d) Error

**34.** What does `"hello".upper()` return?

- (a) `"hello"`
- (b) `"HELLO"`
- (c) `"Hello"`
- (d) Error

**35.** What does `"HELLO".lower()` return?

- (a) `"hello"`
- (b) `"HELLO"`
- (c) `"Hello"`
- (d) Error

**36.** What does `"  hello  ".strip()` return?

- (a) `"hello"`
- (b) `"  hello  "`
- (c) `"hello  "`
- (d) `"  hello"`

**37.** What does `"a,b,c".split(",")` return?

- (a) `"a b c"`
- (b) `["a", "b", "c"]`
- (c) `("a", "b", "c")`
- (d) `"abc"`

**38.** What does `",".join(["a", "b", "c"])` return?

- (a) `"a,b,c"`
- (b) `["a,b,c"]`
- (c) `"a, b, c"`
- (d) Error

**39.** What does `"Python".replace("P", "J")` return?

- (a) `"Python"`
- (b) `"Jython"`
- (c) `"Pjthon"`
- (d) Error

**41.** What does `"Python".endswith("py")` return?

- (a) `True`
- (b) `False`
- (c) `"py"`
- (d) Error

**42.** What does `"abc".isalpha()` return?

- (a) `True`
- (b) `False`
- (c) `"abc"`
- (d) Error

**43.** What does `"123".isdigit()` return?

- (a) `True`
- (b) `False`
- (c) `123`
- (d) Error

**44.** What does `str(42)` return?

- (a) `42`
- (b) `"42"`
- (c) `"'42'"`
- (d) Error

**45.** What does `int("42")` return?

- (a) `"42"`
- (b) `42`
- (c) `42.0`
- (d) Error

**46.** What does `float("3.14")` return?

- (a) `3.14`
- (b) `"3.14"`
- (c) `3`
- (d) Error

**49.** Which character can start a valid Python variable name?

- (a) A digit
- (b) A space
- (c) A letter or underscore
- (d) A hyphen

**50.** Which of the following is NOT a valid Python variable name?

- (a) `my_var`
- (b) `_x`
- (c) `2nd_value`
- (d) `value2`

**51.** What does `type(5)` return?

- (a) `<class 'int'>`
- (b) `<class 'float'>`
- (c) `<class 'number'>`
- (d) `5`

**52.** What is the result of `not True`?

- (a) `True`
- (b) `False`
- (c) `0`
- (d) Error

**54.** How many bits does a standard Python `float` use internally?

- (a) 32
- (b) 64
- (c) 128
- (d) Unlimited

**55.** In a float, which part stores the precision of the number?

- (a) the exponent
- (b) the mantissa
- (c) the sign bit
- (d) the base

---

## Chapter 3 — Control flow: conditions, loops, functions

**56.** What does `range(5)` represent?

- (a) The numbers `1, 2, 3, 4, 5`
- (b) The numbers `0, 1, 2, 3, 4`
- (c) The numbers `0, 1, 2, 3, 4, 5`
- (d) A single integer `5`

**57.** What does `list(range(1, 10, 3))` evaluate to?

- (a) `[1, 4, 7]`
- (b) `[1, 4, 7, 10]`
- (c) `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- (d) `[3, 6, 9]`

**58.** Which keyword immediately stops the execution of a `for`-loop?

- (a) `continue`
- (b) `stop`
- (c) `break`
- (d) `return`

**59.** What is printed by the following code?

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

**60.** Consider the function

```python
def greeting(name, prefix="Hello"):
    print(f"{prefix}, {name}!")
```

Which call prints `Hi, Bob!`?

- (a) `greeting("Hi", "Bob")`
- (b) `greeting(name="Bob", prefix="Hi")`
- (c) `greeting("Bob")`
- (d) `greeting(prefix="Bob", name="Hi")`

**61.** What is a **docstring**?

- (a) A comment starting with `#`.
- (b) A multiline string placed right after the `def`-line, describing what the function does.
- (c) A special `print` statement inside a function.
- (d) A file with `.doc` extension containing documentation.

**62.** Which of the following defines a valid `lambda`-function that squares its argument?

- (a) `lambda x: x ** 2`
- (b) `lambda(x) = x ** 2`
- (c) `def lambda x: x*x`
- (d) `lambda x -> x ** 2`

**63.** Which exception is raised by `int("abc")`?

- (a) `TypeError`
- (b) `NameError`
- (c) `ValueError`
- (d) `SyntaxError`

**64.** Which exception is raised by `1 / 0`?

- (a) `ValueError`
- (b) `ArithmeticError`
- (c) `TypeError`
- (d) `ZeroDivisionError`

**65.** What is the purpose of the `with` statement when opening a file?

- (a) To speed up reading.
- (b) To automatically close the file when the block ends.
- (c) To open the file in read-only mode.
- (d) To encrypt the file.

**66.** Which mode opens a file for appending text at the end?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"x"`

**67.** What is the output of the following code?

```python
res = 5 if 2 > 3 else 10
print(res)
```

- (a) `5`
- (b) `10`
- (c) `True`
- (d) Error

**68.** Inside a function, a variable is assigned a value. After the function returns, what happens to that variable (assuming no `global` or `return`)?

- (a) It keeps its new value outside the function.
- (b) It is deleted and no longer accessible outside.
- (c) It causes an error.
- (d) It overwrites any outer variable of the same name.

**69.** What is the output of `list(range(5, 0, -1))`?

- (a) `[5, 4, 3, 2, 1]`
- (b) `[5, 4, 3, 2, 1, 0]`
- (c) `[4, 3, 2, 1, 0]`
- (d) `[1, 2, 3, 4, 5]`

**70.** What is the output of `list(range(3, 3))`?

- (a) `[3]`
- (b) `[]`
- (c) `[3, 3]`
- (d) Error

**71.** What does the following code print?

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

**73.** What does `continue` do inside a loop?

- (a) Exits the loop.
- (b) Skips the remainder of the current iteration and moves to the next.
- (c) Pauses execution.
- (d) Raises an exception.

**74.** What does the following code print?

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

**75.** A function without a `return` statement implicitly returns:

- (a) `0`
- (b) `False`
- (c) `None`
- (d) An empty string

**76.** Consider the code:

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

**80.** What is the output of the following code?

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

**81.** What is a recursive function?

- (a) A function that returns multiple values.
- (b) A function that calls itself.
- (c) A function without parameters.
- (d) A built-in function.

**83.** What is `list(filter(lambda x: x > 2, [1, 2, 3, 4]))`?

- (a) `[1, 2]`
- (b) `[3, 4]`
- (c) `[2, 3, 4]`
- (d) `[True, True]`

**84.** What does `sorted([3, 1, 2], key=lambda x: -x)` return?

- (a) `[1, 2, 3]`
- (b) `[3, 2, 1]`
- (c) `[-3, -2, -1]`
- (d) `[-1, -2, -3]`

**87.** Which statement raises a custom exception?

- (a) `throw ValueError("bad")`
- (b) `raise ValueError("bad")`
- (c) `error ValueError("bad")`
- (d) `except ValueError("bad")`

**88.** Which exception is raised by `[1, 2, 3][10]`?

- (a) `KeyError`
- (b) `IndexError`
- (c) `ValueError`
- (d) `TypeError`

**89.** Which exception is raised by `{"a": 1}["b"]`?

- (a) `KeyError`
- (b) `IndexError`
- (c) `ValueError`
- (d) `AttributeError`

**90.** Which exception is raised when a file cannot be found?

- (a) `IOError`
- (b) `FileNotFoundError`
- (c) `ValueError`
- (d) `NameError`

**91.** Which file mode truncates the file if it already exists?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"r+"`

**92.** Which file mode fails if the file already exists?

- (a) `"r"`
- (b) `"w"`
- (c) `"a"`
- (d) `"x"`

**93.** What does `f.readlines()` return when called on a file object `f`?

- (a) A single string.
- (b) A list of strings, one per line.
- (c) A generator.
- (d) The number of lines.

**97.** What is the output of the following code?

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

**98.** Which keyword is used to define a function in Python?

- (a) `function`
- (b) `def`
- (c) `func`
- (d) `lambda`

**101.** What does `match`/`case` in Python (3.10+) implement?

- (a) A regex matcher.
- (b) Structural pattern matching (similar to switch-case).
- (c) A new loop construct.
- (d) A type annotation.

**103.** What is the output of the following code?

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

**104.** What is the value of `sum([1, 2, 3, 4])`?

- (a) `10`
- (b) `[1, 2, 3, 4]`
- (c) `6`
- (d) Error

**105.** What happens when a `while True:` loop has no `break`?

- (a) It runs once.
- (b) It runs forever (infinite loop).
- (c) It raises an error.
- (d) It runs until Python is restarted automatically.

**108.** Which statement is required to exit a function and return a value?

- (a) `exit`
- (b) `return`
- (c) `break`
- (d) `stop`

**109.** What is the output of:

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

**111.** Given `a = [10, 20, 30, 40, 50]`, what is `a[1:4]`?

- (a) `[10, 20, 30]`
- (b) `[20, 30, 40]`
- (c) `[20, 30, 40, 50]`
- (d) `[10, 20, 30, 40]`

**112.** Given `a = [10, 20, 30, 40]`, what is `a[-1]`?

- (a) `10`
- (b) `40`
- (c) `-1`
- (d) Error

**113.** Which of the following is **immutable**?

- (a) `list`
- (b) `dict`
- (c) `set`
- (d) `tuple`

**114.** What is the type of `(5)` in Python?

- (a) `tuple`
- (b) `int`
- (c) `list`
- (d) `set`

**115.** What is `len({1, 2, 2, 3, 3, 3})`?

- (a) `3`
- (b) `6`
- (c) `1`
- (d) Error: sets cannot contain duplicates.

**116.** Given `s = {1, 2, 3}` and `t = {3, 4, 5}`, what is `s & t`?

- (a) `{1, 2, 3, 4, 5}`
- (b) `{3}`
- (c) `{1, 2}`
- (d) `set()`

**117.** Given `l = [3, 1, 2]`, what does `print(l.sort())` print?

- (a) `[1, 2, 3]`
- (b) `[3, 2, 1]`
- (c) `None`
- (d) `[3, 1, 2]`

**118.** Which expression returns a new sorted list without changing the original list `l`?

- (a) `l.sort()`
- (b) `sorted(l)`
- (c) `l.sorted()`
- (d) `sort(l)`

**119.** Given `d = {"a": 1, "b": 2}`, what does `d.get("c", 0)` return?

- (a) `None`
- (b) `0`
- (c) An error
- (d) `"c"`

**120.** Which of the following cannot be used as a dictionary key?

- (a) `"name"`
- (b) `42`
- (c) `(1, 2)`
- (d) `[1, 2]`

**121.** What does the following code print?

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

**122.** What does `[x*x for x in range(4)]` evaluate to?

- (a) `[0, 1, 4, 9]`
- (b) `[1, 4, 9, 16]`
- (c) `[0, 2, 4, 6]`
- (d) `[0, 1, 2, 3]`

**123.** What does `[x for x in range(10) if x % 2 == 0]` evaluate to?

- (a) `[1, 3, 5, 7, 9]`
- (b) `[0, 2, 4, 6, 8]`
- (c) `[0, 2, 4, 6, 8, 10]`
- (d) `[2, 4, 6, 8]`

**124.** Given `l = [True, True, False]`, what does `all(l)` return?

- (a) `True`
- (b) `False`
- (c) `2`
- (d) `None`

**125.** What does `enumerate(["a", "b", "c"])` produce when iterated over?

- (a) `"a", "b", "c"`
- (b) `(0, "a"), (1, "b"), (2, "c")`
- (c) `(1, "a"), (2, "b"), (3, "c")`
- (d) `("a", 0), ("b", 1), ("c", 2)`

**126.** What does the following code print?

```python
l = [1, 2, 3]
l.append([4, 5])
print(len(l))
```

- (a) `3`
- (b) `4`
- (c) `5`
- (d) Error

**127.** What does the following code print?

```python
l = [1, 2, 3]
l.extend([4, 5])
print(len(l))
```

- (a) `3`
- (b) `4`
- (c) `5`
- (d) Error

**128.** What is the difference between `l.append(x)` and `l.extend(x)`?

- (a) They are identical.
- (b) `append` adds `x` as a single element; `extend` adds each element of `x`.
- (c) `extend` adds `x` as a single element; `append` adds each element of `x`.
- (d) Only `extend` modifies the original list.

**129.** Given `l = [1, 2, 3]`, what is `l.pop()`?

- (a) `1`
- (b) `3`
- (c) `[1, 2]`
- (d) `None`

**130.** Given `l = [10, 20, 30]`, what is `l.pop(0)`?

- (a) `10`
- (b) `30`
- (c) `[20, 30]`
- (d) `None`

**131.** Given `l = [1, 2, 3, 2]`, what does `l.remove(2)` do?

- (a) Removes all `2`s.
- (b) Removes the first `2`.
- (c) Removes the last `2`.
- (d) Returns a new list.

**132.** Given `l = [1, 2, 3]`, what is `l.index(2)`?

- (a) `0`
- (b) `1`
- (c) `2`
- (d) `3`

**133.** Given `l = [1, 2, 2, 3, 2]`, what is `l.count(2)`?

- (a) `1`
- (b) `2`
- (c) `3`
- (d) `4`

**134.** What does the following code print?

```python
l = [1, 2, 3]
l.insert(1, 99)
print(l)
```

- (a) `[1, 99, 2, 3]`
- (b) `[99, 1, 2, 3]`
- (c) `[1, 2, 3, 99]`
- (d) `[1, 2, 99, 3]`

**135.** Given `l = [1, 2, 3]`, what does `l.reverse()` return?

- (a) `[3, 2, 1]`
- (b) `[1, 2, 3]`
- (c) `None`
- (d) A new list

**136.** What is the value of `[1, 2] + [3, 4]`?

- (a) `[1, 2, 3, 4]`
- (b) `[4, 6]`
- (c) `[[1, 2], [3, 4]]`
- (d) Error

**138.** What is `"hello"[::2]`?

- (a) `"hlo"`
- (b) `"hello"`
- (c) `"el"`
- (d) `"olleh"`

**140.** What does `3 in [1, 2, 3]` return?

- (a) `True`
- (b) `False`
- (c) `3`
- (d) Error

**141.** Given the assignment `a, b = (1, 2)`, what is `b`?

- (a) `1`
- (b) `2`
- (c) `(1, 2)`
- (d) Error

**142.** What does the assignment `a, b = b, a` do?

- (a) Sets `a` and `b` both to `None`.
- (b) Swaps the values of `a` and `b`.
- (c) Raises a syntax error.
- (d) Creates a tuple `(a, b)`.

**143.** Which of the following creates a tuple with a single element `5`?

- (a) `(5)`
- (b) `[5]`
- (c) `(5,)`
- (d) `{5}`

**144.** What is `()` in Python?

- (a) An empty list
- (b) An empty tuple
- (c) An empty set
- (d) `None`

**145.** What is `{}` in Python?

- (a) An empty set
- (b) An empty dictionary
- (c) An empty list
- (d) `None`

**146.** How can you create an empty set in Python?

- (a) `{}`
- (b) `[]`
- (c) `set()`
- (d) `empty_set()`

**147.** Given `s = {1, 2, 3}` and `t = {3, 4}`, what is `s | t`?

- (a) `{3}`
- (b) `{1, 2, 3, 4}`
- (c) `{1, 2}`
- (d) `set()`

**148.** Given `s = {1, 2, 3}` and `t = {3, 4}`, what is `s - t`?

- (a) `{1, 2}`
- (b) `{3}`
- (c) `{4}`
- (d) `set()`

**153.** Given `d = {"a": 1, "b": 2}`, what does `d["a"]` return?

- (a) `1`
- (b) `"a"`
- (c) `("a", 1)`
- (d) Error

**154.** Given `d = {"a": 1, "b": 2}`, what does `list(d.keys())` return?

- (a) `["a", "b"]`
- (b) `[1, 2]`
- (c) `[("a", 1), ("b", 2)]`
- (d) `[]`

**155.** Given `d = {"a": 1, "b": 2}`, what does `list(d.values())` return?

- (a) `["a", "b"]`
- (b) `[1, 2]`
- (c) `[("a", 1), ("b", 2)]`
- (d) `[]`

**156.** Given `d = {"a": 1, "b": 2}`, what does `list(d.items())` return?

- (a) `[("a", 1), ("b", 2)]`
- (b) `["a", 1, "b", 2]`
- (c) `[{"a": 1}, {"b": 2}]`
- (d) `[]`

**157.** What is `{x: x**2 for x in range(4)}`?

- (a) `{0: 0, 1: 1, 2: 4, 3: 9}`
- (b) `[0, 1, 4, 9]`
- (c) `{0, 1, 4, 9}`
- (d) Error

**159.** What does `d.update({"c": 3})` do to the dictionary `d`?

- (a) Replaces `d` entirely with `{"c": 3}`.
- (b) Adds or updates the key `"c"` in `d`.
- (c) Returns a new dictionary.
- (d) Raises an error.

**160.** What does `del d["a"]` do?

- (a) Deletes the value `"a"` from any key in `d`.
- (b) Removes the key `"a"` (and its value) from `d`.
- (c) Sets `d["a"]` to `None`.
- (d) Deletes the dictionary `d`.

**162.** What does `any([False, 0, None, ""])` return?

- (a) `True`
- (b) `False`
- (c) `None`
- (d) Error

**164.** What does `min([3, 1, 2, 5])` return?

- (a) `1`
- (b) `3`
- (c) `5`
- (d) `2`

**166.** What does `sorted(["banana", "pie", "apple"], key=len)` return?

- (a) `["apple", "banana", "pie"]`
- (b) `["pie", "apple", "banana"]`
- (c) `["banana", "apple", "pie"]`
- (d) `["apple", "pie", "banana"]`

**180.** What does the following code print?

```python
d = {"a": [1, 2], "b": [3, 4]}
for k, v in d.items():
    print(k, sum(v))
```

- (a) `a 3` then `b 7`
- (b) `a [1, 2]` then `b [3, 4]`
- (c) `1 2` then `3 4`
- (d) Error

**181.** Given `t = (1, 2, 3)`, what does `t[0] = 10` do?

- (a) Changes the first element to `10`.
- (b) Raises `TypeError`: tuples are immutable.
- (c) Creates a new tuple.
- (d) Does nothing.

**184.** What does `set([1, 2, 2, 3])` return?

- (a) `{1, 2, 3}`
- (b) `[1, 2, 3]`
- (c) `(1, 2, 3)`
- (d) Error

**185.** Which expression gets every second element of a list `l`?

- (a) `l[0::2]`
- (b) `l[1::2]`
- (c) `l[::2]`
- (d) Both (a) and (c)

**186.** Given `matrix = [[1, 2], [3, 4], [5, 6]]`, what is `matrix[1][0]`?

- (a) `1`
- (b) `2`
- (c) `3`
- (d) `4`

**188.** What does `"".join(["a", "b", "c"])` return?

- (a) `"abc"`
- (b) `"a, b, c"`
- (c) `["abc"]`
- (d) `["a", "b", "c"]`

**191.** Suppose `one.py` contains a function `myConst()`. In `two.py`, which import statement lets you call it as `myConst()` (without a prefix)?

- (a) `import one`
- (b) `import one as myConst`
- (c) `from one import myConst`
- (d) `import myConst from one`

**192.** Which import gives you access to `math.pi`?

- (a) `import pi`
- (b) `from math import *` only
- (c) `import math`
- (d) `include math`

**193.** You have a string `"21.4.26, 12:15"` and want to convert it into a `datetime` object. Which function do you use?

- (a) `datetime.datetime.strftime`
- (b) `datetime.datetime.strptime`
- (c) `datetime.parse`
- (d) `datetime.convert`

**194.** Given a `datetime` object `dt`, how do you get the date exactly 7 days later?

- (a) `dt + 7`
- (b) `dt + datetime.timedelta(days=7)`
- (c) `dt.add(7)`
- (d) `dt + datetime.date(7)`

**195.** Why does `Decimal('0.1') + Decimal('0.2')` give an exact result, but `0.1 + 0.2` does not?

- (a) `Decimal` uses a base-10 representation, while `float` uses base 2.
- (b) `Decimal` is faster than `float`.
- (c) `float` is deprecated in recent Python versions.
- (d) They both give the same exact result.

**196.** Which library is used to find patterns like email addresses in a string?

- (a) `os`
- (b) `pickle`
- (c) `re`
- (d) `math`

**197.** What is the purpose of the `pickle` library?

- (a) Handling dates and times.
- (b) Serializing Python objects to a file and loading them back.
- (c) Running tests.
- (d) Finding patterns in strings.

**198.** What does `assert 2 + 2 == 5` do when executed?

- (a) Nothing; the line is silently ignored.
- (b) It prints `False`.
- (c) It raises an `AssertionError`.
- (d) It returns `False`.

**199.** What does `math.sqrt(16)` return?

- (a) `4`
- (b) `4.0`
- (c) `16`
- (d) Error

**202.** What is the approximate value of `math.e`?

- (a) `2.718`
- (b) `3.141`
- (c) `1.618`
- (d) `1.414`

**203.** What does `math.log(math.e)` return?

- (a) `0`
- (b) `1.0`
- (c) `2.718`
- (d) Error

**204.** What does `math.sin(math.pi / 2)` return?

- (a) `0.0`
- (b) `1.0`
- (c) `-1.0`
- (d) `math.pi / 2`

**211.** Given `dt = datetime.datetime(2026, 3, 27, 12, 0)`, what does `dt.strftime("%Y-%m-%d")` return?

- (a) `"2026-03-27"`
- (b) `"27-03-2026"`
- (c) `"2026/03/27"`
- (d) `"%Y-%m-%d"`

**212.** Given two `datetime` objects `a` and `b`, what is the type of `a - b`?

- (a) `datetime`
- (b) `timedelta`
- (c) `int`
- (d) `float`

**214.** Which of the following is a regex module function that finds ALL non-overlapping matches?

- (a) `re.match`
- (b) `re.search`
- (c) `re.findall`
- (d) `re.split`

**219.** Which module provides operating-system-level functionality like listing directory contents?

- (a) `os`
- (b) `sys`
- (c) `io`
- (d) `pathlib`

**221.** What does `pickle.dump(obj, f)` do?

- (a) Writes `obj` to the open binary file `f`.
- (b) Prints `obj`.
- (c) Returns `obj` as a string.
- (d) Reads `obj` from `f`.

---

## Chapter 6 — Numerics (numpy)

**222.** How do you create a 1D numpy array from the list `[1, 2, 3]`?

- (a) `np.array([1, 2, 3])`
- (b) `np.list([1, 2, 3])`
- (c) `np.vector([1, 2, 3])`
- (d) `numpy([1, 2, 3])`

**223.** What does `np.arange(0, 10, 2)` return?

- (a) `array([0, 2, 4, 6, 8])`
- (b) `array([0, 2, 4, 6, 8, 10])`
- (c) `array([2, 4, 6, 8, 10])`
- (d) `array([0, 1, 2, ..., 10])`

**224.** What does `np.linspace(0, 1, 5)` return?

- (a) `array([0., 0.25, 0.5, 0.75, 1.])`
- (b) `array([0., 0.2, 0.4, 0.6, 0.8])`
- (c) `array([0, 1, 2, 3, 4])`
- (d) Error

**225.** What does `np.zeros(3)` return?

- (a) `array([0., 0., 0.])`
- (b) `array([0, 1, 2])`
- (c) `array([0])`
- (d) `0`

**226.** What does `np.ones((2, 3))` return?

- (a) A 2×3 array filled with `1.`
- (b) A 3×2 array filled with `1.`
- (c) A 1D array of length 5
- (d) Error

**227.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a.shape`?

- (a) `(2, 3)`
- (b) `(3, 2)`
- (c) `(6,)`
- (d) `6`

**228.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a.size`?

- (a) `2`
- (b) `3`
- (c) `6`
- (d) `(2, 3)`

**229.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a.ndim`?

- (a) `1`
- (b) `2`
- (c) `3`
- (d) `6`

**230.** What is the default `dtype` of `np.array([1, 2, 3])`?

- (a) An integer type (e.g. `int64`)
- (b) `float64`
- (c) `object`
- (d) `str`

**231.** What does `np.array([1, 2, 3]) + np.array([10, 20, 30])` return?

- (a) `array([11, 22, 33])`
- (b) `array([1, 2, 3, 10, 20, 30])`
- (c) `66`
- (d) Error

**232.** What does `np.array([1, 2, 3]) * 2` return?

- (a) `array([2, 4, 6])`
- (b) `array([1, 2, 3, 1, 2, 3])`
- (c) `6`
- (d) Error

**233.** What does `np.array([[1, 2], [3, 4]]) * np.array([[2, 0], [1, 3]])` return?

- (a) `array([[2, 0], [3, 12]])` (element-wise)
- (b) `array([[4, 6], [10, 12]])` (matrix product)
- (c) A scalar
- (d) Error

**234.** What does `A @ B` compute for numpy 2D arrays `A` and `B` of compatible shapes?

- (a) Element-wise product
- (b) Matrix product
- (c) Outer product
- (d) Concatenation

**235.** Given `a = np.arange(10)`, what is `a[2:6]`?

- (a) `array([2, 3, 4, 5])`
- (b) `array([2, 3, 4, 5, 6])`
- (c) `array([0, 1, 2, 3, 4, 5])`
- (d) Error

**236.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a[1, 2]`?

- (a) `3`
- (b) `6`
- (c) `5`
- (d) `4`

**237.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a[:, 1]`?

- (a) `array([2, 5])`
- (b) `array([4, 5, 6])`
- (c) `array([1, 2, 3])`
- (d) Error

**238.** Given `a = np.array([1, 2, 3, 4, 5])`, what is `a[a > 2]`?

- (a) `array([3, 4, 5])`
- (b) `array([True, True, True])`
- (c) `array([1, 2])`
- (d) Error

**239.** Given `a = np.arange(12)`, what is `a.reshape(3, 4).shape`?

- (a) `(3, 4)`
- (b) `(4, 3)`
- (c) `(12,)`
- (d) Error

**240.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a.sum()`?

- (a) `21`
- (b) `array([5, 7, 9])`
- (c) `array([6, 15])`
- (d) Error

**241.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a.sum(axis=0)`?

- (a) `array([5, 7, 9])`
- (b) `array([6, 15])`
- (c) `21`
- (d) Error

**242.** Given `a = np.array([[1, 2, 3], [4, 5, 6]])`, what is `a.sum(axis=1)`?

- (a) `array([5, 7, 9])`
- (b) `array([6, 15])`
- (c) `21`
- (d) Error

**243.** What does `np.mean([1, 2, 3, 4])` return?

- (a) `2.5`
- (b) `10`
- (c) `2`
- (d) `1`

**244.** What does **broadcasting** refer to in numpy?

- (a) Sending arrays over a network.
- (b) Automatically expanding array shapes in element-wise operations.
- (c) Printing arrays.
- (d) Reshaping arrays manually.

**245.** What is the shape of the result of `np.array([[1, 2, 3]]) + np.array([[10], [20]])`?

- (a) `(1, 3)`
- (b) `(2, 1)`
- (c) `(2, 3)`
- (d) Error

**246.** Given `a = np.array([3, 1, 4, 1, 5, 9])`, what is `a.max()`?

- (a) `9`
- (b) `5`
- (c) `1`
- (d) `3`

**248.** How do you generate 5 random numbers uniformly distributed in `[0, 1)`?

- (a) `np.random.random(5)`
- (b) `random.random(5)`
- (c) `np.random(5)`
- (d) `np.rand(5)`

**249.** How do you create a reproducible random-number generator with seed `42`?

- (a) `np.random.default_rng(42)`
- (b) `np.random(42)`
- (c) `np.seed(42)`
- (d) `np.random.generator()`

**250.** What does `np.linalg.inv(A)` compute for a square numpy matrix `A`?

- (a) The inverse of `A`.
- (b) The transpose of `A`.
- (c) The determinant of `A`.
- (d) The eigenvalues of `A`.

**251.** What does `A.T` do for a numpy 2D array `A`?

- (a) Transposes `A`.
- (b) Inverts `A`.
- (c) Returns `True` or `False`.
- (d) Raises an error.

---

## Chapter 7 — Handling data (pandas)

**252.** How do you create a pandas DataFrame from a dictionary?

- (a) `pd.DataFrame({"a": [1, 2], "b": [3, 4]})`
- (b) `pd.Frame({"a": [1, 2], "b": [3, 4]})`
- (c) `DataFrame.from({"a": [1, 2], "b": [3, 4]})`
- (d) `pandas.Dict({"a": [1, 2], "b": [3, 4]})`

**253.** What is a `pd.Series`?

- (a) A 1D labeled array.
- (b) A 2D table.
- (c) A Python list.
- (d) A dictionary.

**254.** How do you access the column `"age"` of a DataFrame `df`?

- (a) `df["age"]`
- (b) `df("age")`
- (c) `df.get_column("age")`
- (d) `df.col("age")`

**255.** What does `df.head(3)` return?

- (a) The first 3 rows of `df`.
- (b) The last 3 rows.
- (c) The first 3 columns.
- (d) Error

**256.** What does `df.tail(5)` return?

- (a) The last 5 rows.
- (b) The first 5 rows.
- (c) The 5 largest rows.
- (d) Error

**257.** What does `df.shape` return?

- (a) A tuple `(n_rows, n_columns)`.
- (b) The number of rows only.
- (c) The number of columns only.
- (d) Error

**258.** What does `df.describe()` return?

- (a) Summary statistics (count, mean, std, min, quartiles, max) for numeric columns.
- (b) The first 5 rows.
- (c) Only means.
- (d) Column data types.

**260.** How do you select rows of `df` where column `age` is greater than 30?

- (a) `df[df["age"] > 30]`
- (b) `df.where(age > 30)`
- (c) `df.select("age > 30")`
- (d) `df.filter(age > 30)`

**261.** How do you select the row with index label `"Alice"`?

- (a) `df.loc["Alice"]`
- (b) `df.iloc["Alice"]`
- (c) `df["Alice"]`
- (d) `df.row("Alice")`

**262.** How do you select the row at integer position `3`?

- (a) `df.loc[3]`
- (b) `df.iloc[3]`
- (c) `df[3]`
- (d) `df.row(3)`

**263.** What is the difference between `.loc` and `.iloc`?

- (a) `.loc` uses labels; `.iloc` uses integer positions.
- (b) `.iloc` uses labels; `.loc` uses integer positions.
- (c) They are identical.
- (d) `.loc` is deprecated.

**264.** How do you compute the mean of each numeric column in `df`?

- (a) `df.mean()`
- (b) `df.mean(axis=1)`
- (c) `mean(df)`
- (d) `df.average()`

**265.** How do you load a CSV file into a DataFrame?

- (a) `pd.read_csv("file.csv")`
- (b) `pd.load_csv("file.csv")`
- (c) `pd.DataFrame.csv("file.csv")`
- (d) `open_csv("file.csv")`

**266.** How do you save a DataFrame to a CSV file?

- (a) `df.to_csv("file.csv")`
- (b) `df.save("file.csv")`
- (c) `pd.write_csv(df, "file.csv")`
- (d) `df.csv("file.csv")`

**267.** Which method counts the occurrences of each unique value in a Series `s`?

- (a) `s.value_counts()`
- (b) `s.count()`
- (c) `s.unique()`
- (d) `s.frequency()`

**268.** What does `df["col"].unique()` return?

- (a) An array of the unique values in `col`.
- (b) The number of unique values.
- (c) A sorted array.
- (d) Error

**269.** What does `df["col"].nunique()` return?

- (a) The number of unique values.
- (b) An array of unique values.
- (c) The most common value.
- (d) Error

**270.** How do you check for missing values in a DataFrame?

- (a) `df.isna()`
- (b) `df.missing()`
- (c) `df == NaN`
- (d) `df.null()`

**271.** How do you drop rows with any missing values?

- (a) `df.dropna()`
- (b) `df.remove_na()`
- (c) `df.drop(na=True)`
- (d) `df.clean()`

**272.** How do you fill missing values with `0`?

- (a) `df.fillna(0)`
- (b) `df.replace_na(0)`
- (c) `df.na_fill(0)`
- (d) `df.fill(0)`

**273.** How do you group `df` by the column `"category"` and compute the mean of each group?

- (a) `df.groupby("category").mean()`
- (b) `df.group("category").mean()`
- (c) `df.by("category").mean()`
- (d) `df.mean("category")`

**274.** How do you sort `df` by column `"age"` in ascending order?

- (a) `df.sort_values("age")`
- (b) `df.sort("age")`
- (c) `df.order("age")`
- (d) `df.arrange("age")`

**276.** How do you rename a column from `"old"` to `"new"`?

- (a) `df.rename(columns={"old": "new"})`
- (b) `df.columns("old") = "new"`
- (c) `df.rename_col("old", "new")`
- (d) `df["old"].rename("new")`

**277.** How do you add a new column `c` that equals `df["a"] + df["b"]`?

- (a) `df["c"] = df["a"] + df["b"]`
- (b) `df.add_column("c", df["a"] + df["b"])`
- (c) `df.append("c", df["a"] + df["b"])`
- (d) `df.insert_col("c")`

**278.** How do you merge `df1` and `df2` on the column `"id"`?

- (a) `pd.merge(df1, df2, on="id")`
- (b) `df1.merge_with(df2)`
- (c) `df1 + df2`
- (d) `pd.join(df1, df2)`

**279.** How do you concatenate two DataFrames vertically (stacking rows)?

- (a) `pd.concat([df1, df2])`
- (b) `pd.merge(df1, df2)`
- (c) `df1 * df2`
- (d) `pd.stack(df1, df2)`

**280.** How do you convert a DataFrame column to a numpy array?

- (a) `df["col"].to_numpy()`
- (b) `np.from_pandas(df["col"])`
- (c) `np.convert(df["col"])`
- (d) `pd.numpy(df["col"])`

**281.** How do you convert a string column `"date"` to actual datetime values?

- (a) `pd.to_datetime(df["date"])`
- (b) `df["date"].to_date()`
- (c) `datetime(df["date"])`
- (d) `pd.datetime(df["date"])`

---

## Answer key

| #   | Ans | #   | Ans | #   | Ans | #   | Ans | #   | Ans |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|   1 | b   |  36 | a   |  71 | a   | 118 | b   | 155 | b   |
|   2 | b   |  37 | b   |  73 | b   | 119 | b   | 156 | a   |
|   3 | b   |  38 | a   |  74 | b   | 120 | d   | 157 | a   |
|   4 | c   |  39 | b   |  75 | c   | 121 | b   | 159 | b   |
|   5 | c   |  41 | b   |  76 | b   | 122 | a   | 160 | b   |
|   6 | b   |  42 | a   |  80 | a   | 123 | b   | 162 | b   |
|   7 | a   |  43 | a   |  81 | b   | 124 | b   | 164 | a   |
|   8 | b   |  44 | b   |  83 | b   | 125 | b   | 166 | b   |
|   9 | a   |  45 | b   |  84 | b   | 126 | b   | 180 | a   |
|  10 | b   |  46 | a   |  87 | b   | 127 | c   | 181 | b   |
|  11 | a   |  49 | c   |  88 | b   | 128 | b   | 184 | a   |
|  12 | c   |  50 | c   |  89 | a   | 129 | b   | 185 | d   |
|  13 | c   |  51 | a   |  90 | b   | 130 | a   | 186 | c   |
|  14 | b   |  52 | b   |  91 | b   | 131 | b   | 188 | a   |
|  15 | b   |  54 | b   |  92 | d   | 132 | b   | 191 | c   |
|  16 | b   |  55 | b   |  93 | b   | 133 | c   | 192 | c   |
|  17 | c   |  56 | b   |  97 | a   | 134 | a   | 193 | b   |
|  20 | a   |  57 | a   |  98 | b   | 135 | c   | 194 | b   |
|  21 | b   |  58 | c   | 101 | b   | 136 | a   | 195 | a   |
|  22 | b   |  59 | b   | 103 | a   | 138 | a   | 196 | c   |
|  23 | a   |  60 | b   | 104 | a   | 140 | a   | 197 | b   |
|  24 | b   |  61 | b   | 105 | b   | 141 | b   | 198 | c   |
|  25 | b   |  62 | a   | 108 | b   | 142 | b   | 199 | b   |
|  27 | b   |  63 | c   | 109 | b   | 143 | c   | 202 | a   |
|  28 | b   |  64 | d   | 111 | b   | 144 | b   | 203 | b   |
|  29 | a   |  65 | b   | 112 | b   | 145 | b   | 204 | b   |
|  30 | b   |  66 | c   | 113 | d   | 146 | c   | 211 | a   |
|  31 | b   |  67 | b   | 114 | b   | 147 | b   | 212 | b   |
|  33 | b   |  68 | b   | 115 | a   | 148 | a   | 214 | c   |
|  34 | b   |  69 | a   | 116 | b   | 153 | a   | 219 | a   |
|  35 | a   |  70 | b   | 117 | c   | 154 | a   | 221 | a   |

### Answers 222–281

| #   | Ans | #   | Ans | #   | Ans |
|-----|-----|-----|-----|-----|-----|
| 222 | a   | 241 | a   | 262 | b   |
| 223 | a   | 242 | b   | 263 | a   |
| 224 | a   | 243 | a   | 264 | a   |
| 225 | a   | 244 | b   | 265 | a   |
| 226 | a   | 245 | c   | 266 | a   |
| 227 | a   | 246 | a   | 267 | a   |
| 228 | c   | 248 | a   | 268 | a   |
| 229 | b   | 249 | a   | 269 | a   |
| 230 | a   | 250 | a   | 270 | a   |
| 231 | a   | 251 | a   | 271 | a   |
| 232 | a   | 252 | a   | 272 | a   |
| 233 | a   | 253 | a   | 273 | a   |
| 234 | b   | 254 | a   | 274 | a   |
| 235 | a   | 255 | a   | 276 | a   |
| 236 | b   | 256 | a   | 277 | a   |
| 237 | a   | 257 | a   | 278 | a   |
| 238 | a   | 258 | a   | 279 | a   |
| 239 | a   | 260 | a   | 280 | a   |
| 240 | a   | 261 | a   | 281 | a   |
