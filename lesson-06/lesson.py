import numpy as np
import matplotlib.pyplot as plt

angles = np.deg2rad([90, 150, 210, 270, 330, 30])
hexagon = np.column_stack([np.cos(angles), np.sin(angles)])
hexagon = np.vstack([hexagon, hexagon[0]])  # замыкаем контур

theta = np.deg2rad(45)
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

M_yx = np.array([
    [0, 1],
    [1, 0]
])

P_rotated = hexagon @ R.T
P_reflected = hexagon @ M_yx.T


color_orig = "#FFE600"
color_rot  = "#7E79FF"
color_ref  = "#DB73D8"

fig, ax = plt.subplots(figsize=(7.5, 7.5))

# Рисуем фигуры с новыми цветами
ax.plot(hexagon[:, 0], hexagon[:, 1], "o-", color=color_orig, 
        label="Исходный", lw=2.5, markersize=6)
ax.plot(P_rotated[:, 0], P_rotated[:, 1], "o-", color=color_rot, 
        label="Поворот 45°", lw=2.5, markersize=6)
ax.plot(P_reflected[:, 0], P_reflected[:, 1], "o-", color=color_ref, 
        label="Отражение y=x", lw=2.5, markersize=6)

ax.axhline(0, color="black", lw=1.5, alpha=0.7)
ax.axvline(0, color="black", lw=1.5, alpha=0.7)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, markersize=8)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, markersize=8)

ax.grid(True, which="both", alpha=0.3)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal")

ax.set_xlabel("X", fontsize=12)
ax.set_title("Преобразования шестиугольника", fontsize=14)

# Легенда в правом верхнем углу
ax.legend(loc="upper right", framealpha=0.9)

plt.tight_layout()
plt.show()