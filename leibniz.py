sum = 0
den = 1
neg = False

while True:
    if neg:
        sum -= 4 / den
    else:
        sum += 4 / den

    den += 2
    neg = not neg

    print(sum, end="\r")
    pass
