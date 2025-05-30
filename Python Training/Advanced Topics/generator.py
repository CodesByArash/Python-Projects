def my_range(start, finish):
    i = start
    while i<finish:
        yield i
        i+=1

for i in my_range(5,12):
    print(i)