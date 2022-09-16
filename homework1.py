while True:   
    sum = 0

    number = str(input('ваше число: '))

    lnumber = len(number)

    while lnumber != 0:
        a = number[lnumber - 1]
        if a == '1' or a == '2' or a == '3' or  a == '4' or  a == '5' or  a == '6' or  a == '7' or  a == '8' or  a == '9' or  a == '0':
            sum = int(a) + sum
        lnumber -= 1

    print('сумма цифр вашего числа: ' + str(sum))