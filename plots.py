import matplotlib.pyplot as plt
import numpy as np

sample_size = np.array([4, 8, 16, 32, 60])
execution_time = np.array([82, 667, 6120, 25296, 56644])

plt.title('Benchmarking of OpenRDP implementation')
plt.xlabel('Sample size (N of sequences)')
plt.ylabel('Execution time (seconds)')

plt.plot(sample_size, execution_time)
plt.scatter(sample_size, execution_time, marker='x', color='red', zorder=5)

offset = 2000

midpoint_x = (sample_size[0] + sample_size[2]) / 2

for i in range(len(sample_size)):
    if i == 1:
        plt.text(midpoint_x, 80 + offset, f'({sample_size[i]}, {execution_time[i]})', fontsize=8, ha='center', va='bottom')
    else:
        plt.text(sample_size[i], execution_time[i] + offset, f'({sample_size[i]}, {execution_time[i]})', fontsize=8, ha='center', va='bottom')

plt.xlim(0, max(sample_size) * 1.1)
plt.ylim(0, max(execution_time) * 1.2)
plt.grid(axis='x', linestyle='--', alpha=0.5, which='major')
plt.xticks(np.arange(0, max(sample_size) + 1, 10))

plt.tight_layout()
plt.show()

