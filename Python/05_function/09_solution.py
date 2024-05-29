def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

limit = 10
print(even_generator(limit))

for num in even_generator(10):
    print(num)

