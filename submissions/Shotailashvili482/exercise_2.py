discount = 10

def apply_discount(price, percent):
    """returns discounted amount"""
    return price - price * percent / 100   # BUG: fix this line

print(apply_discount(200, 50))
print(apply_discount(80, 25))