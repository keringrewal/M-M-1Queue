#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kerin Grewal
lt1_problem1
Python 3
"""



"""DIRECTIONS
Call SimulateA() to test the results
Returns a 2 element list
"""

import matplotlib.pyplot as plt
import math
import numpy as np

class RandVar():
    
    def exp(lamb):
        x = np.random.uniform()
        y = -(np.log(1-x))/ lamb
        return [x, y]
    
    def drawScatter(K, lamb, N):
    
        X = [0]*N
        Y = [0]*N
        
        
        for i in range(1, N):
            Y[i] = K[i][1]
            X[i] = K[i][0]
            
        X.sort()
        Y.sort()
        
        plt.scatter(Y, X, color="red", s = 3)
        
        xas = [i/5 for i in range(11)]
        yas = [1 - math.exp(-lamb * x) for x in xas]
        plt.plot(xas, yas, color='blue', ms =.1)
        plt.legend(('Actual results', 'Experimental Results'))
        
        plt.title("Analytical/Experimental Distribution")
        plt.xlabel("Outcome")
        plt.ylabel("Probability")
        plt.legend()
        plt.show()
    
    
    
    


    
lamb= 4
N = 1000

def SimulateA(lamb= 4, N= 1000):
    X = [0] * N
    for i in range(N):
        X[i] = RandVar.exp(lamb)

    RandVar.drawScatter(X, lamb, N)
