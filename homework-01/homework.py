import math

#Задача №1
print("--- Задача №1 ---")
a = 81.359
delta = 0.04
print("Верные цифры: 8, 1, 3. Их количество = 3")
print()

#Задача №2
print("--- Задача №2 ---")
x = 35.49
dx = 0.002
y = 1.27
dy = 0.003
sum_val = x + y
sum_err = dx + dy
print(f"Сумма: {sum_val} ± {sum_err}")
diff_val = x - y
diff_err = dx + dy
print(f"Разность: {round(diff_val, 3)} ± {diff_err}") # округлили для красоты
print()

#Задача №3
print("--- Задача №3 ---")
approx = 1.2188
exact = (2/3) * (2 * math.sqrt(2) - 1)
abs_err = abs(exact - approx)
rel_err = (abs_err / exact) * 100
print(f"Точное значение: {exact:.6f}")
print(f"Абсолютная погрешность: {abs_err:.6f}")
print(f"Относительная погрешность: {rel_err:.4f}%")