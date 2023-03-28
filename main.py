def generator(n):
    num = 1
    while num <= n:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


for i in generator(1000):
    print(i)
