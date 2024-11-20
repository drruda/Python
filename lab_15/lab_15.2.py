import pandas as pd
import matplotlib.pyplot as plt

# Налаштування стилю графіків
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# Завантаження даних із файлу
fixed_df = pd.read_csv(
    'Data2015.csv',
    sep=',',
    encoding='latin1',
    parse_dates=['Date'],
    dayfirst=True,
    index_col='Date'
)

# Додавання стовпця 'Month' із місяцем
fixed_df['Month'] = fixed_df.index.month
# Сумуємо використання велодоріжок по місяцях
monthly_usage = fixed_df.groupby('Month').sum().sum(axis=1)

# Визначення найпопулярнішого місяця
most_popular_month = monthly_usage.idxmax()
print(f"Найпопулярніший місяць для велосипедистів: {most_popular_month} місяць")
print(f"Кількість використань велодоріжок у цей місяць: {monthly_usage[most_popular_month]}")

# Побудова графіка використання велодоріжок по місяцях
monthly_usage.plot(kind='bar', color='skyblue', title='Використання велодоріжок по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість використань')
plt.xticks(range(12), ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру'], rotation=45)
plt.show()
