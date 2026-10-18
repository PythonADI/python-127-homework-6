discount = 10

def apply_discount(price ,percent):
   """ return the  price after applying the  given percentage discount. """
   return price - price * percent / 100    # BUG fixed

print (apply_discount(200, 50))
print (apply_discount(80,  25))