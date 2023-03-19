from decimal import Decimal, getcontext

getcontext().prec = 20

pi = Decimal(1)
n = 1

while 1:
    pi *= (Decimal(2 * n) / Decimal(2 * n - 1)) * (Decimal(2 * n) / Decimal(2 * n + 1))

    n += 1

    print(2 * pi, end="\r")
