def reverse(number) :
    count = 0
    digits = 1
    temp = number

    while temp > 0 :
        temp -= (temp % (10 ** digits))
        digits += 1

    newNum = 0
    while digits >= 0 :
        newNum += (number % (10 ** count)) * (10 ** (digits - count))
        number -= (number % (10 ** count))
        count += 1
        digits -= 1

    return newNum