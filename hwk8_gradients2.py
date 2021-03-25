#By Kay Towner

import math
import numpy as np
import scipy as py
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#2.) Gradient Descent:

def func(x, y):
    """Function for the equation in HW question 2. parts a and b."""
    return (5*np.exp(-(x-1)**2-(2*(y-3)**2))) + (3*np.exp(-2*(x-4)**2-(y-1)**2))

#C/ a:
def deriv_func_x(x_1=None, x_2=None):
    """Function of the derivative of the first function 'func'."""
    return ( func(x_1) - func(x_1) ) / ( (x_2) - (x_1) )

def deriv_func_y(x_1=None, x_2=None):
    """Function of the derivative of the first function 'func'."""
    return ( func(y_2) - func(y_1) ) / ( (y_2) - (y_1) )

#C/ b: Make my own grad-descent function:
def gradient(x, y, intitialguess=None, gamma=None, f_prime=None):
    """Function that returns the gradient of derivative of f.
    input: gamma
    output: maximum at (+) gamma*f prime"""   
    return x + gamma*(f_prime) 


if __name__=="__main__":
#values:
    x_1 = 0
    x_2 = 5
    y_1 = 0
    y_2 = 5

    x=1
    y=3

#a) Graphing the plot:
    xdomain = np.linspace(0, 5)
    ydomain = np.linspace(0, 5)
    x, y = np.meshgrid(xdomain, ydomain)
    z = (5*np.exp(-(x-1)**2-(2*(y-3)**2))) + (3*np.exp(-2*(x-4)**2-(y-1)**2))

    fig,ax=plt.subplots(1, 1)
    cp = ax.contourf(x, y, z)
    plt.contour(z, x, y)
    plt.colorbar(cp)
    plt.title('Contourplot')
    plt.show()
    plt.savefig('Contourplot.jpeg')
    
#b) scipy minimizing using the powell method:
    x0 = np.array([0, 1, 2, 3, 4, 5])
    fmin = py.optimize.minimize(func, x0, method='powell',
               options={'xatol': 1e-8, 'disp': True})
    print('The mimimization is:', fmin)

#C/ a:
    grad_for_part_a = gradient(deriv_func(x, y))
    print('The max of deriv_func is:', grad_for_part_a)
#C/ b: 
    grad_for_b = gradient(x, y, initialguess=3, gamma=4, f_prime=deriv_func(x_1, x_2, y_1, y_2))
    print('The max of deriv_func is:', grad_for_b)

#I got tripped up when it came to the py optimize method. I couldn't seem to
    #get it to work with the y veriable. The second trouble I had was with the
    #x and y veriables but how to "merge" the two functions.


#the "true derviative" of func():
#(5*np.exp(x**2+2*x+12*y-2*y**2-17)) + (3*np.exp(-2*x**2+16*x+2*y-33))







