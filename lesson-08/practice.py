# TASK 1
import math
import matplotlib.pyplot as plt

f1 = lambda x: x**3 - 2*x + 2
df1 = lambda x: 3*x**2 - 2

def newton(f, df, x0, eps=1e-12, max_iter=100):
    journal = []
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, journal, "zero_derivative"
        x_new = x - fx / dfx
        journal.append({
            "iter": k,
            "x": x,
            "f(x)": fx,
            "f'(x)": dfx,
            "x_new": x_new,
            "step": abs(x_new - x),
        })
        if abs(x_new - x) < eps or abs(fx) < eps:
            return x_new, journal, "ok"
        x = x_new
    return x, journal, "max_iter"

def secant(f, x0, x1, eps=1e-12, max_iter=100):

    journal = []
    x_prev, x_curr = x0, x1
    f_prev, f_curr = f(x_prev), f(x_curr)
    for k in range(1, max_iter + 1):
        if f_curr - f_prev == 0:
            return x_curr, journal, "zero_denominator"
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        journal.append({
            "iter": k,
            "x_prev": x_prev,
            "x_curr": x_curr,
            "f_curr": f_curr,
            "x_new": x_new,
            "step": abs(x_new - x_curr),
        })
        if abs(x_new - x_curr) < eps or abs(f_curr) < eps:
            return x_new, journal, "ok"
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_new
        f_curr = f(x_curr)
    return x_curr, journal, "max_iter"

def print_journal_newton(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x':>14} | {'f(x)':>14} | {'f\'(x)':>14} | {'war':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x']:>14.10f} | {row['f(x)']:>14.3e} | "
              f"{row['f\'(x)']:>14.3e} | {row['step']:>10.2e}")

def print_journal_secant(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x_prev':>14} | {'x_curr':>14} | {'f_curr':>14} | {'war':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.10f} | "
              f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}")

def bisection(f, a, b, eps=1e-12, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Нет смены знака")
    c = (a + b) / 2
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) < eps:
            return c, k
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    return c, k

xs = [i/100 for i in range(-300, 301)]
ys = [f1(x) for x in xs]
plt.figure(figsize=(7, 4))
plt.plot(xs, ys)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)
plt.title("f(x) = x³ − 2x + 2 на [−3, 3]")
plt.show()

root_n0, jn0, st_n0 = newton(f1, df1, x0=0.0, eps=1e-12, max_iter=10)
print_journal_newton(jn0, "Ньютон: f(x) = x³ − 2x + 2, x₀ = 0")
print(f"статус = {st_n0}, итераций: {len(jn0)}")

root_n, jn, st_n = newton(f1, df1, x0=-2.0, eps=1e-12)
print_journal_newton(jn, "Ньютон: f(x) = x³ − 2x + 2, x₀ = −2")
print(f"корень = {root_n:.12f}, итераций: {len(jn)}")

root_s, js, st_s = secant(f1, x0=-2.0, x1=-1.0, eps=1e-12)
print_journal_secant(js, "Секущие: f(x) = x³ − 2x + 2, x₀ = −2, x₁ = −1")
print(f"корень = {root_s:.12f}, итераций: {len(js)}")

root_b, n_b = bisection(f1, -2.0, -1.0, eps=1e-12)
print(f"\nБисекция на [−2, −1]: корень = {root_b:.12f}, итераций: {n_b}")

print(f"\n{'Метод':<12} | {'Старт':<16} | {'Корень':<18} | {'Итераций':>9}")
print("-" * 65)
print(f"{'Ньютон':<12} | {'x₀ = 0':<16} | {'—':<18} | {len(jn0):>9}")
print(f"{'Ньютон':<12} | {'x₀ = −2':<16} | {root_n:<18.12f} | {len(jn):>9}")
print(f"{'Секущие':<12} | {'−2, −1':<16} | {root_s:<18.12f} | {len(js):>9}")
print(f"{'Бисекция':<12} | {'[−2, −1]':<16} | {root_b:<18.12f} | {n_b:>9}")


#TASK 2
def make_f(k):
    return lambda x: math.exp(x) - k*x

def make_df(k):
    return lambda x: math.exp(x) - k

def newton(f, df, x0, eps=1e-12, max_iter=100):

    journal = []
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, journal, "zero_derivative"
        x_new = x - fx / dfx
        journal.append({
            "iter": k,
            "x": x,
            "f(x)": fx,
            "f'(x)": dfx,
            "x_new": x_new,
            "step": abs(x_new - x),
        })
        if abs(x_new - x) < eps or abs(fx) < eps:
            return x_new, journal, "ok"
        x = x_new
    return x, journal, "max_iter"

def secant(f, x0, x1, eps=1e-12, max_iter=100):

    journal = []
    x_prev, x_curr = x0, x1
    f_prev, f_curr = f(x_prev), f(x_curr)
    for k in range(1, max_iter + 1):
        if f_curr - f_prev == 0:
            return x_curr, journal, "zero_denominator"
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        journal.append({
            "iter": k,
            "x_prev": x_prev,
            "x_curr": x_curr,
            "f_curr": f_curr,
            "x_new": x_new,
            "step": abs(x_new - x_curr),
        })
        if abs(x_new - x_curr) < eps or abs(f_curr) < eps:
            return x_new, journal, "ok"
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_new
        f_curr = f(x_curr)
    return x_curr, journal, "max_iter"

def print_journal_newton(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x':>14} | {'f(x)':>14} | {'f\'(x)':>14} | {'war':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x']:>14.10f} | {row['f(x)']:>14.3e} | "
              f"{row['f\'(x)']:>14.3e} | {row['step']:>10.2e}")

