import numpy as np
import matplotlib.pyplot as plt
import math



# x = rad * np.cos(theta)
# y = rad * np.sin(theta)
#
# plt.fill(x, y, color = 'white', linestyle = '-')
for i in range(11):
    theta = np.arange(0, 2*np.pi, 0.01)
    x = i * np.cos(theta)
    y = i * np.sin(theta)
    plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 2)
    plt.plot(i)

x1 = [0, 5*math.sqrt(3)]
y1 = [0, 5]
plt.plot(x1, y1, color = 'Blue')
x2 = [0, 5]
y2 = [0, 5*math.sqrt(3)]
plt.plot(x2, y2, color = 'Blue')
x3 = [0, -5*math.sqrt(3)]
y3 = [0, 5]
plt.plot(x3, y3, color = 'Blue')
x4 = [0, -5]
y4 = [0, 5*math.sqrt(3)]
plt.plot(x4, y4, color = 'Blue')
x5 = [0, -5*math.sqrt(3)]
y5 = [0, -5]
plt.plot(x5, y5, color = 'Blue')
x6 = [0, -5]
y6 = [0, -5*math.sqrt(3)]
plt.plot(x6, y6, color = 'Blue')
x7 = [0, 5*math.sqrt(3)]
y7 = [0, -5]
plt.plot(x7, y7, color = 'Blue')
x8 = [0, 5]
y8 = [0, -5*math.sqrt(3)]
plt.plot(x8, y8, color = 'Blue')

plt.axvline(0, 0, 1, color = 'Black', linestyle = '-')
plt.axhline(0, 0, 1, color = 'Black', linestyle = '-')
plt.axis('equal')
plt.title("Author : Ling-Hao Lin")
plt.grid()
plt.show()
