# # Мини-задание для закрепления

# import math

# def relative_error(approx, exact):
#     return abs(approx - exact) / abs(exact)

# approx_pi = 3.14
# exact_pi = math.pi
# abs_err_pi = abs(approx_pi - exact_pi)
# rel_err_pi = relative_error(approx_pi, exact_pi)

# print("Функция №1")
# print(f"Абсолютная погрешность: {abs_err_pi}")
# print(f"Относительная погрешность: {rel_err_pi}")

# approx_sum = 0.1 + 0.2
# exact_sum = 0.3
# abs_err_sum = abs(approx_sum - exact_sum)
# rel_err_sum = relative_error(approx_sum, exact_sum)

# print("Функция №2")
# print(f"Результат сложения: {approx_sum}")
# print(f"Абсолютная погрешность: {abs_err_sum}")
# print(f"Относительная погрешность: {rel_err_sum}")

# approx_total = 0.0
# for _ in range(1000000):
#     approx_total += 0.1

# exact_total = math.fsum([0.1] * 1000000)
# abs_err_total = abs(approx_total - exact_total)
# rel_err_total = relative_error(approx_total, exact_total)

# print("Функция №3")
# print(f"Обычная сумма: {approx_total}")
# print(f"Точная сумма (fsum): {exact_total}")
# print(f"Абсолютная погрешность: {abs_err_total}")
# print(f"Относительная погрешность: {rel_err_total}")

