from math import*

print("sine taylor series is=")

x = float(0.64)
x1 = float(640/(3.1416))
x2 = 640

flag = False
res = 0
for k in range(0, 50, 1):
    y = ((-1) ** k) * (x ** (1 + 2 * k)) / factorial(1 + 2 * k)
    res = res+y
print(sin(1.5*3.1416))
print(sin(10-(3*3.1416)))