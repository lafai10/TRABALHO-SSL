def f(t):
    if t == 0:
        return 1
    return 5 * 2**t - 4

t = 0
while t <= 8:
    print(f(t))
    t += 1

#Plota o gráfico
import matplotlib.pyplot as plt
t = range(0, 15)
y = [f(t) for t in t]

plt.plot(t, y)
plt.title('Ex1')
plt.grid(True)
plt.show()
