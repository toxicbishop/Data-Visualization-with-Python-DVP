import matplotlib.pyplot as plt
import numpy as np
m=5
c=5
#when y=x
x=np.arange(-4,4)
y=np.arange(-4,4)

plt.axvline(color='g')
plt.axhline(color='g')

plt.title ("Linear Plotting")
#when y=x
plt.plot (x,y,color='c',marker='D' , label='Y=X' )
#when y =- x
plt.plot (-x,y, color='k' ,marker='*' , label='Y =- X')
#when slope=5 and intercept=5
plt.plot (x,m*x+c, color='r' ,marker='o' , label='Y=5X+5' )
#when slope =- 5 and intercept=5
plt.plot (x,-m*x+c, color='b' ,marker='^', label='Y =- 5X+5')
plt.grid()
plt.legend ()
plt.savefig(r'..\output\06_Matplotlib_Linear_Plotting\06a_linear_plot.png')
plt.show ()