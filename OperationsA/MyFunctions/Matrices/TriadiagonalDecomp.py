'''
Created on Jan 24, 2016

@author: ahanagrawal
'''

import numpy as np

def trisolve (coeff, solution):
    
    sol = solution.copy()
    
    c = np.zeros(len(coeff) - 1)
    d = np.zeros(len(coeff))
    e = np.zeros(len(coeff) - 1)
    
    for i in range (0, len(coeff) - 1):
        c[i] = coeff[i+1][i]
    for i in range(0, len(coeff)):
        d[i] = coeff[i][i]
    for i in range(0, len(coeff) - 1):
        e[i] = coeff[i][i+1]

        
        
    for j in range(len(c)):
        lam = c[j]/d[j]
        d[j+1] =  d[j+1] - lam*e[j]
#         sol[j+1] = sol[j+1] - lam*sol[j]
        c[j] = lam
        
    y = np.empty(len(coeff))
    y[0] = sol[0]
    
    for j in range(1, len(coeff)):
        y[j] = sol[j] - y[j-1]*c[j-1]
        
    x = np.empty(len(coeff))
    x[len(d)-1] = y[len(d) - 1]/d[len(d) - 1]
    
    for j in range(len(coeff) - 2, -1, -1):
        x[j] = (y[j] - e[j]*x[j+1])/(d[j])
        
        
    return x
    
    



if __name__ == '__main__':
    a = np.zeros((5,5))
    counter = -1
    fillers = [-1, 2, -1]
    for j in range(len(a)):
        for i in range(counter, counter + 3, 1):
            if i >= 0 and i < len(a):
                a[j][i] = fillers[i - counter]
        counter += 1
    
    coeff = [5, -5, 4, -5, 5]
    print(a)
    x = trisolve(a, coeff)
    print(x)
        
            
        
    
 