import matplotlib.pyplot as plt
import numpy as np

# Data
ncores = [4, 16, 32, 64, 128, 256, 512]
wall_times = [435, 108, 62, 42, 37, 35, 28]

cores = np.array(ncores, dtype=float)
times = np.array(wall_times, dtype=float)

# Speedup and efficiency
Tmin = times[0]
speedup = Tmin / times
efficiency = speedup / (cores / cores[0])

# 1x3 subplot layout
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Wall time
axes[0].plot(cores, times, "o-", label="Measured")
axes[0].set_xlabel("Number of cores")
axes[0].set_ylabel("Wall time (s)")
axes[0].set_title("Wall time vs cores")
axes[0].grid(True)
axes[0].legend()

# Speedup
axes[1].plot(cores, speedup, "o-", label="Measured")
axes[1].plot(cores, cores/cores[0], "--", label="Ideal")
axes[1].set_xlabel("Number of cores")
axes[1].set_ylabel("Speedup")
axes[1].set_title("Speedup vs cores")
axes[1].grid(True)
axes[1].legend()

# Efficiency
axes[2].plot(cores, efficiency, "o-")
axes[2].set_xlabel("Number of cores")
axes[2].set_ylabel("Parallel efficiency")
axes[2].set_title("Efficiency vs cores")
axes[2].grid(True)

plt.tight_layout()
plt.savefig("scaling_1x3.png", dpi=200)
plt.show()

print("Saved: scaling_1x3.png")
