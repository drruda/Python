import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
import string

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Довільний текст до 100 слів
text = """Natural language processing is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful."""

# Токенізація по словам
tokens = word_tokenize(text)

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Функція для лемматизації
def lemmatize_word(word):
    return lemmatizer.lemmatize(word, pos='v')

# Функція для стеммінгу
def stem_word(word):
    return stemmer.stem(word)

# Лемматизація та стеммінг кожного слова
lemmatized_tokens = [lemmatize_word(word) for word in filtered_tokens]
stemmed_tokens = [stem_word(word) for word in filtered_tokens]

# Видалення пункуації
punctuation = set(string.punctuation)
cleaned_tokens = [word for word in stemmed_tokens if word not in punctuation]

# Запис обробленого тексту в новий файл
processed_text = " ".join(cleaned_tokens)

with open("processed_text.txt", "w") as file:
    file.write(processed_text)

print("Оброблений текст збережено у файлі 'processed_text.txt'.")
