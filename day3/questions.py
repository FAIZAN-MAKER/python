# Q 5 Sum of first n natural numbers

# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1, n+1):
#     sum += i
    
# print(sum)

# Q 6 Factorial of a number.

# num = int(input("Enter a number: "))
# fact = 1

# if num < 0:
#     print("Factorial does not exist for your number.")
# elif num == 0 or num == 1:
#     print("Factorial of your number is 1.")
# else:
#     for i in range(num, 0, -1):
#         fact = fact * i
#     print(f"Facotiral of your number is {fact}")

# Q 7 Print sum of all even and odd numbers in a range seperately.

num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        even_sum += i     
    else:
        odd_sum += i
        

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers are {odd_sum}")