import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt
from collections import Counter

# Завантаження тексту з файлу
try:
    with open('melville-moby_dick.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

# Функція для підрахунку кількості слів
def count_words(text):
    words = word_tokenize(text)  # токенізація по словах
    return len(words)

# Функція для знаходження 10 найбільш вживаних слів та побудови діаграми
def most_used_words(text, title):
    words = word_tokenize(text.lower())  # токенізація та переведення в нижній регістр
    words = [word for word in words if word.isalpha()]  # залишаємо лише слова
    cnt = Counter(words)
    most_common = cnt.most_common(10)
    x = [word[0] for word in most_common]
    y = [word[1] for word in most_common]

    # Побудова діаграми
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue')
    plt.title(title)
    plt.xlabel("Слова")
    plt.ylabel("Кількість повторень")
    plt.show()

# Підрахунок слів у тексті
nltk.download('punkt')
total_words = count_words(text)
print(f"Кількість слів у тексті: {total_words}")

# 10 найбільш вживаних слів до очищення
most_used_words(text, "10 найбільш вживаних слів (до очищення)")

# Видалення стоп-слів та пунктуації
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
words = word_tokenize(text.lower())
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# 10 найбільш вживаних слів після очищення
filtered_text = ' '.join(filtered_words)
most_used_words(filtered_text, "10 найбільш вживаних слів (після очищення)")

# Підрахунок слів після очищення
filtered_word_count = len(filtered_words)
print(f"Кількість слів після очищення: {filtered_word_count}")
