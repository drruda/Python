from mod import calculate_S

N=int(input("Введіть значення N>1: "))
while N<=1:
    print("Помилка. N має бути більше 1")
    N=int(input("Введіть значення N ще раз: "))

result_2 = calculate_S(N)
print("Cумa квадратів чисел від 1 до %d: " %(N), result_2)