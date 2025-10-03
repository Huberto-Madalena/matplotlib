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

#splitting the chart up
plt.subplot(1,2,1)
plt.plot(x_1,y_1, 'r')
#heads up! the 3rd parameter is the colour scheme for  teh chart (r for red, b for blue etc)
plt.subplot(1,2,2)
plt.plot(x_1,y_1,'b')


fig_1 = plt.figure(figsize=(5,4), dpi=100)
axes_1 = fig_1.add_axes([0.1,0.1,0.9,0.9])
axes_1.set_xlabel('days')
axes_1.set_ylabel('days squared')
axes_1.set_title('days squared chart')
axes_1.plot(x_1,y_1,label='x/x²')
axes_1.plot(y_1,y_1,label='x²/x')
axes_1.legend(loc=0)
#upper right:1, upper left:2, lower left:3; lower right:4

axes_2 = fig_1.add_axes([0.45, 0.45, 0.4, 0.3])
axes_2.set_xlabel('days')
axes_2.set_ylabel('days squared')
axes_2.set_title('days squared chart')
axes_2.plot(x_1,y_1,'r')

axes_2.text(0,40, 'message')



plt.show()