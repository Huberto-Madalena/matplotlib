import matplotlib.pyplot as plt
####%matplotlib inline
import numpy as np
import pandas as pd

#%reload_ext autoreload
#%autoreload 2

x_1 = np.linspace(0,5,10)
y_1 = x_1**2;
plt.plot(x_1, y_1)
plt.show()