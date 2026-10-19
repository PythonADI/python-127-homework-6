discount = 10  # ვერ მივხვდი ამის დანიშნულებას? პროცენტები ხომ გაწერილი გვაქვს ფუნქციის ნაწილში პარამეტრად და ეს რაღა საჭიროა?..
                
def apply_discount(price, percent):
    return price - price * percent / 100   # BUG: fix this line

print(apply_discount(200, 50))
print(apply_discount(80, 25))