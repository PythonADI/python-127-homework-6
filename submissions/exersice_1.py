def order(item, size="medium", sugar=0):
    print(f"{item} ({size}), sugar: {sugar}") 

order("tea")
order("coffee", sugar=2)
order("juice", size="large")
order("cocoa", size="small", sugar=1)