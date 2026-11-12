import numpy as np

arr = np.arange(24).reshape(6, 4)
print("1:", arr.shape, arr.ndim, arr.size, arr.dtype)
print("2 (не изменились):", np.array_equal(arr.flatten(), arr.reshape(4, 6).reshape(2, 3, 4).reshape(24)))

col = arr[:, 2]
col[0] = 999  
print("3 (это view, arr изменился):", arr[0, 2] == 999)

arr = np.arange(24).reshape(6, 4)
filtered = arr[arr > 10]
print("4 (среднее):", filtered.mean())

centered = arr - arr.mean(axis=1, keepdims=True)
print("5 (форма сохранена, суммы ~0):", centered.shape, np.allclose(centered.sum(axis=1), 0))