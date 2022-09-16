import random
i = 0
list = []
n = int(input('ваше число: '))
m = -n - 1
res = []
d = ''

while m != n:
    m += 1
    if random.randint(0, 1) == 1 and len(list) != n:
        list.append(m)

print(list)

p = input()
p += ' '
plen = len(p)


res = 1

while i != plen:
    if p[i] != ' ':
        d = d + p[i]
    else:
        d = int(d)
        h = list[d]
        res = res * h
        d = ''
    i += 1

print(res)
