i = 0
list = []

n = int(input('ваше число: '))

while i != n:
    i += 1
    g = 1
    o = 0
    while o != i:
        o += 1
        g = o * g
    list.append(g)
print(list)


