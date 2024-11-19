import numpy as np
import matplotlib.pyplot as plt

# Задаємо список
people = [
    {"name":"Shevchenko Oleksandr", "height": 180, "gender": "male"},
    {"name":"Levchenko Nataliya", "height": 175, "gender": "female"},
    {"name":"Hnatyuk Andrii", "height": 175, "gender": "male"},
    {"name":"Romaniuk Olha", "height": 160, "gender": "female"},
    {"name":"Sydorenko Ihor", "height": 182, "gender": "male"},
    {"name":"Bilyi Dmytro", "height": 178, "gender": "male"},
    {"name":"Melnyk Kateryna", "height": 172, "gender": "female"},
    {"name":"Petrenko Viktor", "height": 185, "gender": "male"},
    {"name":"Kravchuk Anna", "height": 168, "gender": "female"},
    {"name":"Kovalenko Maryna", "height": 165, "gender": "female"}
]

# Розподіл з категоріями
categories = {"<170": 0, "170-180": 0, ">180": 0}
for person in people:
    height = person["height"]
    if height < 170:
        categories["<170"] += 1
    elif 170 <= height <= 180:
        categories["170-180"] += 1
    else:
        categories[">180"] += 1

# Дані для кругової діаграми
labels = list(categories.keys())
sizes = list(categories.values())

# Побудова кругової діаграми
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax.axis("equal") # кругла діаграма
plt.title("Зріст людей")
plt.show()