arr = [8, 3, 15, 2, 10]
largest_num = arr[0]

for i in arr[1:]:
    if i > largest_num:
        largest_num = i
        
print(largest_num)

# I choosed this approach cuz i think it's just so simple that i work with this way, and this was the first thing that could come in my mind like just run a loop and store what is largest, a piece of cake. Time complexity? it should be O(n), no explaining since it's just so simple and we've been learning it and i can guess just by looking at it. And space complexity? array was given, we only created one variable so it's gotta be O(1). I don't think it can be improved, i am sure as hell.