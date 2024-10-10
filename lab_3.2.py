string=input("Введіть слово: ")
result=""
for char in string:
    if char.isalpha():
        result+=char
print("Слово без символів, що не є буквами: ",result)