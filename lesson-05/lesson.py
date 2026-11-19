# Задача №1

# Задача №2
import timeit
import tracemalloc
import matplotlib.pyplot as plt

N_values = [100_000, 1_000_000]

methods = {
    "for+append": "out = []\nfor i in range(N):\n    out.append(i * i)",
    "listcomp":   "out = [i * i for i in range(N)]",
    "map+lambda": "out = list(map(lambda i: i * i, range(N)))",
}

times_ms  = {name: [] for name in methods} 
mems_mb   = {name: [] for name in methods} 

for N in N_values:
    for name, stmt in methods.items():
        r = timeit.repeat(stmt, globals={"N": N}, number=1, repeat=5)
        times_ms[name].append(min(r) * 1000) 
        tracemalloc.start()
        exec(stmt, {"N": N})                   
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        mems_mb[name].append(peak / (1024 * 1024)) 


print(f"{'N':>10} | {'метод':<12} | {'время, мс':>10} | {'пик, МБ':>9}")
print("-" * 50)
for i, N in enumerate(N_values):
    for name in methods:
        print(f"{N:>10} | {name:<12} | {times_ms[name][i]:>10.2f} | "
              f"{mems_mb[name][i]:>9.2f}")
    print("-" * 50)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

for name in methods:
    ax1.plot(N_values, times_ms[name], "o-", label=name)
ax1.set_xscale("log")
ax1.set_xlabel("N")
ax1.set_ylabel("время, мс")
ax1.set_title("Время создания списка квадратов")
ax1.grid(True, which="both", alpha=0.2)
ax1.legend()

x = list(range(len(N_values)))
width = 0.25
for k, name in enumerate(methods):
    ax2.bar([xi + (k - 1) * width for xi in x],
            mems_mb[name], width=width, label=name)
ax2.set_xticks(x)
ax2.set_xticklabels([f"N={N}" for N in N_values])
ax2.set_ylabel("пиковая память, МБ")
ax2.set_title("Пиковая память при создании")
ax2.grid(True, axis="y", alpha=0.2)
ax2.legend()

plt.tight_layout()
plt.savefig("bench_list_build.png", dpi=130)
plt.show()

print(
    "\nВывод:\n"
    "(а) По памяти все три способа практически равны: результат — один и тот же\n"
    "    список из N int-объектов, а промежуточные объекты (append-вызовы,\n"
    "    lambda-вызовы) краткоживущие и на пик почти не влияют.\n"
    "(б) По времени list comprehension быстрее всех: цикл выполняется на уровне\n"
    "    C без вызовов append для каждого элемента.\n"
    "(в) map + lambda медленнее из-за накладных расходов на вызов lambda\n"
    "    для каждого элемента; for+append обычно между ними или медленнее."
)