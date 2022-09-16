k = 0 
number = int(input('ваше число: '))
sum = 0

while k != number:
    k += 1
    res = (1 + 1 / k) ** k
    sum = sum + res

print(sum)