import numpy as np
import matplotlib.pyplot as plt
import math


# x = rad * np.cos(theta)
# y = rad * np.sin(theta)
#
# plt.fill(x, y, color = 'white', linestyle = '-')



def plot(k):
    theta = np.arange(0, 2*np.pi, 0.01)   
    r = np.arange(0, k)
    for i in r:
        x = i * np.cos(theta)
        y = i * np.sin(theta)
        plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 2)
        plt.plot(i)
    plt.axis('equal')    
    plt.grid()
    plt.show()


def trans(l):
    theta = np.arange(0, 2*np.pi, 0.01)
    r = np.arange(0, l)
    for i in r:
        x = (i * 2)* np.cos(theta)
        y = (i * 3) * np.sin(theta)
        plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 2)
        plt.plot(i)
    plt.axis('equal')    
    plt.grid()
    plt.show()


def line(u):
    ur = np.arange(0,u)
    for i in ur:
        x = np.arange(-i, i)
        y = (j for j in range(i))
        yl = np.array(list(y))
        plt.plot(xl, yl, color = 'red') 
    plt.show()




if __name__ =='__main__':
    plot(10)
    trans(10)
    line(10)







