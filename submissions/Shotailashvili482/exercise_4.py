def is_valid_username(name):
    if 3 <= len(name) <= 12 and " " not in name:
        return True
    return False

    for ch in name:
        if ch == " ":
            return False
    return True

print(is_valid_username("nino"))
print(is_valid_username("ab"))
print(is_valid_username("giorgi kakhidze"))
print(is_valid_username("a b c"))
print(is_valid_username("luka_2024"))