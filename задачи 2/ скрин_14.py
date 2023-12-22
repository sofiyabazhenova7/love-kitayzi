import math
r = float(input("Введите радиус: "))
h = float(input("Введите высоту"))
plt = 1000
def vika(r,h,plt):
    m = r**2*h*math.pi*plt
    m = round(m, 2)
    print(m)

vika(r,h,plt)
