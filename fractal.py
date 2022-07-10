import numpy as np
from services import plot

def formula1(z, c):
    z = (z * z) + c
    return z

def formula2(z, c):
    z = (z * np.sin(z)) + c
    return z

def formula3(z, c):
    z = z - (z - 1)*(z - 1)*(z - 1)/(3*z*z) + c
    return z



def mandelbrot(n_x, n_y, iterations,formula):
    x_cor = np.linspace(-2,1,n_x) # evenly spaced n_x number of numbers between -2 and 1
    y_cor = np.linspace(-2,1,n_y) # evenly spaced n_y number of numbers between -2 and 1
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len)) # initialize output array with size of x_len and y_len
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_cor[i], y_cor[j])
            z = complex(0.5, 0.5)
            count = 0
            for k in range(iterations):
                z = formula(z, c)
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
            print("{:3.1f}% completed".format((i/x_len)*100))
    plot(output.T)


mandelbrot(700,700,100,formula3)
