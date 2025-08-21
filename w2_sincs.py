from math import sin
from math import pi

#def g_sinc_long(f): # i tried defining the below function w/o lambda
#    def s(x):
#        fx = f(x)
#        return 1. if f(x) == 0. else sin(f(x)) / f(x)
#    return s

def g_sinc(f): # returns a function
    return lambda x : 1.0 if abs(f(x) - 0.0) < 1e-15 \
        else sin(f(x)) / f(x)

def u_sinc(x):
    return g_sinc(lambda x : x)(x)#, g_sinc_long(lambda x : x)(x)

def n_sinc(x):
    return g_sinc(lambda x : pi * x)(x)

## now my playing around

def approx_zero(f):
    def wraps(*args, **kwargs):
        fargs = f(*args, **kwargs)
        return 0 if abs(fargs) < 1e-15 else fargs
    return wraps

@approx_zero
def my_n_sinc(x):
    pix = pi * x
    return 1 if pix == 0 else sin(pix) / pix

print(my_n_sinc(2.99), my_n_sinc(3))