text=input("Enter a text: ")
elements=set(text.lower())
repeated_elements=set()
for x in elements:
    if text.lower().count(x) >= 2:
        repeated_elements.add(x)
print(repeated_elements)