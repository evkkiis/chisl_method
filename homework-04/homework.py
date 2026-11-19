# Домашнее задание: 15 задач на отработку темы «NumPy: 
# массивы, формы, типы данных и базовые операции»

# Задача №1. Инвентаризация массива.
# Создайте массив np.arange(60).reshape(3, 4, 5). 
# Выведите shape, ndim, size, dtype, strides, C_CONTIGUOUS. 
# Объясните в 2–3 предложениях, что означает каждое число в strides и почему size = 60.

import numpy as np

arr = np.arange(60).reshape(3, 4, 5)

print(f"shape: {arr.shape}")
print(f"ndim: {arr.ndim}")
print(f"size: {arr.size}")
print(f"dtype: {arr.dtype}")
print(f"strides: {arr.strides}")
print(f"C_CONTIGUOUS: {arr.flags['C_CONTIGUOUS']}")

# Задача 2. int vs float — тихая ловушка.
# Создайте a = np.array([1, 2, 3, 4]). 
# Выполните a / 2, a // 2, a / 2.0, a.dtype, (a / 2).dtype, (a // 2).dtype. 
# Затем создайте b = np.array([1, 2, 3], dtype=np.int8), прибавьте 127 и выведите результат и dtype. 
# Объясните: почему a / 2 не меняет a, а b + 127 даёт странный результат, и почему NumPy не падает с ошибкой.

