# # Блок №1
# # Задание №1. Задача 1. Сумма массива
import time
import numpy as np

# rng = np.random.default_rng(42)
# a = rng.normal(size=10**6) 

# def loop_sum(arr):
#     s = 0.0
#     for x in arr:
#         s += x
#     return s

# def numpy_sum(arr):
#     return arr.sum()

# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop,  t_loop  = measure(loop_sum,  a)
# r_numpy, t_numpy = measure(numpy_sum, a)

# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")


# # ── Способ 2: NumPy ────────────────────────────────────────
# def numpy_sum(arr):
#     return arr.sum()


# # ── Замер: запускаем 3 раза, берём лучший (минимум) ────────
# def measure(fn, arr, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(arr)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# # ── Сравнение ──────────────────────────────────────────────
# r_loop,  t_loop  = measure(loop_sum,  a)
# r_numpy, t_numpy = measure(numpy_sum, a)

# print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop:.6f}")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy:.6f}")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")


# # Задача №2. Среднее и стандартное отклонение
# import time
# import math
# import numpy as np

# rng = np.random.default_rng(42)
# a = rng.normal(size=10**6) 


# def loop_mean_std(arr):
#     n = len(arr)
#     total = 0.0
#     for x in arr: total += x
#     mean = total / n
#     sq_sum = 0.0
#     for x in arr: sq_sum += (x - mean) ** 2
#     return mean, math.sqrt(sq_sum / n)


# def numpy_mean_std(arr):
#     return arr.mean(), arr.std()


# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# r_loop,  t_loop  = measure(loop_mean_std,  a)
# r_numpy, t_numpy = measure(numpy_mean_std, a)

# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# # Задача №3. Поэлементное преобразование: (y = \sin(x) + x^2).
# import time
# import math
# import numpy as np

# rng = np.random.default_rng(42)
# a = rng.normal(size=10**6) 


# def loop_sin_sq(arr):
#     result = []
#     for x in arr:
#         result.append(math.sin(x) + x * x)
#     return np.array(result)


# def numpy_sin_sq(arr):
#     return np.sin(arr) + arr**2


# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# r_loop,  t_loop  = measure(loop_sin_sq,  a)
# r_numpy, t_numpy = measure(numpy_sin_sq, a)

# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# # Задача 4. Условная замена (clipping)
# import time
# import numpy as np

# rng = np.random.default_rng(42)
# a = rng.normal(size=10**6) 


# def loop_clip(arr):
#     result = []
#     for x in arr:
#         if x < 0:
#             result.append(0.0)
#         elif x > 1:
#             result.append(1.0)
#         else:
#             result.append(x)
#     return np.array(result)


# def numpy_clip(arr):
#     return np.clip(arr, 0, 1)


# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best


# r_loop,  t_loop  = measure(loop_clip,  a)
# r_numpy, t_numpy = measure(numpy_clip, a)

# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

## Блок №2. Агрегации по осям (задачи 5–7)
# Задание №5.

# ── ДАННЫЕ ───────────────────────────────────────────────
# rng = np.random.default_rng(42)
# n = 10**5
# m = rng.normal(size=(n, 10))


# # ── СПОСОБ 1: ЦИКЛ ────────────────────────────────────────
# def loop_sum_rows(mat):
#     result = [0.0] * mat.shape[0]
#     for i in range(mat.shape[0]):
#         s = 0.0
#         for j in range(mat.shape[1]):
#             s += mat[i, j]
#         result[i] = s
#     return result


# # ── СПОСОБ 2: NUMPY ───────────────────────────────────────
# def numpy_sum_rows(mat):
#     return mat.sum(axis=1)


# # ── ЗАМЕР ────────────────────────────────────────────────
# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop,  t_loop  = measure(loop_sum_rows,  m)
# r_numpy, t_numpy = measure(numpy_sum_rows, m)

# sloc_loop = 6
# sloc_numpy = 2

# print("--- Задача №5 ---")
# print(f"цикл:   {t_loop*1000:10.2f} мс   SLOC = {sloc_loop}")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс   SLOC = {sloc_numpy}")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# Задание №6
# ── ДАННЫЕ ───────────────────────────────────────────────
# rng = np.random.default_rng(42)
# n = 10**5
# m = rng.normal(size=(n, 10)) 


