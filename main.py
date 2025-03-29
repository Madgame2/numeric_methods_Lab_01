import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fixed_point
from decimal import Decimal
from my_math import *


def F(x):
    return x**3+8*x-6

def F_prim(x):
    return 3*x**2+8

x= np.linspace(-5,5,100)
y=F(x)

def create_plot():
    fig,ax = plt.subplots()
    ax.axhline(0, color='black', linewidth=0.5)  # Ось X
    ax.axvline(0, color='black', linewidth=0.5)  # Ось Y
    ax.grid(True, linestyle='--', linewidth=0.5)  # Сетка
    return fig,ax

def add_function_to_plot(ax,func,x_range, color='b',label=None,linewidth=2,linestyle='-'):
    x = np.linspace(*x_range,100)
    y = F(x)
    ax.plot(x,y,color=color,linewidth=linewidth,linestyle=linestyle,label=label)
    if label:
        ax.legend()

fig, ax = create_plot()
add_function_to_plot(ax,F,(-5,5),color='r',label=r'$f(x) = x^3 + 8x - 6$')

x0 = Decimal(1.0)

result_1 = bisection_method(F,-5,5, tol=0.01)
result_2 = Newton_method(F,F_prim,1, tol=0.01)

phi = lambda x: 6 / (x ** 2 + 8)
root = simple_iteration(phi, x0=1)

print(f"Корень (по полам): {result_1}")
print(f"Корень (Ньютона): {result_2}")
print(f"Корень (Итераций): {root}")


plt.show()

