import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pokemon = pd.read_csv('pokemon.csv')

plt.figure(figsize=(20, 5))

plt.subplot(1, 2, 1)
bins = np.arange(0, pokemon.height.max() + 0.5, 0.5)
plt.hist(data=pokemon, x='height', bins=bins)

plt.subplot(1, 2, 2)
bins = np.arange(0, pokemon.height.max() + 0.2, 0.2)
plt.hist(data=pokemon, x='height', bins=bins)
plt.xlim(0, 6)

plt.show()