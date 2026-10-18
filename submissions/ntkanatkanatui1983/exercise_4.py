def is_valid_username(name):
    if len(name) < 3 or len(name) > 12:
        return False
    for char in name:
        if char == " ":
           return False
    return True



print(is_valid_username("Nino"))
print(is_valid_username("ab"))
print(is_valid_username("Giorgi Kakhidze"))
print(is_valid_username("a b c"))
print(is_valid_username("Luka_2024"))

 