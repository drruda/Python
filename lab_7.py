#виведення на екран всіх значень словника
def Print(people):
    for i,(key, value) in enumerate(people.items(),1):
        print(f"{i}. {key}: зріст {value[0]} см, стать {value[1]}")

#додавання нового запису до словника
def Add(people, key, value):
    if key in people:
        print(f"Запис з ключем '{key}' вже існує.")
    else:
        people[key] = value
        print(f"Додано: {key}")

#видалення запису зі словника
def Del(people, key):
    if key in people:
        del people[key]
        print("Видалено", key)
    else:
        print("Запис не знайдено")

#перегляд вмісту словника за відсортованими ключами
def Sort(people):
    people={k: people[k] for k in sorted(people)}
    print("\nВідсортований словник:")
    Print(people)

#Скласти програму, яка визначає середній зріст чоловіків.
def average_height(people):
    sum=0
    count=0
    for key, value in people.items():
        if value[1]=="чоловіча":
            sum+=value[0]
            count+=1
    return sum/count

people = {
    "Шевченко Олександр": [180, "чоловіча"],
    "Левченко Наталія": [175, "жіноча"],
    "Гнатюк Андрій": [175, "чоловіча"],
    "Романюк Ольга": [160, "жіноча"],
    "Сидоренко Ігор": [182, "чоловіча"],
    "Білий Дмитро": [178, "чоловіча"],
    "Мельник Катерина": [172, "жіноча"],
    "Петров Віктор": [185, "чоловіча"],
    "Кравчук Анна": [168, "жіноча"],
    "Коваленко Марина": [165, "жіноча"]
}

print("---Оберіть дію, що хочете виконати---")
print("Вивести усі значення словника ->1<-\nДодати новий запис ->2<-\nВидалити запис ->3<-\n"
      "Переглянути відсортований за алфавітом словник ->4<-\nПереглянути середній зріст чоловіків ->5<-\nВийти з програми ->0<-\n")
flag = int(input("Введіть значення: "))
while flag!=0:
    if flag == 1:
        print("\nЗначення словника: ")
        Print(people)
    elif flag == 2:
        key = input("\nВведіть прізвище та ім'я: ")
        height = input("Введіть зріст: ")
        gender = input("Введіть стать: ")
        Add(people, key, [height, gender])
    elif flag == 3:
        key = input("\nВведіть ім'я, що хочете видалити: ")
        Del(people, key)
    elif flag == 4:
        Sort(people)
    elif flag==5:
        print(f"\nСередній зріст чоловіків: {average_height(people)} см")

    continue_flag = input("\nБажаєте продовжити? (так/ні): ").strip().lower()
    if continue_flag== "ні":
        break
    flag = int(input("Введіть значення: "))