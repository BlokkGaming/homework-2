import random

f = int(input())

list = []
i = 0

while i != f:
    i += 1
    a = input('')
    list.append(a)

i = 0

while i != f:
    n = list[random.randint(0, f-1)]
    list.remove(n)
    list.append(n)
    i += 1
   
print(list)