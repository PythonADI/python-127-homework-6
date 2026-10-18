def order(item, size ="medium", sugar = 0):
    """  print the drink order and its sugar amount. """
    print(f"{item} ({size}), sugar: {sugar}")


order("tea")
order("coffee", sugar=2)
order(size = "large", item = "juice")
order("cocoa", "small", sugar=1)