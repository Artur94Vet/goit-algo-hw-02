'''
Завдання 2. Обчислення визначеного інтеграла

Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.

 📖 Можете обрати функцію на власний розсуд.
Виконаємо побудову графіка.



✂️ Це можна запустити!

import matplotlib.pyplot as plt
import numpy as np

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

1. Обчисліть значення інтеграла функції за допомогою методу Монте-Карло, інакше кажучи, знайдіть площу під цим графіком (сіра зона).

2. Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, шляхом порівняння отриманого результату та аналітичних 
розрахунків або результату виконання функції quad. Зробіть висновки.

'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# --- 1. Визначення функції ---
def f(x):
    return x ** 2

# --- 2. Межі інтегрування ---
a = 0
b = 2

# --- 3. Побудова графіка функції ---
x_vals = np.linspace(-0.5, 2.5, 400)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, 'r', linewidth=2)

# Заповнення області інтегрування
ix = np.linspace(a, b, 100)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Вісь, мітки, межі
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_xlim([x_vals[0], x_vals[-1]])
ax.set_ylim([0, max(y_vals) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графік f(x) = x² на відрізку [0, 2]')
plt.grid()
plt.show()

# --- 4. Метод Монте-Карло ---
N = 100000  # кількість точок
x_rand = np.random.uniform(a, b, N)
fx_rand = f(x_rand)
mean_fx = np.mean(fx_rand)
mc_integral = (b - a) * mean_fx

print("Інтеграл методом Монте-Карло:", mc_integral)

# --- 5. Точне значення інтегралу через quad ---
exact_result, error_est = spi.quad(f, a, b)

print("Аналітичний інтеграл (quad):", exact_result)
print("Абсолютна похибка:", abs(exact_result - mc_integral))
print("Оцінка помилки quad:", error_est)
