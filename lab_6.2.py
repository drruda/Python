numbers=list(map(int,input("Enter a list: ").split()))
for x in range(0, len(numbers)-1, 2):
    numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
print(numbers)