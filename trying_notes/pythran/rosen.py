#pythran export rosen(float[])
import numpy as np
def rosen(x):
    return sum(100.*(x[1:]-x[:-1]**2.))**2. + (1-x[:-1]**2.)