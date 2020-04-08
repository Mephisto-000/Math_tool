import numpy as np
import matplotlib.pyplot as plt
import math




def circle_plot(k):
    theta = np.arange(0, 2*np.pi, 0.01)   
    r = np.arange(0, k)
    for i in r:
        x = i * np.cos(theta)
        y = i * np.sin(theta)
        plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 2)
        plt.plot(i)
    plt.axvline(0, 0, 1, color='Black', linestyle='--')
    plt.axhline(0, 0, 1, color='Black', linestyle='--')
    plt.plot(0, 0, 'o', color='Black', linewidth=5)
    plt.axis('equal')    
    plt.grid()
    plt.show()


def conic_section(l,a,b):
    theta = np.arange(0, 2*np.pi, 0.01)
    r = np.arange(0, l + 1)
    for i in r:
        x = (i * a)* np.cos(theta)
        y = (i * b) * np.sin(theta)
        plt.plot(x, y, color = 'red', linestyle = '-', linewidth = 2)
        plt.plot(i)
    plt.axvline(0, 0, 1, color='Black', linestyle='--')
    plt.axhline(0, 0, 1, color='Black', linestyle='--')
    plt.plot(0, 0, 'o', color='Black', linewidth=5)
    plt.axis('equal')    
    plt.grid()
    plt.show()


def line(a, b, c, d, cl):
    x = [a, c]
    y = [b, d]
    plt.plot(x, y, '-', color = '%s' %cl, linewidth = 2)
    plt.axvline(0, 0, 1, color='Black', linestyle='--')
    plt.axhline(0, 0, 1, color='Black', linestyle='--')
    plt.plot(0, 0, 'o', color = 'Black', linewidth = 5)
    plt.axis('equal')
    plt.grid()
    plt.show()




if __name__ =='__main__':

    





