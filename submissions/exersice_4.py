def is_valid_username(name):
    if len(name) < 3 or len(name) > 12:
     return False

    for user in name:
        if user == " ":
            return False
    return True

print(is_valid_username("nino"))
print(is_valid_username("ab"))
print(is_valid_username("giorgi kakhidze"))
print(is_valid_username("a b c"))
print(is_valid_username("luka_2024"))