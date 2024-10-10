numbers=list(map(int,input("Enter a list: ").split()))
for x in range(len(numbers)):
    if x!=0 and x%2==0:
        numbers[x]=int(input("Enter new value: "))
print(numbers)