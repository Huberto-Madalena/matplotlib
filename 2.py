import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#simple squared chart
x_1 = np.linspace(0,5,10)
#np.linspace takes the values of the x axle and uses them as reference for future calculations
y_1 = x_1**2;
#the values for the y axle on our chart will have the values of x squared
#this is also a quadratic function,as the line follows an exponential growth rate
plt.plot(x_1, y_1)
plt.title('days squared chart')
plt.xlabel('days')
plt.ylabel('days squared')


plt.show()