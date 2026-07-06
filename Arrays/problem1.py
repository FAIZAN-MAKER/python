# 🎯 Problem 1 (Very Easy)

# Given an array of integers, print each element on a new line.

# Example:

# arr = [5, 2, 8, 1]

# Output:

# 5
# 2
# 8
# 1
# Rules
# Use a function.
# Use a for loop.
# Don't search online.
# Think first, then code.

arr = [5, 2, 8, 1]

def print_element(arr):
    for i in arr:
        print(i)
        
print_element(arr)

# As we can see in question, this approach is simple and i don't see any sense using another method since question requirments are this. Let's talk about Time complexity: our program have a funtion and a loop inside it and that loop runs arr(n) times meaning it depends on arr size so it's n, function runs one time. I don't know if i am calculating right or not but anything that i can come up with is O(n) + 1 = O(N). YOu did'nt teach me anything about space complexity so i can't really calculate it. To answer 4 question: i don't think it can be improved, i'll be damend if it can.. really. And as for other questions: What is computer dong inside memeory? bro.. it just created one array and gave them address. when we runs a loop it went each item by using index? most probably. and we just prints it.. that's what i have done with our problem one.