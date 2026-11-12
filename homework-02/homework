import math
from decimal import Decimal, getcontext
import time
import numpy as np
import random
import sys

#Блок №1. Обусловленность задачи

print("--- Задача 1 ---")
cond1 = 0.5
print(f"1. sqrt(x): cond = {cond1}")

cond2 = abs(1 / math.log(1.001))
print(f"2. ln(x): cond = {cond2:.1f}")

cond3 = abs(1.000001 / (1.000001 - 1))
print(f"3. x-1: cond = {cond3:.0f}")

cond4 = 0.0
print(f"4. sin(x): cond = {cond4}")
print("Самая опасная: №3 - вычитание близких чисел\n")

print("--- Задача 2 ---")

a = 1 + 1e-8
b = 1.0
da = 1e-9

f = a - b
f_new = (a + da) - b
df = f_new - f

print(f"f = {f}")
print(f"df = {df}")
print(f"Относительная ошибка результата = {df / f * 100:.0f}%")
print("Вывод: ошибка огромная (10-100%), совпадает с теорией.\n")


print("--- Задача 3 ---")
print("eps       сдвиг      отношение")
print("-" * 35)

for eps in [1e-2, 1e-4, 1e-6]:
    shift = math.sqrt(eps)
    print(f"{eps:.0e}    {shift:.4f}     {shift/eps:.0f}")
print("Вывод: сдвиг корня растет как sqrt(eps) -> плохая обусловленность.\n")


print("--- Задача 4 ---")

r = 10.0
area_good = math.pi * r**2
pi_bad = 4 * sum(((-1)**i) / (2*i + 1) for i in range(10))
area_bad = pi_bad * r**2

print(f"Точная площадь:     {area_good:.4f}")
print(f"Площадь (плохой):   {area_bad:.4f}")
print(f"Разница:            {abs(area_good - area_bad):.4f}")
print("Вывод: задача хорошая, a алгоритм плохой.\n")

# Блок №2. Устойчивость алгоритма

print("--- Задача 5 ---")
getcontext().prec = 50 

def solve_equation(a_val, b_val, c_val):
    a, b, c = Decimal(a_val), Decimal(b_val), Decimal(c_val)
    D = b**2 - 4*a*c
    x2_exact = (-b + D.sqrt()) / (2*a)
    x2_bad = (-float(b_val) + float(D.sqrt())) / (2 * a_val)
    x2_good = (2 * float(c_val)) / (-float(b_val) - float(D.sqrt()))
    err_bad = abs((Decimal(str(x2_bad)) - x2_exact) / x2_exact * 100)
    err_good = abs((Decimal(str(x2_good)) - x2_exact) / x2_exact * 100)
    
    return float(x2_exact), float(x2_bad), float(err_bad), float(err_good)

print(f"{'b':>8} | {'Ошибка плохого':>15} | {'Ошибка хорошего':>15}")
print("-" * 45)
for b in [10**8, 10**4, 10**12]:
    exact, bad, err_b, err_g = solve_equation(1, b, 1)
    print(f"{b:>8} | {err_b:>14.2e}% | {err_g:>14.2e}%")

print("\nВывод:")
print("В 'плохом' способе при больших b происходит вычитание двух очень близких чисел,")
print("что приводит к катастрофической потере точности. При b=10^8 ошибка уже огромна.\n")


print("\n--- Задача 6 ---")
getcontext().prec = 50

print(f"{'x':>7} | {'Ошибка плохого':>15} | {'Ошибка хорошего':>15}")
print("-" * 45)

for x in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
    dx = Decimal(str(x))
    exact = (1 - dx.cos()) / (dx**2)
    f_bad = (1 - math.cos(x)) / (x**2)
    f_good = (2 * math.sin(x/2)**2) / (x**2)
    
    err_bad = abs(Decimal(str(f_bad)) - exact) / exact * 100
    err_good = abs(Decimal(str(f_good)) - exact) / exact * 100
    
    print(f"{x:>7.0e} | {float(err_bad):>14.2e}% | {float(err_good):>14.2e}%")

print("\nВывод:")
print("Плохой способ теряет точность из-за вычитания близких чисел (1 - cos x -> 0).")
print("Хороший способ (через sin^2) не имеет этой проблемы и остается точным даже при x=1e-10.\n")


print("\n--- Задача 7 ---")
getcontext().prec = 50
print(f"{'x':>7} | {'Ошибка плохого':>15} | {'Ошибка хорошего':>15}")
print("-" * 45)

for x in [1e4, 1e8, 1e12, 1e14, 1e16]:
    dx = Decimal(str(x))
    exact = (dx + 1).sqrt() - dx.sqrt()
    f_bad = math.sqrt(x + 1) - math.sqrt(x)
    f_good = 1 / (math.sqrt(x + 1) + math.sqrt(x))
    
    err_bad = abs(Decimal(str(f_bad)) - exact) / exact * 100
    err_good = abs(Decimal(str(f_good)) - exact) / exact * 100
    
    print(f"{x:>7.0e} | {float(err_bad):>14.2e}% | {float(err_good):>14.2e}%")

