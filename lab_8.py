# Пищик Іван, тім лід, словник та функція додавання студентів до словника
# Функція для додавання студента до словника через введення з клавіатури
def add_student_from_input():
    name = str(input("Введіть прізвище та ім'я: "))
    # Перевірка, чи студент з таким прізвищем таа ім'ям вже є в словнику
    if name in students_data:
        print(f"Студент {name} вже існує!")
        return
    group= str(input("Введіть номер групи: "))
    course = int(input("Введіть курс: "))

    # Введення оцінок за предмети
    subjects_grades = {}
    print("Введіть предмети та оцінки (для завершення введіть 'стоп'): ")
    while True:
        subject = input("Предмет: ")
        if subject.lower() == "стоп":
            break
        grade = int(input(f"Оцінка за {subject}: "))
        subjects_grades[subject] = grade

    # Додаємо студента до словника
    full_name = f"{name}"
    students_data[full_name] = {
        "group": group,
        "course": course,
        "subjects_grades": subjects_grades
    }


# Наступний студент: додати функцію видалення по прізвищу та ім'ям, організувати діалог між користувачем та програмою(Рожченко Іван)

# Виводимо інформацію про студентів(Рожченко Іван: зробив з дії функцію)
def print_students_data():
    print("\nІнформація про студентів:")
    for student, data in students_data.items():
        print(f"{student} (Група {data['group']}, Курс {data['course']}): {data['subjects_grades']}")

# Функція для видалення студента за прізвищем і ім'ям(Рожченко Іван)
def data_remove(key):
    if key in students_data:
        students_data.pop(key)
        print(f"{student} видалений/на зі списку студентів")
    else:
        print("<--Студента/ку не знайдено-->")

# Наступний студент: додати функцію обрахунку середнього балу студента за прізвищем, додати відповідну дію до діалогу

# функція обрахунку середнього балу студента за прізвищем (Дяченко Юлія)
def averadge_grade_of_student(students: dict):
    student_name = input("Введіть ім'я студента, середній бал якого ви хочете дізнатись: ")
    if student_name in students:
        grades_sum = 0
        grades_amount = 0
        for key in students[student_name]['subjects_grades'].keys():
            grades_sum+=students[student_name]['subjects_grades'][key]
            grades_amount+=1
        print(f"Середній бал студента '{student_name}':", grades_sum/grades_amount)
    else:
        print("Даного студента немає в списку")

# Наступний студент: додати функцію виведення студентів у алфавітному порядку, додати відповідну дію до діалогу
# Функція для виведення студентів у алфавітному порядку (Івженко Тимофій)
def print_sorted_students():
    print("\nСписок студентів за алфавітом:")
    sorted_students = sorted(students_data.keys())
    for student in sorted_students:
        data = students_data[student]
        print(f"{student} (Група {data['group']}, Курс {data['course']}): {data['subjects_grades']}")


# Наступний студент: додати функцію пошуку студента з найвищим середнім балом
# Функція для знаходження студента з найвищим середнім балом
def student_with_highest_average():
    highest_avg = 0
    top_student = ""

    for student, data in students_data.items():
        grades = data['subjects_grades'].values()
        avg_grade = sum(grades) / len(grades)

        if avg_grade > highest_avg:
            highest_avg = avg_grade
            top_student = student

    if top_student:
        print(f"Студент з найвищим середнім балом: {top_student} (Середній бал: {highest_avg:.2f})")
    else:
        print("Список студентів порожній.")


# Створюємо порожній словник для зберігання інформації про студентів
students_data = {'Іванов Іван': {'group': "КН-39.1", 'course': 2, 'subjects_grades': {'Пайтон': 97, 'ЧМ': 92, 'ММДО': 99}},
                 'Петрова Софія': {'group': "КН-39.2", 'course': 2, 'subjects_grades': {'Пайтон': 83, 'ЧМ': 72, 'ММДО': 91}},
                 'Ярило Вікторія': {'group': "КН-39.2", 'course': 2, 'subjects_grades': {'Пайтон': 78, 'ЧМ': 95, 'ММДО': 69}},
                 'Піддубна Марія': {'group': "КН-39.1", 'course': 2, 'subjects_grades': {'Пайтон': 81, 'ЧМ': 98, 'ММДО': 61}},
                 'Розумний Ігор': {'group': "КН-39.2", 'course': 2, 'subjects_grades': {'Пайтон': 73, 'ЧМ': 67, 'ММДО': 88}},
                 'Ніжна Ірина': {'group': "КН-39.1", 'course': 2, 'subjects_grades': {'Пайтон': 84, 'ЧМ': 97, 'ММДО': 98}}
                 }



# Діалог з користувачем (оновлений)
number = 0
while True:
    if number == 0:
        print("\n<1>Вивести список студентів"
              "\n<2>Додати студента/ку"
              "\n<3>Видалити студента/ку"
              "\n<4>Обрахувати середній бал конкретного студента/студентки"
              "\n<5>Вивести студентів за алфавітним порядком"
              "\n<6>Знайти студента з найвищим середнім балом"
              "\n<0>Завершити програму")
        number += 1
    answer = int(input("\nВиберіть дію: "))
    match answer:
        case 0:
            break
        case 1:
            print_students_data()
        case 2:
            add_student_from_input()
        case 3:
            student = str(input("Введіть прізвище і ім'я: "))
            data_remove(student)
        case 4:
            averadge_grade_of_student(students_data)
        case 5:
            print_sorted_students()
        case 6:
            student_with_highest_average()
        case _:
            print("Помилка введення")
print("Програму завершено")