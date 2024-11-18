a = 5
b = 80
count = 0
suma = 0
for i in range(a, b + 1):
    count += 1
    suma += i ** 2
average = float(suma / count)
print(average)
