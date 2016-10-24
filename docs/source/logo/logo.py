import numpy
from matplotlib import pyplot as plt


x0 = numpy.linspace(0, 25, 1000)
y0 = numpy.cos(x0)

x1 = numpy.linspace(0, 3.14, 1000)
y1 = numpy.sin(x1)

x = x0
y = y0 * y1

fig = plt.figure(figsize=(5, 5), facecolor='purple')
plt.plot(x, y, color='w', linewidth=10.0)
plt.axis('off')
fig.axes[0].get_xaxis().set_visible(False)
fig.axes[0].get_yaxis().set_visible(False)

plt.savefig('logo.svg', facecolor='purple', bbox_inches='tight', pad_inches=1.)
