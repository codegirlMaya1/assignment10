orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Carla", "Cellular", 4),
    ("Rick", "TV", 3),
    # More orders...
]
first,*next,last=orders
print(first)
print(next)
print(last)