print("\nВывод:")
print("При росте x ошибка 'плохого' способа растет (пропорционально x).")
print("'Хороший' способ (сопряженное выражение) остается точным.\n")


print("\n--- Задача 8 ---")
getcontext().prec = 50

print(f"{'x':>7} | {'Ошибка плохого':>15} | {'Ошибка хорошего':>15}")
print("-" * 45)

for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    dx = Decimal(str(x))
    exact = (1 + dx).ln()
    f_bad = math.log(1 + x) 
    f_good = math.log1p(x)
    if f_bad == 0:
        err_bad_str = "100% (Inf)"
    else:
        err_bad = abs(Decimal(str(f_bad)) - exact) / exact * 100
        err_bad_str = f"{float(err_bad):.2e}%"
        
    err_good = abs(Decimal(str(f_good)) - exact) / exact * 100
    
    print(f"{x:>7.0e} | {err_bad_str:>15} | {float(err_good):>14.2e}%")

print("\nВывод:")
print("Функция math.log1p(x) специально создана для вычисления ln(1+x) при малых x.")
print("Она внутри использует ряды Тейлора, обходя вычитание (1+x - 1),")
print("которое в обычном math.log(1+x) уничтожает точность. При x=1e-16")
print("обычный способ вообще дает 0 (так как 1 + 1e-16 округляется до 1.0).")
print("Аналогично, math.expm1(x) = exp(x) - 1 и math.hypot(x, y) = sqrt(x^2+y^2)")
print("решают аналогичные проблемы потери точности.\n")

print("--- Задача 9 ---")
getcontext().prec = 50
def sum_loop(arr):
    s = 0.0
    for x in arr: s += x
    return s
def sum_builtin(arr):
    return sum(arr)
def sum_fsum(arr):
    return math.fsum(arr)
print(f"{'n':>7} | {'Ошибка цикла':>15} | {'Ошибка sum':>15} | {'Ошибка fsum':>15}")
print("-" * 65)

for n in [10**5, 10**6, 10**7]:
    arr = [1.0 / k for k in range(1, n + 1)]
    exact = sum(Decimal(1) / Decimal(k) for k in range(1, n + 1))
    
    s_loop = sum_loop(arr)
    s_builtin = sum_builtin(arr)
    s_fsum = sum_fsum(arr)
    err_loop = abs((Decimal(str(s_loop)) - exact) / exact) * 100
    err_builtin = abs((Decimal(str(s_builtin)) - exact) / exact) * 100
    err_fsum = abs((Decimal(str(s_fsum)) - exact) / exact) * 100
    
    print(f"{n:>7} | {float(err_loop):>14.2e}% | {float(err_builtin):>14.2e}% | {float(err_fsum):>14.2e}%")

print("\nВывод:")
print("Наивный цикл накапливает ошибку, так как прибавляет очень маленькие числа к уже большим.")
print("Ошибка > 10^-9% достигается уже при n = 10^6.")
print("Функция math.fsum() использует алгоритм Кэхана (компенсацию ошибок) и остается точной.\n")

# Блок 3. Корректная постановка эксперимента

import math
import numpy as np
from decimal import Decimal, getcontext

print("\n--- Задача 10 ---")
print("Функция: f(x) = (1 - cos(x)) / x^2, при x = 1e-6\n")
print("а) Меняем x (фиксируем алгоритм - плохой):")
print(f"{'x':>8} | {'Ошибка, %':>15}")
for x in [1e-2, 1e-4, 1e-6, 1e-8]:
    dx = Decimal(str(x))
    exact = (1 - dx.cos()) / (dx**2)
    res = (1 - math.cos(x)) / (x**2)
    err = abs(Decimal(str(res)) - exact) / exact * 100
    print(f"{x:>8.0e} | {float(err):>14.2e}")

print("\nб) Фиксируем x=1e-6 (влияние машинной точности float32 vs float64):")
x_val = 1e-6
dx = Decimal(str(x_val))
exact = (1 - dx.cos()) / (dx**2)
x32 = np.float32(x_val)
res32 = (1 - np.cos(x32)) / (x32**2)
err32 = abs(Decimal(str(res32)) - exact) / exact * 100
print(f"Float32: ошибка = {float(err32):.2e}%")
print(f"Float64: ошибка = {float(err32*0 + (Decimal(str((1 - math.cos(x_val)) / (x_val**2))) - exact) / exact * 100):.2e}%")

