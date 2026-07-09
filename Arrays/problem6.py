n = 687
sum = 0

digits = [int(d) for d in str(n)]

for i in digits:
    sum += i
    
print(sum)