def print_journal_secant(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x_prev':>14} | {'x_curr':>14} | {'f_curr':>14} | {'war':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.10f} | "
              f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}")

def bisection(f, a, b, eps=1e-12, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Нет смены знака")
    c = (a + b) / 2
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) < eps:
            return c, k
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    return c, k

f1 = make_f(1)
df1 = make_df(1)
print(f"\n1. k = 1: f(x) = e^x - x, min f(x) = {f1(0):.6f} > 0, корней нет")

k_e = math.e
f_e = make_f(k_e)
df_e = make_df(k_e)
print(f"\n2. k = e:")
print(f"f(1) = {f_e(1):.3e}, f'(1) = {df_e(1):.3e}")
root_ne, jne, st_ne = newton(f_e, df_e, x0=1.0, eps=1e-12)
print(f"Ньютон x0=1: статус = {st_ne}, итераций: {len(jne)}")
root_se, jse, st_se = secant(f_e, 0.9, 1.1, eps=1e-12)
print(f"Секущие 0.9, 1.1: статус = {st_se}, итераций: {len(jse)}")
try:
    rb, nb = bisection(f_e, 0.5, 1.5, eps=1e-12)
    print(f"Бисекция [0.5, 1.5]: корень = {rb:.12f}, итераций: {nb}")
except ValueError as e:
    print(f"Бисекция [0.5, 1.5]: {e}")
print("Вывод: f(1)=0, f'(1)=0 — касание. Ньютон делит на ноль, секущие дают знаменатель 0, бисекция не видит смены знака.")

print(f"\n3. k = 3:")
f3 = make_f(3)
df3 = make_df(3)

root_n3a, jn3a, st_n3a = newton(f3, df3, x0=0.0, eps=1e-12)
root_s3a, js3a, st_s3a = secant(f3, 0.0, 0.5, eps=1e-12)
root_b3a, nb3a = bisection(f3, -0.1, 0.9, eps=1e-12)

root_n3b, jn3b, st_n3b = newton(f3, df3, x0=1.5, eps=1e-12)
root_s3b, js3b, st_s3b = secant(f3, 1.5, 2.5, eps=1e-12)
root_b3b, nb3b = bisection(f3, 1.1, 2.1, eps=1e-12)

print(f"{'Метод':<12} | {'Корень':<18} | {'Итераций':>9}")
print("-" * 48)
print(f"{'Ньютон':<12} | {root_n3a:<18.12f} | {len(jn3a):>9}")
print(f"{'Секущие':<12} | {root_s3a:<18.12f} | {len(js3a):>9}")
print(f"{'Бисекция':<12} | {root_b3a:<18.12f} | {nb3a:>9}")
print("-" * 48)
print(f"{'Ньютон':<12} | {root_n3b:<18.12f} | {len(jn3b):>9}")
print(f"{'Секущие':<12} | {root_s3b:<18.12f} | {len(js3b):>9}")
print(f"{'Бисекция':<12} | {root_b3b:<18.12f} | {nb3b:>9}")

print(f"\n4. k = 5:")
f5 = make_f(5)
df5 = make_df(5)

root_n5a, jn5a, st_n5a = newton(f5, df5, x0=0.0, eps=1e-12)
root_s5a, js5a, st_s5a = secant(f5, 0.0, 0.3, eps=1e-12)
root_b5a, nb5a = bisection(f5, -0.1, 0.5, eps=1e-12)

root_n5b, jn5b, st_n5b = newton(f5, df5, x0=2.0, eps=1e-12)
root_s5b, js5b, st_s5b = secant(f5, 2.0, 3.0, eps=1e-12)
root_b5b, nb5b = bisection(f5, 1.6, 2.6, eps=1e-12)

print(f"{'Метод':<12} | {'Корень':<18} | {'Итераций':>9}")
print("-" * 48)
print(f"{'Ньютон':<12} | {root_n5a:<18.12f} | {len(jn5a):>9}")
print(f"{'Секущие':<12} | {root_s5a:<18.12f} | {len(js5a):>9}")
print(f"{'Бисекция':<12} | {root_b5a:<18.12f} | {nb5a:>9}")
print("-" * 48)
print(f"{'Ньютон':<12} | {root_n5b:<18.12f} | {len(jn5b):>9}")
print(f"{'Секущие':<12} | {root_s5b:<18.12f} | {len(js5b):>9}")
print(f"{'Бисекция':<12} | {root_b5b:<18.12f} | {nb5b:>9}")

k_vals = [math.e + 0.1*i for i in range(0, 100)]  # от e до ~10
small_roots, large_roots = [], []
for k in k_vals:
    fk = make_f(k)
    dfk = make_df(k)
    r_small, _, _ = newton(fk, dfk, x0=0.1, eps=1e-10)
    r_large, _, _ = newton(fk, dfk, x0=1.5 + math.log(k), eps=1e-10)
    small_roots.append(r_small)
    large_roots.append(r_large)

plt.figure(figsize=(7, 4))
plt.plot(k_vals, small_roots, label="малый корень")
plt.plot(k_vals, large_roots, label="большой корень")
plt.axvline(math.e, color="red", linestyle="--", label="k = e")
plt.xlabel("k")
plt.ylabel("x*")
plt.grid(True)
plt.legend()
plt.title("Зависимость корней e^x − kx = 0 от k")
plt.show()

print("\n5. Вывод: При k → e⁺ корни сливаются в x = 1 (касание).")
print("При k → ∞ малый корень → 0⁺, большой корень ~ ln k + ln ln k → ∞.")