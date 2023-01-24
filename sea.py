import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

sns.set()
x = np.linspace(0, 10, 500)
y = np.random.randn(500)
plt.plot(x, y)
plt.show()

# distplot lets you not only view the histogram of a sample
# but also estimate the distribution from which the sample is derived.
sns.displot(y, kde=True);
plt.show()

# loading a dataset
iris = sns.load_dataset("iris")
iris.head()
sns.pairplot(iris, hue='species', height=2.5);
plt.show()