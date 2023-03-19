import random

R = 1e100
totalPoint = 0
cerclePoint = 0

while True:
    # Place un point aleatoire sur un plan de 2R par 2R
    # Sur ce plan on trace un cercle de rayon R
    # Le point a une rance de Pi*R^2 / 4R^2 d'etre sur le cercle
    # en calculant ce ration on obtiens Pi

    x = random.randint(-1 * R, R)
    y = random.randint(-1 * R, R)
    totalPoint += 1

    if x * x + y * y < R * R:
        cerclePoint += 1

    print(4 * (cerclePoint / totalPoint))
