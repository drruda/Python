import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з файлу .csv
file_path = "Data1.csv"
data = pd.read_csv(file_path)

# Введення назви країни користувачем
country = input("Enter the country name: ").strip()

# Перевірка, чи є така країна у даних
if country not in data["Country Name"].values:
    print(f"Country '{country}' not found in the dataset.")
else:
    # Фільтрація даних для вибраної країни
    data_country = data[data["Country Name"] == country]

    # Отримання років і значень показника
    years = [col.split(" ")[0] for col in data.columns if col.startswith("20")]
    values = data_country.iloc[0, 4:].values.astype(float)

    # Побудова стовпчастої діаграми
    plt.figure(figsize=(10, 6))
    plt.bar(years, values, color="skyblue")

    # Підпис осей і графіка
    plt.title(f"Indicator Values for {country}", fontsize=15)
    plt.xlabel("Year", fontsize=12, color="red")
    plt.ylabel("Indicator Value", fontsize=12, color="red")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Відображення графіка
    plt.show()
