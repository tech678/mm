import random
import numpy as np
import sympy as sy
def f(x):
  return sy.sin(x**2)
# limits of integration
a = 0
b = 1
N = 100000
ar = np.zeros(N)
for i in range(len(ar)):
  ar[i] = random.uniform(a, b)
integral = 0.0
for i in ar:
  integral += f(i)
ans = (b-a)/float(N)*integral
print("The value calculated by monte carlo integration is {}.".format(round(ans,3)))
x = sy.Symbol("x")
b = sy.integrate(f(x), (x, 0, 1))
print("The value calculated normally using integration is {}.".format(round(b,3)))
