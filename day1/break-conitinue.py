for i in range(1, 10):
    if i == 5:
        break

    print(i)
    
print("Here the continue part starts")
    
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    
print("Here starts the else part")
    

for i in range(1, 10):
    if i == 2:
        break
    print(i)
else:
    print("BREAK DID'NT REACH IT'S DESTINATION")