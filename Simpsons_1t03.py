from math import pi, sin

def f(x): return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
a = 0                   
b = pi/2                

n = 6                   
h = (b - a) / n   


S = (f(a) + f(b))
for i in range(1, n, 2):      #for odd
    S += 4 * f(a + i*h)
for i in range(2, n, 2):       #for even
    S += 2 * f(a + i*h)
I = 1/3 * h * S

print("Integral of the equation, I = %f" % I)
