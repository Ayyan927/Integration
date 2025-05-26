#(f(x)=x^{2}\) at \(x=2\)
import numpy as np
def f(x):
    return x ** 2
def derivative(f, x):
    h = 0.0001  
    return (f(x + h) - f(x)) / h 
print(np.round(derivative(f, 2)))
