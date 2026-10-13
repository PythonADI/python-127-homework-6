# Exercises

Create these files inside your own folder:
`submissions/<your-github-username>/`.

Give every function you write a one-line docstring saying what it
returns or does.

## exercise_1.py — Drink order

Write a function `order(item, size="medium", sugar=0)` that prints one
line: `<item> (<size>), sugar: <sugar>`. Then call it exactly like this,
using positional and keyword arguments:

```python
order("tea")
order("coffee", sugar=2)
order(size="large", item="juice")
order("cocoa", "small", 1)
```

Expected output:
```
tea (medium), sugar: 0
coffee (medium), sugar: 2
juice (large), sugar: 0
cocoa (small), sugar: 1
```

## exercise_2.py — Fix the bug

This code should print `100.0` and `60.0` (50% off 200, 25% off 80),
but it prints `180.0` and `72.0`. Copy it into `exercise_2.py`, then
fix the function. Change only the line with the `BUG` comment.

```python
discount = 10

def apply_discount(price, percent):
    return price - price * discount / 100   # BUG: fix this line

print(apply_discount(200, 50))
print(apply_discount(80, 25))
```

Expected output:
```
100.0
60.0
```

## exercise_3.py — Minutes and seconds

Write a function `split_time(total_seconds)` that returns **two**
values: the whole minutes and the leftover seconds (hint: `//` and
`%`). Unpack the result in the caller:

```python
minutes, seconds = split_time(135)
print(f"{minutes} min {seconds} s")
minutes, seconds = split_time(59)
print(f"{minutes} min {seconds} s")
minutes, seconds = split_time(3600)
print(f"{minutes} min {seconds} s")
```

Expected output:
```
2 min 15 s
0 min 59 s
60 min 0 s
```

## exercise_4.py — Valid username

Write a yes/no function `is_valid_username(name)` that returns `True`
only if the name has **3 to 12 characters** and contains **no spaces**,
otherwise `False`. Return early: check the length first, then loop
over the characters and return `False` the moment you see a space.
Return the booleans — do not print inside the function. Then call it
like this:

```python
print(is_valid_username("nino"))
print(is_valid_username("ab"))
print(is_valid_username("giorgi kakhidze"))
print(is_valid_username("a b c"))
print(is_valid_username("luka_2024"))
```

Expected output:
```
True
False
False
False
True
```

## exercise_5.py — Bonus: ask until it is valid

Write a function `ask_number(low=1, high=10)` that keeps asking until
the user types a whole number from `low` to `high` (inclusive), and
then **returns** that number. Each time it asks, it first prints
`Enter a number from <low> to <high>:` on its own line and then calls
`input()` with **no prompt text** (so the output is unambiguous). If
the number is out of range, print `Out of range.` and ask again.
(You may assume the user always types a whole number.)

Then use it like this:

```python
first = ask_number()
second = ask_number(high=3)
print(f"You chose {first} and {second}")
```

Run it and type these five values, one per line, pressing Enter after
each: `15`, `0`, `7`, `5`, `2`.

Expected output, as it looks in the terminal (the lines `15`, `0`,
`7`, `5` and `2` are what you typed):
```
Enter a number from 1 to 10:
15
Out of range.
Enter a number from 1 to 10:
0
Out of range.
Enter a number from 1 to 10:
7
Enter a number from 1 to 3:
5
Out of range.
Enter a number from 1 to 3:
2
You chose 7 and 2
```
