import math
import matplotlib.pyplot as plt

#ЗАДАНИЕ №1

def bisection(f, a, b, eps=1e-9, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError(f"Нет смены знака на [{a}, {b}]: f(a)={fa}, f(b)={fb}")
    journal = []
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        length = b - a
        journal.append({"iter": k, "a": a, "b": b, "c": c, "fc": fc, "length": length})
        if fc == 0:
            return c, journal, "f_zero"
        if length < eps:
            return c, journal, "ok"
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c, journal, "max_iter"


def print_journal(journal, title="", show_all=False):
    print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'a':>10} | {'b':>10} | {'c':>10} | {'f(c)':>12} | {'b-a':>10}")
    print("-" * 65)
    if not show_all and len(journal) > 10:
        rows = journal[:5] + [None] + journal[-5:]
    else:
        rows = journal
    for row in rows:
        if row is None:
            print(f"{'...':>3} | {'...':>10} | {'...':>10} | {'...':>10} | {'...':>12} | {'...':>10}")
        else:
            print(f"{row['iter']:>3} | {row['a']:>10.6f} | {row['b']:>10.6f} | "
                  f"{row['c']:>10.6f} | {row['fc']:>12.2e} | {row['length']:>10.2e}")


def f(x):
    return x**3 - 6 * x**2 + 11 * x - 6


def plot_function():
    x_vals = [i / 100 for i in range(401)]
    y_vals = [f(x) for x in x_vals]
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x) = x³ - 6x² + 11x - 6")
    plt.axhline(0, color='black', linewidth=1)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title("График функции f(x) на отрезке [0, 4]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_function()

    intervals = [
        (0.5, 1.1, "Корень 1 (около x=1)"),
        (1.5, 2.1, "Корень 2 (около x=2)"),
        (2.5, 3.1, "Корень 3 (около x=3)")
    ]
    eps = 1e-9
    results = []

    for a, b, name in intervals:
        root, journal, status = bisection(f, a, b, eps=eps)
        print_journal(journal, f"{name}, [{a}, {b}]")
        delta_0 = b - a
        n_theor = math.ceil(math.log2(delta_0 / eps))
        print(f"Найденный корень: {root:.12f}")
        print(f"Значение f(root): {f(root):.3e}")
        print(f"Статус: {status}, Итераций: {len(journal)} (теор. оценка: {n_theor})")
        results.append((name, root, len(journal), delta_0, n_theor))

    print("\n" + "=" * 80)
    print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ")
    print("=" * 80)
    print(f"{'Корень':<25} | {'Числ. x*':<15} | {'Итераций':<9} | {'Теор. n':<8} | {'f(x*)':<10}")
    print("-" * 80)
    exact_roots = [1.0, 2.0, 3.0]
    for i, (name, root, iters, delta_0, n_theor) in enumerate(results):
        print(f"{name:<25} | {root:>15.10f} | {iters:>9} | {n_theor:>8} | {f(root):>10.2e}")

    print("\n" + "=" * 80)
    print("ОЦЕНКА ПОГРЕШНОСТЕЙ")
    print("=" * 80)
    print(f"{'x* точный':<10} | {'x* численный':<15} | {'Абс. погрешность':<16} | {'Отн. погрешность':<16}")
    print("-" * 80)
    for i, (name, root, iters, delta_0, n_theor) in enumerate(results):
        x_exact = exact_roots[i]
        abs_err = abs(root - x_exact)
        rel_err = abs_err / abs(x_exact)
        print(f"{x_exact:<10.1f} | {root:>15.10f} | {abs_err:>16.2e} | {rel_err:>16.2e}")