import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

sns.set()
x = np.linspace(0, 10, 500)
y = np.random.randn(500)
plt.plot(x, y)
plt.show()