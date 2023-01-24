import matplotlib.pyplot as plt
import numpy as np
import random

fig = plt.figure()
ax = plt.axes()
plt.show()
# The variable  fig  corresponds to a container that contains all objects 
# (axes, labels, data, etc.). The axes correspond to the grid shown above
#  which will then contain the graph's data.

fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));

plt.show()

#  While this plot is nice, it is not quite ready for use in a professional setting.
#  There are many aesthetic elements 

# Change default font size
plt.rcParams.update({'font.size': 15})

fig = plt.figure()
ax = plt.axes()

# Solid Line , color specified by its name
plt.plot(x, np.sin(x - 0), color="blue", linestyle='solid', label='bleu')

#short name for color, dashed line
plt.plot(x, np.sin(x - 1), color="g", linestyle='dashed', label='vert')

# Grayscale between 0 and 1 , dashes and dots
plt.plot(x, np.sin(x - 2), color="0.75", linestyle='dashdot', label='gris')

# RGB color , dotted line
plt.plot(x, np.sin(x - 3), color="#FF0000", linestyle='dotted', label='rouge')

# Axis limits. Try also 'tight' and 'equal' to see their effect
plt.axis([-1, 11, -1.5, 1.5]);
#Labels
plt.title("Example of a Graph")
# place of the legend
plt.legend(loc='lower left');
# Axis titles
ax = ax.set(xlabel='titulo x', ylabel='titulo y axis')
plt.show()


# DISCRETE DATA
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.k');
plt.show()

# same but with styling
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
ecolor='lightgray', elinewidth=3, capsize=0);
plt.show()

print(plt.style.available[:6])
# change the size of the figure
fig = plt.figure(figsize=(12, 8))
for i in range(6):
    # This is how you add subplots
    fig.add_subplot(3, 2, i + 1)
    plt.style.use(plt.style.available[i])
    plt.plot(x, y)
    # this is how you write on a plot
    plt.text(s=plt.style.available[i], x=5, y=2, color='red')
plt.show()    





