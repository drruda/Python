import math

def calculate_z(x, y):
    z=(math.cos(math.radians(x))**2)+(math.sin(math.radians(y))**2)
    return z

def calculate_S(N):
    S=0
    for i in range(1, N+1):
        S+=i**2
    return S

print("Введіть значення х та у в градусах")
x=int(input(" х: "))
y=int(input(" у: "))

print("Значення функції z: %.2f" %calculate_z(x, y))
print(" ")

N=int(input("Введіть значення N>1: "))
while N<=1:
    print("Помилка. N має бути більше 1")
    N=int(input("Введіть значення N ще раз: "))

print("Cумa квадратів чисел від 1 до %d: " %(N), calculate_S(N))