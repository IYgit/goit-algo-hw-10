import numpy as np
from scipy.integrate import quad


def f(x):
    return x**2

# Кількість випадкових точок для методу Монте-Карло
num_points = 10000

# Випадкові значення x та y
x_values = np.random.uniform(0, 1, num_points)
y_values = np.random.uniform(0, 1, num_points)

# Обчислення кількості точок, які знаходяться під графіком функції
points_under_curve = sum(1 for x, y in zip(x_values, y_values) if y < f(x))

# Площа під графіком функції
area_under_curve = points_under_curve / num_points

# Аналітичне обчислення визначеного інтеграла за допомогою quad
integral, _ = quad(f, 0, 1)

print("Метод Монте-Карло:", area_under_curve)
print("Аналітичний метод (quad):", integral)
