import json

# Ініціалізація даних
people = [
    {"name": "Shevchenko Oleksandr", "height": 180, "gender": "male"},
    {"name": "Levchenko Nataliya", "height": 175, "gender": "female"},
    {"name": "Hnatyuk Andrii", "height": 175, "gender": "male"},
    {"name": "Romaniuk Olha", "height": 160, "gender": "female"},
    {"name": "Sydorenko Ihor", "height": 182, "gender": "male"},
    {"name": "Bilyi Dmytro", "height": 178, "gender": "male"},
    {"name": "Melnyk Kateryna", "height": 172, "gender": "female"},
    {"name": "Petrov Viktor", "height": 185, "gender": "male"},
    {"name": "Kravchuk Anna", "height": 168, "gender": "female"},
    {"name": "Kovalenko Maryna", "height": 165, "gender": "female"}
]

# Запис початкових даних у файл
with open("PeopleData.json", "wt") as file:
    json.dump(people, file, indent=4)

# Завантаження даних з JSON-файлу
def load(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return []


# Збереження даних у JSON-файл
def save(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Виведення вмісту JSON-файлу
def display(filename):
    data = load(filename)
    if data:
        for person in data:
            print(f"Name: {person['name']}, Height: {person['height']}, Gender: {person['gender']}")
    else:
        print("File is empty or not found.")


# Додавання нового запису
def add(filename):
    data = load(filename)
    name = input("Enter name: ")
    height = int(input("Enter height: "))
    gender = input("Enter gender (male/female): ")

    data.append({"name": name, "height": height, "gender": gender})
    save(data, filename)
    print(f"{name} successfully added.")


# Видалення запису за ім'ям
def delete(filename):
    data = load(filename)
    name = input("Enter name to delete: ")
    new_data = [person for person in data if person["name"] != name]

    if len(new_data) < len(data):
        save(new_data, filename)
        print(f"{name} successfully deleted.")
    else:
        print(f"{name} not found.")


# Пошук за іменем
def search(filename):
    data = load(filename)
    name = input("Enter name to search: ")
    for person in data:
        if person["name"] == name:
            print(f"Name: {person['name']}, Height: {person['height']}, Gender: {person['gender']}")
            return
    print(f"{name} not found.")


# Обчислення та збереження середнього зросту чоловіків
def average_height(filename, output_filename):
    data = load(filename)
    male_heights = [person["height"] for person in data if person["gender"] == "male"]

    if male_heights:
        avg_height = sum(male_heights) / len(male_heights)
        print(f"Average height of males: {avg_height:.2f}")

        # Зберігаємо результат у файл
        with open(output_filename, "wt") as file:
            json.dump({"Average height of males": avg_height}, file, indent=4)
    else:
        print("There are no males in the list.")


# Основна програма
filename = "PeopleData.json"
output_filename = "AverageHeight.json"

while True:
    print("\nShow file content ->1<-")
    print("Add record ->2<-")
    print("Delete record ->3<-")
    print("Search record by name ->4<-")
    print("Calculate average height of males and save the result ->5<-")
    print("Exit program ->0<-")

    x = input("\nSelect action: ")

    if x == "1":
        display(filename)
    elif x == "2":
        add(filename)
    elif x == "3":
        delete(filename)
    elif x == "4":
        search(filename)
    elif x == "5":
        average_height(filename, output_filename)
    elif x == "0":
        print("Program terminated.")
        break
    else:
        print("Invalid input. Please try again.")
