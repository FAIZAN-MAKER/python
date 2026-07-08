arr = [8, 3, 15, 2, 10]

largest_number = arr[0]
second_largest_numer = arr[0]

for i in arr[1:]:
    if i > largest_number:
        largest_number = i
    
arr.remove(largest_number) # With this approach i am removing the largest number so i can just fin the second largest number by finding the largest in remainig. This is approach i came up with my reasoning.

for i in arr[1:]:
    if i > second_largest_numer:
        second_largest_numer = i

print(f"The second largest number in given list is: {second_largest_numer}")

# Time Complexity: It should be O(n), since our main work going is running two loops. And both of them are O(n) + O(n) resulting in 2n and we ignore constants as we work with worst case scenrios.

# SPace complexity should be constant. O(1), i made two variables. 1+1 = 2 and it becomes 1 since it's constant. If i am wrong then tell me cuz i am calculating it via the method of time complexity that we learned.

# Due to some problems. Like if i have arr = [15] and arr = [15, 15, 10]. Then my Algorithm would not honestly work that's why i am coming up with another way. 

arr = [8, 3, 15, 2, 10]

largest_number = arr[0]
second_largest_numer = arr[0]

for i in arr[1:]:
    if i > largest_number :
       second_largest_numer = largest_number
       largest_number = i
       continue
       
    if i > second_largest_numer:
        second_largest_numer = i
       
print(second_largest_numer)


# Time complexity: O(n). NO need to expain since its linear.
# Space complexity: cONSTANT which means o(1)
        