a = np.array([1, 2, 3, 4])
print("a / 2:", a / 2)
print("a // 2:", a // 2)
print("a / 2.0:", a / 2.0)
print("a.dtype:", a.dtype)
print("(a / 2).dtype:", (a / 2).dtype)
print("(a // 2).dtype:", (a // 2).dtype)

b = np.array([1, 2, 3], dtype=np.int8)
print("b + 127:", b + 127)
print("dtype of b + 127:", (b + 127).dtype)

# Задача 3. float32 vs float64 — реальная точность.
# Сравните np.float32(0.1) - np.float32(0.1) не поможет; сделайте иначе: float(np.float32(0.1)) - 0.1 и float(np.float64(0.1)) - 0.1. 
# Выведите оба числа в repr и в :.20e. Посчитайте, во сколько раз ошибка float32 больше ошибки float64. 
# Сделайте вывод: в каких задачах численных методов float32 допустим, а в каких — нет.

err_32 = float(np.float32(0.1)) - 0.1
err_64 = float(np.float64(0.1)) - 0.1
print(f"Ошибка float32: {err_32:g} | в exp: {err_32:.20e}")
print(f"Ошибка float64: {err_64:g} | в exp: {err_64:.20e}")

ratio = abs(err_32) / abs(err_64)
print(f"Ошибка float32 больше в {ratio:.2e} раз")

# Задача 4. Явный dtype при создании.
# Создайте четыре массива одинакового размера (2, 3):
# np.zeros с dtype=np.float64;
# np.zeros с dtype=np.float32;
# np.ones с dtype=np.int16;
# np.full со значением 7 и dtype=np.uint8.

z64 = np.zeros((2, 3), dtype=np.float64)
z32 = np.zeros((2, 3), dtype=np.float32)
o16 = np.ones((2, 3), dtype=np.int16)
f7 = np.full((2, 3), 7, dtype=np.uint8)

for name, arr in [("float64", z64), ("float32", z32), ("int16", o16), ("uint8", f7)]:
    print(f"{name}: dtype={arr.dtype}, nbytes={arr.nbytes}")

size_elements = 1000 * 1000
bytes_f64 = size_elements * 8
bytes_f32 = size_elements * 4 
savings_mb = (bytes_f64 - bytes_f32) / (1024 ** 2)
print(f"Экономия памяти с float32 на массиве (1000, 1000): {savings_mb:.2f} МБ")

# Блок 2. reshape, ravel, flatten, .T, newaxis (задачи 5–8)

# Задача 5. Цепочка reshape.
# Создайте a = np.arange(24). Преобразуйте последовательно в (4, 6), (2, 3, 4), (2, 2, 6), (24,). После каждого шага выведите shape и проверьте через np.array_equal(a, текущий.ravel()), что данные не потерялись. Объясните: почему reshape обычно не копирует данные и когда он вынужден скопировать.

a = np.arange(24)
shapes = [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]

for s in shapes:
    a = a.reshape(s)
    is_equal = np.array_equal(np.arange(24), a.ravel())
    print(f"Новая форма: {a.shape}, данные сохранены: {is_equal}")

# Задача 6. flatten vs ravel — копия или view.
# Создайте M = np.arange(12).reshape(3, 4). Получите f = M.flatten() и r = M.ravel(). Выведите f.base is None, r.base is M (или r.base is not None). Измените f[0] = 999 и r[1] = 888 — проверьте, изменился ли M в каждом случае. Сделайте вывод: когда использовать ravel, когда flatten.

M = np.arange(12).reshape(3, 4)

f = M.flatten()
r = M.ravel()

print(f"f.base is None: {f.base is None}")
print(f"r.base is M: {r.base is M} (или r.base is not None: {r.base is not None})")

f[0] = 999
r[1] = 888

print("\nМассив M после изменений:")
print(M)

# Задача 7. newaxis, squeeze, транспонирование.
# Создайте v = np.arange(5). Получите:
# v[:, None] — форма?
# v[None, :] — форма?
# np.squeeze(v[:, None]) — форма?
# np.arange(6).reshape(2, 3).T — форма и содержимое.
# Для каждой операции объясните одной строкой, что произошло. Затем вычислите v[:, None] + v[None, :] — какая форма получилась и что это за матрица (подсказка: таблица умножения).


# Задача 8. Транспонирование без копии.
# Создайте A = np.arange(6).reshape(2, 3). Получите B = A.T. Проверьте B.base is A (или B.base is not None). Измените B[0, 1] = 999 — изменился ли A? Сделайте вывод: почему .T — view, а не копия, и как это связано с strides.

A = np.arange(6).reshape(2, 3)
B = A.T

print(f"B.base is A: {B.base is A}")
print(f"B.base is not None: {B.base is not None}")
B[0, 1] = 999

print("\nМассив A после изменения B:")
print(A)

# Блок 3. Операции, агрегации, axis (задачи 9–11)

# Задача 9. Поэлементно vs матричное.
# Создайте A = np.arange(6).reshape(2, 3) и B = np.arange(6).reshape(3, 2). Выполните A @ B, A.T @ B.T, A * A. Выведите формы и значения. Объясните: почему A * B даёт ошибку (или работает?) и в чём разница между * и @. Приведите пример, когда * и @ дают одинаковый результат (подсказка: диагональная матрица).


# Задача 10. axis=0 vs axis=1.
# Создайте M = np.arange(12).reshape(3, 4). Вычислите M.sum(axis=0), M.sum(axis=1), M.mean(axis=0), M.mean(axis=1), M.argmax(axis=0), M.argmax(axis=1). Для каждой операции объясните одной строкой: по какой оси «свернули» и что означает результат. Проверьте на маленьком примере, что M.sum(axis=0) — это сумма по столбцам, а не по строкам.

M = np.arange(12).reshape(3, 4)
print(f"M:\n{M}\n")

print(f"M.sum(axis=0): {M.sum(axis=0)}")
print(f"M.sum(axis=1): {M.sum(axis=1)}")
print(f"M.mean(axis=0): {M.mean(axis=0)}")
print(f"M.mean(axis=1): {M.mean(axis=1)}")
print(f"M.argmax(axis=0): {M.argmax(axis=0)}")
print(f"M.argmax(axis=1): {M.argmax(axis=1)}\n")

small = np.array([[1, 2], [3, 4]])
print(f"Маленький массив:\n{small}")
print(f"Сумма по axis=0: {small.sum(axis=0)}")

# Задача 11. keepdims и broadcasting.
# Создайте X = np.random.default_rng(42).normal(size=(5, 3)). Вычислите X.mean(axis=0) (форма (3,)) и X.mean(axis=0, keepdims=True) (форма (1, 3)). Выполните X - X.mean(axis=0) и X - X.mean(axis=0, keepdims=True) — обе формы должны дать (5, 3). Затем посчитайте X.std(axis=1) без keepdims и с ним, и нормируйте строки: (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True). Убедитесь, что средние по строкам ≈ 0, std по строкам ≈ 1. Объясните, зачем нужен keepdims.

X = np.random.default_rng(42).normal(size=(5, 3))
print(f"Исходная форма X: {X.shape}")

mean_0 = X.mean(axis=0)
mean_0_keep = X.mean(axis=0, keepdims=True)

print(f"X.mean(axis=0) shape: {mean_0.shape}")
print(f"X.mean(axis=0, keepdims=True) shape: {mean_0_keep.shape}\n")

res_no_keep = X - mean_0
res_keep = X - mean_0_keep
print(f"Форма X - X.mean(axis=0): {res_no_keep.shape}")
print(f"Форма X - X.mean(axis=0, keepdims=True): {res_keep.shape}\n")

X_std = X.std(axis=1, keepdims=True)
X_mean = X.mean(axis=1, keepdims=True)
X_norm = (X - X_mean) / X_std

print(f"Среднее по строкам после нормировки (должно быть ~0):\n{X_norm.mean(axis=1)}")
print(f"Std по строкам после нормировки (должно быть ~1):\n{X_norm.std(axis=1)}")

# Блок 4. Индексация, выборки, broadcasting (задачи 12–15)

print("="*60)
print("БЛОК 1. ndarray, shape, dtype (Задачи 1-4)")
print("="*60)

# Задача №1
print("\n--- Задача 1: Инвентаризация массива ---")
arr1 = np.arange(60).reshape(3, 4, 5)
print(f"shape: {arr1.shape}, ndim: {arr1.ndim}, size: {arr1.size}")
print(f"dtype: {arr1.dtype}, strides: {arr1.strides}")
print(f"C_CONTIGUOUS: {arr1.flags['C_CONTIGUOUS']}")
print("Пояснение: strides показывают смещение в байтах для перехода по осям. size = 3*4*5 = 60.")

# Задача №2
print("\n--- Задача 2: int vs float ---")
a2 = np.array([1, 2, 3, 4])
print(f"a / 2 = {a2 / 2} (dtype: {(a2 / 2).dtype})")
print(f"a // 2 = {a2 // 2} (dtype: {(a2 // 2).dtype})")
print(f"a / 2.0 = {a2 / 2.0}")
b2 = np.array([1, 2, 3], dtype=np.int8)
print(f"b + 127 = {b2 + 127} (dtype: {(b2 + 127).dtype})")
print("Пояснение: деление / всегда дает float. int8 переполняется: 3+127=130 -> -126.")

# Задача №3
print("\n--- Задача 3: float32 vs float64 ---")
err_32 = float(np.float32(0.1)) - 0.1
err_64 = float(np.float64(0.1)) - 0.1
print(f"Ошибка float32: {err_32:.20e}")
print(f"Ошибка float64: {err_64:.20e}")
print(f"Отношение ошибок: {abs(err_32)/abs(err_64):.2e}")
print("Пояснение: float32 быстрее и экономнее, но менее точен. Допустим в ML/графике, недопустим в фин. расчетах/ЧМ.")

# Задача №4
print("\n--- Задача 4: Явный dtype ---")
arrays4 = [
    ("float64", np.zeros((2, 3), dtype=np.float64)),
    ("float32", np.zeros((2, 3), dtype=np.float32)),
    ("int16", np.ones((2, 3), dtype=np.int16)),
    ("uint8", np.full((2, 3), 7, dtype=np.uint8))
]
for name, arr in arrays4:
    print(f"{name}: nbytes={arr.nbytes}")
print("Экономия float32 vs float64 на (1000,1000): 4 МБ (50%).")


print("\n" + "="*60)
print("БЛОК 2. Изменение формы (Задачи 5-8)")
print("="*60)

# Задача №5
print("\n--- Задача 5: Цепочка reshape ---")
a5 = np.arange(24)
for s in [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]:
    a5 = a5.reshape(s)
    print(f"shape: {a5.shape}, данные целы: {np.array_equal(np.arange(24), a5.ravel())}")
print("Пояснение: reshape не копирует данные, если порядок элементов в памяти (C-порядок) позволяет.")

# Задача №6
print("\n--- Задача 6: flatten vs ravel ---")
M6 = np.arange(12).reshape(3, 4)
f6, r6 = M6.flatten(), M6.ravel()
print(f"f.base is None: {f6.base is None}, r.base is not None: {r6.base is not None}")
f6[0] = 999
r6[1] = 888
print(f"M6 после изменений (изменился только от r): \n{M6}")
print("Пояснение: flatten() всегда копирует, ravel() возвращает view, если возможно.")

# Задача №7
print("\n--- Задача 7: newaxis, squeeze, транспонирование ---")
v7 = np.arange(5)
print(f"v[:, None].shape: {v7[:, None].shape}")
print(f"v[None, :].shape: {v7[None, :].shape}")
print(f"np.squeeze(v[:, None]).shape: {np.squeeze(v7[:, None]).shape}")
A7 = np.arange(6).reshape(2, 3)
print(f"A.T.shape: {A7.T.shape}")
matrix_sum = v7[:, None] + v7[None, :]
print(f"v[:, None] + v[None, :] shape: {matrix_sum.shape}")
print("Пояснение: newaxis добавляет ось, squeeze удаляет, .T меняет оси местами. Сложение дает таблицу (матрицу) размером 5x5.")

# Задача №8
print("\n--- Задача 8: Транспонирование без копии ---")
A8 = np.arange(6).reshape(2, 3)
B8 = A8.T
print(f"B.base is not None: {B8.base is not None}")
B8[0, 1] = 999
print(f"A8 после изменения B8:\n{A8}")
print("Пояснение: .T создает view, меняя strides. Изменения в B отражаются на A.")


print("\n" + "="*60)
print("БЛОК 3. Операции и оси (Задачи 9-11)")
print("="*60)

# Задача №9
print("\n--- Задача 9: Поэлементно vs матричное ---")
A9, B9 = np.arange(6).reshape(2, 3), np.arange(6).reshape(3, 2)
print(f"A @ B:\n{A9 @ B9}")
try:
    A9 * B9
except ValueError as e:
    print(f"A * B выдает ошибку: {e}")
D9, E9 = np.array([[1, 0], [0, 2]]), np.array([[3, 0], [0, 4]])
print(f"Диагональные матрицы: D*E == D@E -> {np.array_equal(D9*E9, D9@E9)}")
print("Пояснение: * поэлементное (нужны одинаковые формы), @ матричное. Для диагональных совпадают.")

# Задача №10
print("\n--- Задача 10: axis=0 vs axis=1 ---")
M10 = np.arange(12).reshape(3, 4)
print(f"M.sum(axis=0): {M10.sum(axis=0)} (свернули по строкам, сумма по столбцам)")
print(f"M.sum(axis=1): {M10.sum(axis=1)} (свернули по столбцам, сумма по строкам)")

# Задача №11
print("\n--- Задача 11: keepdims и broadcasting ---")
X11 = np.random.default_rng(42).normal(size=(5, 3))
print(f"X.mean(axis=0).shape: {X11.mean(axis=0).shape}")
print(f"X.mean(axis=0, keepdims=True).shape: {X11.mean(axis=0, keepdims=True).shape}")
X_norm11 = (X11 - X11.mean(axis=1, keepdims=True)) / X11.std(axis=1, keepdims=True)
print(f"Среднее по строкам после нормировки: {np.round(X_norm11.mean(axis=1), 5)}")
print("Пояснение: keepdims сохраняет размерность 1 для корректного broadcasting.")


print("\n" + "="*60)
print("БЛОК 4. Представления и индексация (Задачи 12-14)")
print("="*60)

# Задача №12
print("\n--- Задача 12: Срез --- view, не копия ---")
a12 = np.arange(10)
b12 = a12[2:5]
b12[0] = 999
print(f"a после изменения view-среза: {a12}")
c12 = a12[2:5].copy()
c12[0] = -1
print(f"a после изменения копии: {a12}")
print("Пояснение: срез создает view. Для независимости нужен .copy().")

# Задача №13
print("\n--- Задача 13: Булева маска и fancy indexing ---")
a13 = np.random.default_rng(0).normal(size=20)
print(f"a[a > 0] кол-во: {len(a13[a13 > 0])}")
print(f"a[(a > -1) & (a < 1)] кол-во: {len(a13[(a13 > -1) & (a13 < 1)])}")
print(f"a[[0, 5, 10, 15]]: {a13[[0, 5, 10, 15]]}")
print(f"Выбросы a[np.abs(a) > 2]: {a13[np.abs(a13) > 2]}")
a13[a13 < 0] = 0
print(f"После a[a < 0] = 0: {a13}")
print("Пояснение: скобки в булевых масках обязательны из-за приоритета операторов.")

# Задача №14
print("\n--- Задача 14: Broadcasting в реальной задаче ---")
X14 = np.random.default_rng(1).normal(size=(100, 3))
mean14, std14 = X14.mean(axis=0), X14.std(axis=0)
X_norm14 = (X14 - mean14) / std14
print(f"Проверка среднего: {np.allclose(X_norm14.mean(axis=0), 0)}")
print(f"Проверка std: {np.allclose(X_norm14.std(axis=0), 1)}")
D14 = np.sqrt(((X_norm14[:, np.newaxis, :] - X_norm14[np.newaxis, :, :]) ** 2).sum(axis=-1))
print(f"Матрица расстояний D.shape: {D14.shape}")
print(f"Диагональ = 0: {np.allclose(np.diag(D14), 0)}, Симметрична: {np.allclose(D14, D14.T)}")
print("Пояснение: broadcasting позволяет векторизовать вычисление попарных расстояний без циклов.")


print("\n" + "="*60)
print("ИТОГОВЫЙ ВЫВОД")
print("="*60)
print("""
1. Операции copy() потребовались при необходимости получить независимый массив (flatten(), .copy() для срезов), чтобы избежать случайного изменения оригинала.
2. Broadcasting сработал при нормировке матриц (вычитание вектора средних из матрицы), при создании таблицы сложения через newaxis и при вычислении попарных расстояний.
3. Ошибки формы возникали при попытке поэлементного умножения матриц разных форм (A * B) из-за несовместимости (2,3) и (3,2) по правилам вещания.
""")