# # ── СПОСОБ 1: ЦИКЛ ────────────────────────────────────────
# def loop_norm(mat):
#     n_rows, n_cols = mat.shape
#     # 1. Ищем среднее для каждого столбца
#     means = [0.0] * n_cols
#     for j in range(n_cols):
#         s = 0.0
#         for i in range(n_rows):
#             s += mat[i, j]
#         means[j] = s / n_rows
        
#     # 2. Вычитаем среднее из каждого элемента
#     result = np.zeros_like(mat)
#     for i in range(n_rows):
#         for j in range(n_cols):
#             result[i, j] = mat[i, j] - means[j]
#     return result


# # ── СПОСОБ 2: NUMPY ───────────────────────────────────────
# def numpy_norm(mat):
#     # axis=0 означает "по столбцам". Broadcasting автоматически 
#     # вычтет среднее каждого столбца из всех строк.
#     return mat - mat.mean(axis=0)


# # ── ЗАМЕР ────────────────────────────────────────────────
# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop,  t_loop  = measure(loop_norm,  m)
# r_numpy, t_numpy = measure(numpy_norm, m)

# print("\n--- Задача 6 ---")
# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# Задание №7

# ── ДАННЫЕ ───────────────────────────────────────────────
# rng = np.random.default_rng(42)
# a = rng.normal(size=10**6)


# # ── СПОСОБ 1: ЦИКЛ ────────────────────────────────────────
# def loop_max(arr):
#     max_val = arr[0]
#     max_idx = 0
#     for i in range(1, len(arr)):
#         if arr[i] > max_val:
#             max_val = arr[i]
#             max_idx = i
#     return max_val, max_idx


# # ── СПОСОБ 2: NUMPY ───────────────────────────────────────
# def numpy_max(arr):
#     return arr.max(), arr.argmax()


# # ── ЗАМЕР ────────────────────────────────────────────────
# def measure(fn, x, repeat=3):
#     best = float("inf")
#     result = None
#     for _ in range(repeat):
#         t0 = time.perf_counter()
#         result = fn(x)
#         t1 = time.perf_counter()
#         best = min(best, t1 - t0)
#     return result, best

# r_loop,  t_loop  = measure(loop_max,  a)
# r_numpy, t_numpy = measure(numpy_max, a)

# print("\n--- Задача 7 ---")
# print(f"цикл:   {t_loop*1000:10.2f} мс   (val={r_loop[0]:.4f}, idx={r_loop[1]})")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс   (val={r_numpy[0]:.4f}, idx={r_numpy[1]})")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")

# match = np.isclose(r_loop[0], r_numpy[0]) and (r_loop[1] == r_numpy[1])
# print(f"результаты совпадают: {match}")

# Блок 3. Фильтрация и маски (задачи 8–10)
# Задание №8

# Задание №9

# ── ДАННЫЕ ───────────────────────────────────────────────
# rng = np.random.default_rng(42)
# a = rng.normal(size=10**6) 

# a_loop = a.copy()
# a_np = a.copy()


# # ── СПОСОБ 1: ЦИКЛ ────────────────────────────────────────
# def loop_abs_inplace(arr):
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             arr[i] = -arr[i]
#     return arr


# # ── СПОСОБ 2: NUMPY ───────────────────────────────────────
# def numpy_abs_inplace(arr):
#     arr[arr < 0] *= -1
#     return arr


# # ── ЗАМЕР ────────────────────────────────────────────────

# t0 = time.perf_counter()
# loop_abs_inplace(a_loop)
# t_loop = time.perf_counter() - t0

# t0 = time.perf_counter()
# numpy_abs_inplace(a_np)
# t_numpy = time.perf_counter() - t0

# print("\n--- Задача 9 ---")
# print(f"цикл:   {t_loop*1000:10.2f} мс")
# print(f"NumPy:  {t_numpy*1000:10.2f} мс")
# print(f"ускорение: {t_loop / t_numpy:.1f}×")
# print(f"результаты совпадают: {np.allclose(a_loop, a_np)}")

# Задание №10