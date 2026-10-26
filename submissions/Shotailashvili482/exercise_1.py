def order(item, size = "medium", sugar = 0):
    """prints measurements for each ingredient"""
    print(f"{item} ({size}), sugar: {sugar}")

order("tea")
order("coffee", sugar=2)
order(size="large", item="juice")
order("cocoa", "small", 1)