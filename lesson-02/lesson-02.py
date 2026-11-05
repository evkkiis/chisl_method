import math
import mpmath as mp

mp.mp.dps = 50
def bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)
def good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))
def exact(x):
    return mp.sqrt(x + 1) - mp.sqrt(x)

print("x | ошибка плохого | ошибка хорошего")
for x in [10**10, 10**-12, 10**14]:
    e = exact(x)
    err_bad = abs(bad(x) - e) / abs(e)
    err_good = abs(good(x) - e) / abs(e)
    print(f"{x:.0e} | {float(err_bad):.2e} | {float(err_good):.2e}")