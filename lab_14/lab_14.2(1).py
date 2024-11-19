import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з файлу .csv
file_path = "Data1.csv"
data = pd.read_csv(file_path)

# Фільтрація даних для двох країн
country_1 = "Ukraine"
country_2 = "Albania"

data_country_1 = data[data["Country Name"] == country_1]
data_country_2 = data[data["Country Name"] == country_2]

# Отримання років і значень показника
years = [col.split(" ")[0] for col in data.columns if col.startswith("20")]
values_country_1 = data_country_1.iloc[0, 4:].values.astype(float)
values_country_2 = data_country_2.iloc[0, 4:].values.astype(float)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(years, values_country_1, label=country_1, color="blue", marker="o")
plt.plot(years, values_country_2, label=country_2, color="green", marker="o")

# Підпис осей і графіка
plt.title("Dynamics of Indicator for Two Countries", fontsize=15)
plt.xlabel("Year", fontsize=12, color="red")
plt.ylabel("Indicator Value", fontsize=12, color="red")
plt.legend()
plt.grid(True)

# Відображення графіка
plt.show()
