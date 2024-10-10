N = int(input("N = "))
while N < 2:
    print("Помилка. N має бути більше 1")
    N = int(input("N = "))

for i in range(1, N + 1):
    print(" " * (N - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()