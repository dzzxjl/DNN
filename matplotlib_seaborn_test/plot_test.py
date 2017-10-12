import numpy as np
import matplotlib.pylab as plt

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)
# fig理解成一张图片

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

plt.show()
