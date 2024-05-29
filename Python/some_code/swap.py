# x = 34
# y = 76
# x , y = y , x

# print(x)
# print(y)

doors = [False] * 100
for i in range(100):
   for j in range(i, 100, i+1):
       doors[j] = not doors[j]
   print("Door %d:" % (i+1), 'open' if doors[i] else 'close')