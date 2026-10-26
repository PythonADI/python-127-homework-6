def split_time(total_seconds):
    """calculates amount of 60s in each number as minutes and leftovers as seconds"""
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

minutes, seconds = split_time(135)
print(f"{minutes} min {seconds} s")
minutes, seconds = split_time(59)
print(f"{minutes} min {seconds} s")
minutes, seconds = split_time(3600)
print(f"{minutes} min {seconds} s")