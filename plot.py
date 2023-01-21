import matplotlib.pyplot as plt
import numpy as np
from math import exp

def slope(x, y):
    #return x+y
    #return x**2 + 2*x - y
    return 3*x*x*y
    #return y-x
    #return pow(x, 3)* exp(-2*x)-2*y

def function(x):
    #return 2*exp(x)-x-1
    #return x**2 + exp(1-x)
    return exp(x**3)
    #return exp(x)+x+1
    #return exp(-2*x) * (pow(x, 2)+4)/4

x0global = 0
y0global = 1
xn = 1
h = 0.1

#analytical graph
x0 = x0global
y0 = y0global
xArray = np.arange(start = x0, stop = xn+h, step = h)
yArray = np.zeros(len(xArray))

print("\nAnalytical Method")
print("x \t\t y (analytical)")
for i in range(len(xArray)):
    yArray[i] = function(xArray[i])
    print("%f \t %f" % (xArray[i], yArray[i]))

plt.plot(xArray, yArray, "red", label="Analytical graph")

#rk1 method
print("\nRK 1 Method / Euler's Method")
print("x \t\t y (rk1) \t y (analytical)")
print("%f \t %f \t %f" % (x0, y0, function(x0)))

n = int((xn - x0) / h)

xArray1 = np.zeros(n+1)
yArray1 = np.zeros(n+1)
xArray1[0] = x0
yArray1[0] = y0

#Plot Euler's method(rk1)
for i in range(n):
    y0 += slope(x0, y0) * h
    x0 += h
    print("%f \t %f \t %f" % (x0, y0, function(x0)))
    xArray1[i+1] = x0
    yArray1[i+1] = y0

plt.plot(xArray1, yArray1, "x-", label = "Euler h = " + str(h))

#rk2 method
x0 = x0global
y0 = y0global
print("\nRK 2 Method / Modified Euler's Method")
print("x \t\t y (rk2) \t y (analytical)")
print("%f \t %f \t %f" % (x0, y0, function(x0)))

n = int((xn - x0) / h)

xArray2 = np.zeros(n+1)
yArray2 = np.zeros(n+1)
xArray2[0] = x0
yArray2[0] = y0

#Plot rk2 method
for i in range(n):
    k1 = h * slope(x0, y0)
    k2 = h * slope(x0+h, y0+k1)
    y0 += (k1+k2)/2
    x0 += h
    print("%f \t %f \t %f" % (x0, y0, function(x0)))
    xArray2[i+1] = x0
    yArray2[i+1] = y0

plt.plot(xArray2, yArray2, color='black', marker='o', linestyle='dashed', markersize=4, label = "RK 2 h = " + str(h))

#rk4 method
x0 = x0global
y0 = y0global
print("\nRK 4 Method")
print("x \t\t y (rk4) \t y (analytical)")
print("%f \t %f \t %f" % (x0, y0, function(x0)))

n = int((xn - x0) / h)

xArray3 = np.zeros(n+1)
yArray3 = np.zeros(n+1)
xArray3[0] = x0
yArray3[0] = y0

#Plot rk4 method
for i in range(n):
    k1 = h * slope(x0, y0)
    k2 = h * slope(x0+h/2, y0+k1/2)
    k3 = h * slope(x0+h/2, y0+k2/2)
    k4 = h * slope(x0+h, y0+k3)
    y0 += (k1+2*k2+2*k3+k4)/6
    x0 += h
    print("%f \t %f \t %f" % (x0, y0, function(x0)))
    xArray3[i+1] = x0
    yArray3[i+1] = y0

plt.plot(xArray3, yArray3, color='yellow', marker='*', linestyle='dashed',  linewidth=1, markersize=3, label = "RK 4 h = " + str(h))
plt.title("RK method.")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


