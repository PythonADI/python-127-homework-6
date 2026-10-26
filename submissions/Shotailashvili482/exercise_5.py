def ask_number(low=1 , high=10):
    while True:
        print(f"Enter a number from {low} to {high}:")
        number = int(input())
        if low <= number <= high:
            return number
        else:
            print("Out of range.")

first = ask_number()
second = ask_number(high=3)
print(f"You chose {first} and {second}")