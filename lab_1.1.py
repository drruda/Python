a=int(input("Введіть значення а: "))
while (a<=0 or a>100):
    print("Помилка. Введіть a від 1 до 100")
    a=int(input("Введіть значення а: "))
b=int(input("Введіть значення b: "))
while (b<=0 or b>100):
    print("Помилка. Введіть b від 1 до 100")
    b=int(input("Введіть значення b: "))
if a>b:
    X= float(b/a+61)
elif a==b:
    X=(-5)
else:
    X=float((b-a)/b)
print("Результат: ", X)