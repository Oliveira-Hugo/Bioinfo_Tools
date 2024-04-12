import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/prj/posgrad/hugodpo/Downloads/resultados_denv_1_cdhit_00001')

start_end = df[['Start', 'End']]

positions = start_end.values.flatten()
plt.figure(figsize=(10, 6))
plt.hist(positions, bins=np.arange(0, 10963, 20), density=True, alpha=0.7, color='blue')
plt.title('Density of predicted recombination event positions')
plt.xlabel('Position')
plt.ylabel('Density')
plt.grid(True)
plt.show()