print("\nв) Фиксируем x=1e-6 (влияние алгоритма - плохой vs хороший):")
res_bad = (1 - math.cos(x_val)) / (x_val**2)
res_good = (2 * math.sin(x_val/2)**2) / (x_val**2)
err_bad = abs(Decimal(str(res_bad)) - exact) / exact * 100
err_good = abs(Decimal(str(res_good)) - exact) / exact * 100
print(f"Плохой алгоритм (1-cos): {float(err_bad):.2e}%")
print(f"Хороший алгоритм (sin^2): {float(err_good):.2e}%")

print("\nВывод:")
print("1. Обусловленность задачи: при уменьшении x ошибка 'плохого' алгоритма растет.")
print("2. Машинная точность: переход на float32 увеличивает ошибку на несколько порядков.")
print("3. Устойчивость алгоритма: замена на тригонометрическое тождество убирает ошибку.\n")


print("--- Задача 11 ---")

def area_approx1(r):
    pi = 4 * sum(((-1)**i) / (2*i + 1) for i in range(5))
    return pi * r**2

def area_approx2(r):
    pi = 3.14159
    return pi * r**2

r = 10.0
res1 = area_approx1(r)
res2 = area_approx2(r)
exact = math.pi * r**2

print(f"Алгоритм 1: {res1}")
print(f"Алгоритм 2: {res2}")
print(f"Они равны друг другу (res1 == res2)? -> {res1 == res2}")
print(f"Эталон (math.pi): {exact}")
print(f"Ошибка Алгоритма 1: {abs(res1 - exact):.4f}")
print(f"Ошибка Алгоритма 2: {abs(res2 - exact):.4f}")

print("\nВывод:")
print("Два разных алгоритма могут дать одинаковый (или очень близкий) результат,")
print("но оба будут неправильными. Сравнение float с float без эталона опасно:")
print("они могут совпасть в своей ошибке. Всегда нужен независимый точный эталон.\n")


print("--- Задача 13 ---")
print(f"Версия Python: {sys.version.split()[0]}")
print(f"Версия NumPy:  {np.__version__}\n")

def run_experiment(seed):
    random.seed(seed)
    arr_rand = [random.random() for _ in range(10**5)]
    
    rng = np.random.default_rng(seed)
    arr_np = rng.random(10**5)
    
    sum_builtin_rand = sum(arr_rand)
    sum_fsum_rand = math.fsum(arr_rand)
    sum_np_rand = np.sum(arr_rand)
    
    sum_builtin_np = sum(arr_np)
    sum_fsum_np = math.fsum(arr_np)
    sum_np_np = np.sum(arr_np)
    
    return (sum_builtin_rand, sum_fsum_rand, sum_np_rand, 
            sum_builtin_np, sum_fsum_np, sum_np_np)

res1 = run_experiment(42)
res2 = run_experiment(42)
res3 = run_experiment(43)

print(f"С seed=42 (1-й раз): {res1[:3]}")
print(f"С seed=42 (2-й раз): {res2[:3]}")
print(f"Результаты совпадают: {res1 == res2}\n")

print(f"С seed=43 (1-й раз): {res3[:3]}")
print(f"Результаты НЕ совпадают с seed=42: {res1 != res3}")

print("\nВывод:")
print("При фиксированном seed результаты полностью воспроизводятся.")
print("При смене seed данные меняются, и результаты сумм расходятся.")
print("Без фиксации seed эксперимент невозможно повторить - он невоспроизводим.\n")

print("\n--- Задача 14 ---")
values = [
    ("Большие (1e300)", 1e300),
    ("Маленькие (1e-300)", 1e-300),
    ("Ноль", 0.0),
    ("Денормализованные (5e-324)", 5e-324),
    ("Бесконечность (inf)", float('inf')),
    ("Не число (nan)", float('nan'))
]

print(f"{'Тип значения':<30} | {'Сумма (sum)':>15} | {'Сумма (fsum)':>15}")
print("-" * 70)

for name, val in values:
    arr = [val] * 10 
    s_builtin = sum(arr)
    try:
        s_fsum = math.fsum(arr)
    except Exception as e:
        s_fsum = f"Ошибка: {e}"
        
    print(f"{name:<30} | {str(s_builtin):>15} | {str(s_fsum):>15}")
mixed = [float('inf'), float('-inf')]
print(f"\nСмесь +inf и -inf: sum={sum(mixed)}, fsum={math.fsum(mixed)}")
print("\nВывод:")
print("1. nan 'отравляет' любую сумму: и sum, и fsum дают nan.")
print("2. inf в sum дает inf, а в fsum вызывает ошибку (ValueError), так как fsum")
print("   пытается использовать компенсацию, которая невозможна с бесконечностями.")
print("3. Денормализованные числа (очень маленькие) могут теряться при sum, если")
print("   к ним прибавить что-то большее, но fsum сохраняет их точнее.\n")

