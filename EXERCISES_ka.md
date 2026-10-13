# სავარჯიშოები

შექმენით ეს ფაილები თქვენს საკუთარ საქაღალდეში:
`submissions/<your-github-username>/`.

თითოეულ ფუნქციას, რომელსაც დაწერთ, დაუწერეთ ერთსტრიქონიანი docstring,
რომელიც ამბობს, რას აბრუნებს ან რას აკეთებს.

## exercise_1.py — სასმელის შეკვეთა

დაწერეთ ფუნქცია `order(item, size="medium", sugar=0)`, რომელიც ბეჭდავს
ერთ ხაზს: `<item> (<size>), sugar: <sugar>`. შემდეგ გამოიძახეთ ზუსტად ასე,
პოზიციური და საკვანძო (keyword) არგუმენტების გამოყენებით:

```python
order("tea")
order("coffee", sugar=2)
order(size="large", item="juice")
order("cocoa", "small", 1)
```

მოსალოდნელი შედეგი:
```
tea (medium), sugar: 0
coffee (medium), sugar: 2
juice (large), sugar: 0
cocoa (small), sugar: 1
```

## exercise_2.py — გაასწორეთ შეცდომა

ეს კოდი უნდა ბეჭდავდეს `100.0` და `60.0` (50% ფასდაკლება 200-ზე, 25%
ფასდაკლება 80-ზე), მაგრამ ბეჭდავს `180.0` და `72.0`. გადაწერეთ
`exercise_2.py`-ში და შეასწორეთ ფუნქცია. შეცვალეთ მხოლოდ ის ხაზი,
რომელზეც `BUG` კომენტარია.

```python
discount = 10

def apply_discount(price, percent):
    return price - price * discount / 100   # BUG: fix this line

print(apply_discount(200, 50))
print(apply_discount(80, 25))
```

მოსალოდნელი შედეგი:
```
100.0
60.0
```

## exercise_3.py — წუთები და წამები

დაწერეთ ფუნქცია `split_time(total_seconds)`, რომელიც აბრუნებს **ორ**
მნიშვნელობას: მთელ წუთებს და დარჩენილ წამებს (მინიშნება: `//` და
`%`). გამომძახებელში დაშალეთ შედეგი ორ ცვლადად:

```python
minutes, seconds = split_time(135)
print(f"{minutes} min {seconds} s")
minutes, seconds = split_time(59)
print(f"{minutes} min {seconds} s")
minutes, seconds = split_time(3600)
print(f"{minutes} min {seconds} s")
```

მოსალოდნელი შედეგი:
```
2 min 15 s
0 min 59 s
60 min 0 s
```

## exercise_4.py — სწორი username

დაწერეთ კი/არა ფუნქცია `is_valid_username(name)`, რომელიც აბრუნებს
`True`-ს მხოლოდ მაშინ, როცა სახელს აქვს **3-დან 12-მდე სიმბოლო** და
**არ შეიცავს ინტერვალს (space)**, სხვა შემთხვევაში `False`-ს. გამოიყენეთ
ადრეული დაბრუნება: ჯერ შეამოწმეთ სიგრძე, შემდეგ გადაუარეთ სიმბოლოებს
და დააბრუნეთ `False`, როგორც კი ინტერვალს ნახავთ. აბრუნეთ ბულეანი —
ფუნქციის შიგნით არ დაბეჭდოთ. შემდეგ გამოიძახეთ ასე:

```python
print(is_valid_username("nino"))
print(is_valid_username("ab"))
print(is_valid_username("giorgi kakhidze"))
print(is_valid_username("a b c"))
print(is_valid_username("luka_2024"))
```

მოსალოდნელი შედეგი:
```
True
False
False
False
True
```

## exercise_5.py — ბონუსი: ვკითხოთ, სანამ სწორი არ იქნება

დაწერეთ ფუნქცია `ask_number(low=1, high=10)`, რომელიც ხელახლა
კითხულობს, სანამ მომხმარებელი არ შეიყვანს მთელ რიცხვს `low`-დან
`high`-მდე (ჩათვლით), და შემდეგ ამ რიცხვს **აბრუნებს**. ყოველი
კითხვისას ჯერ დაბეჭდეთ ცალკე ხაზზე `Enter a number from <low> to
<high>:` და შემდეგ გამოიძახეთ `input()` **ტექსტის გარეშე** (რომ
შედეგი ცალსახა იყოს). თუ რიცხვი დიაპაზონს გარეთაა, დაბეჭდეთ
`Out of range.` და თავიდან ჰკითხეთ. (შეგიძლიათ ივარაუდოთ, რომ
მომხმარებელი ყოველთვის მთელ რიცხვს შეიყვანს.)

შემდეგ გამოიყენეთ ასე:

```python
first = ask_number()
second = ask_number(high=3)
print(f"You chose {first} and {second}")
```

გაუშვით და შეიყვანეთ ეს ხუთი მნიშვნელობა, თითო ხაზზე, ყოველის შემდეგ
Enter-ით: `15`, `0`, `7`, `5`, `2`.

მოსალოდნელი შედეგი ისე, როგორც ტერმინალში გამოჩნდება (ხაზები `15`, `0`,
`7`, `5` და `2` თქვენ შეიყვანეთ):
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
