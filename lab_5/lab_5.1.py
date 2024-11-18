N=int(input("Введіть кількість елементів масиву: N = "))
print("Введіть %d значень масиву arr:" %N)
arr=[int(input()) for _ in range(N)]
positive=[x for x in arr if x>0]
min_element=min(positive)
print("Мінімальний додатній елемент: ", min_element)