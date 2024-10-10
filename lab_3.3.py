from collections import Counter
string=input("Введіть речення: ")
words=string.split()
word_list=Counter(words)
result=" ".join([word for word, count in word_list.items() if count==1])
print("Речення без повторів: ", result)