import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,10,100) # діапазон значень для х
y=x**(np.sin(10*x)) # визначення функції у(х)

plt.plot(x, y, label='x^(sin(10*x))', color = "pink", linewidth = 4) # побудова графіка

plt.title('Function graph', fontsize=15)   # назва графіка
plt.xlabel('x', fontsize=12, color='purple') # позначення вісі абсцис
plt.ylabel('y', fontsize=12, color='purple') # позначення вісі ординат
plt.legend() # додавання легенди
plt.grid(True) # додавання сітки
plt.show() # відображення графіка