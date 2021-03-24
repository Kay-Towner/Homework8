#By Kay Towner

import math
import numpy as np
import scipy as py
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#1. a)
def buckingham(x):
    """Function of the Buckingham potential formula."""
    return 1 * (np.exp(-1*x[:1])) - (1/x[:1]**6)

#Main:
if __name__=="__main__":
#1.) Scipy Optimization:
    
    #r =  #electron voltz
    A = 1
    B = 1
    C = 1
    phi = 10  #10 angstroms = 1nm

#a)  Graphing the plot:
    r = np.array(range(20)) #x-axis
    angs = A * np.exp(-B*r) - (C/r**6) #y-axis
    plt.title('Potential Plot')
    plt.xlabel('eV')
    plt.ylabel('Angstroms')
    plt.plot(r, angs)
    plt.show()
    plt.savefig('Potential_plot.jpeg')

#b) Minimizing (Maxing) the function:
    x0 = np.array([0, 1, 2, 3, 4, 5])
    res = minimize(buckingham, x0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})
    print('The mimimization is:', res)

#even though this is a minimizing routine, I think just looking
#at the largest value that would be the (abs) maximum of the function.























    
