# Creating a tuple
my_tuple = (10, 20, 30)

print("Original Tuple:", my_tuple)

# Attempting to modify an element
try:
    my_tuple[1] = 50
except TypeError as e:
    print("Error:", e)

print("Tuple after modification attempt:", my_tuple)