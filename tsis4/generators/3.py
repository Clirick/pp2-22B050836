def even_numbers(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0 and i!=0:
            yield i

n = int(input("Введите n: "))

even_nums = even_numbers(n)
print(','.join(map(str, even_nums)))
