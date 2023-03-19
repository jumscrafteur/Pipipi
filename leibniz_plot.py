import matplotlib.animation as animation
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

sum = 0
den = 1
neg = False


def animate(i, xs, ys):
    global sum
    global den
    global neg

    if neg:
        sum -= 4 / den
    else:
        sum += 4 / den

    den += 2
    neg = not neg

    xs.append(sum)
    ys.append(i)

    xs = xs[-500:]
    ys = ys[-500:]

    print(sum, end="\r")

    ax.clear()
    ax.plot(ys, xs)


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=10)
plt.tight_layout()
plt.show()
