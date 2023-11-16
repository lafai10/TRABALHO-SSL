def f(t):
    if t == 0:
        return 1
    return t+3*2**t - 2*3**t 

t = 0
while t <= 8:
    print(f(t))
    t += 1

#Plota o gráfico
import matplotlib.pyplot as plt
t = range(0, 15)
y = [f(t) for t in t]

plt.plot(t, y)
plt.title('Ex3')
plt.grid(True)
plt.show()