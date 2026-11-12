# Блок №1
# Задание №1. Задача 1. Сумма массива
import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=10**6) 

def loop_sum(arr):
    s = 0.0
    for x in arr:
        s += x
    return s

def numpy_sum(arr):
    return arr.sum()

def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best

r_loop,  t_loop  = measure(loop_sum,  a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")


# ── Способ 2: NumPy ────────────────────────────────────────
def numpy_sum(arr):
    return arr.sum()


# ── Замер: запускаем 3 раза, берём лучший (минимум) ────────
def measure(fn, arr, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(arr)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


# ── Сравнение ──────────────────────────────────────────────
r_loop,  t_loop  = measure(loop_sum,  a)
r_numpy, t_numpy = measure(numpy_sum, a)

print(f"цикл:   {t_loop*1000:10.2f} мс   результат = {r_loop:.6f}")
print(f"NumPy:  {t_numpy*1000:10.2f} мс   результат = {r_numpy:.6f}")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.isclose(r_loop, r_numpy)}")


# Задача №2. Среднее и стандартное отклонение
import time
import math
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=10**6) 


def loop_mean_std(arr):
    n = len(arr)
    total = 0.0
    for x in arr: total += x
    mean = total / n
    sq_sum = 0.0
    for x in arr: sq_sum += (x - mean) ** 2
    return mean, math.sqrt(sq_sum / n)


def numpy_mean_std(arr):
    return arr.mean(), arr.std()


def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


r_loop,  t_loop  = measure(loop_mean_std,  a)
r_numpy, t_numpy = measure(numpy_mean_std, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# Задача №3. Поэлементное преобразование: (y = \sin(x) + x^2).
import time
import math
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=10**6) 


def loop_sin_sq(arr):
    result = []
    for x in arr:
        result.append(math.sin(x) + x * x)
    return np.array(result)


def numpy_sin_sq(arr):
    return np.sin(arr) + arr**2


def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


r_loop,  t_loop  = measure(loop_sin_sq,  a)
r_numpy, t_numpy = measure(numpy_sin_sq, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")

# Задача 4. Условная замена (clipping)
import time
import numpy as np

rng = np.random.default_rng(42)
a = rng.normal(size=10**6) 


def loop_clip(arr):
    result = []
    for x in arr:
        if x < 0:
            result.append(0.0)
        elif x > 1:
            result.append(1.0)
        else:
            result.append(x)
    return np.array(result)


def numpy_clip(arr):
    return np.clip(arr, 0, 1)


def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


r_loop,  t_loop  = measure(loop_clip,  a)
r_numpy, t_numpy = measure(numpy_clip, a)

print(f"цикл:   {t_loop*1000:10.2f} мс")
print(f"NumPy:  {t_numpy*1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")