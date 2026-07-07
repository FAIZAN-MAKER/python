# 🎯 Problem 2

# Print the array using indexes, not values.

# Example:

# arr = [10, 20, 30]

# Output:

# Index 0 -> 10
# Index 1 -> 20
# Index 2 -> 30

# Hint: This is different from Problem 1 because you need the index as well as the value.

arr = [10, 20, 30]

for index, value in enumerate(arr):
    print(f"Index {index} -> {value}")