def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except Exception as e:
        print("Помилка відкриття файлу", file_name, ":", e)
        return None
    else:
        print("Файл", file_name, "успішно відкрито")
        return file  # Повертаємо об'єкт файлу


# Імена файлів
file1 = "TF16_1.txt"
file2 = "TF16_2.txt"
vowels = "аеєиіїоую"  # Голосні українські літери

# а) Створення текстового файлу TF16_1
file1_w = Open(file1, "w")
if file1_w is not None:
    file1_w.write(
        "Узимку часто йдуть сніг і дощ, а іноді утворюються іскристі кристали на поверхні, що створюють дивовижну атмосферу.")
    print("Інформацію було записано в файл TF16_1.txt")
    file1_w.close()

# б) Читання вмісту файлу TF16_1, знаходження слів на голосні та запис у TF16_2
file1_r = Open(file1, "r")
if file1_r is not None:
    sentence = file1_r.read()  # Читаємо вміст файлу
    words = sentence.split()  # Розбиваємо речення на слова
    res = [word for word in words if word.lower()[0] in vowels]  # Фільтруємо слова на голосні

    # Записуємо знайдені слова у файл TF16_2
    file2_w = Open(file2, "w")
    if file2_w is not None:
        for word in res:
            file2_w.write(word + '\n')  # Записуємо кожне слово на новому рядку
        file2_w.close()
    file1_r.close()  # Закриваємо перший файл

# в) Читання вмісту файлу TF16_2 і вивід по рядках
print("\nВміст файлу TF16_2.txt:")
file2_r = Open(file2, "r")
if file2_r is not None:
    for line in file2_r:
        print(line.strip())  # Виводимо кожен рядок без зайвих пробілів
    file2_r.close()  # Закриваємо другий файл