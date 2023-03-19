from decimal import Decimal, getcontext

from scipy.special import factorial, factorial2

getcontext().prec = 100

sum = Decimal(0)
k = 0
add = Decimal(1)
while add > 1e-100:
    add = Decimal(2 * factorial(k, exact=True)) / Decimal(
        factorial2(2 * k + 1, exact=True)
    )
    sum += add
    k += 1
    # print(sum)

print(sum)
