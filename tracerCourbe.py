from matplotlib import pyplot as plt
import numpy as np

x = np.arange(10)

y = x

plt.figure(1)
plt.subplot(121)
plt.plot(x, y, 'r')
plt.subplot(122)
plt.plot(x, y * y, 'g')

plt.show()

