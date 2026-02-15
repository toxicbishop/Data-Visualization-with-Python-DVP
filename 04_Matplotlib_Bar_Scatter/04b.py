import matplotlib.pyplot as plt
import numpy as np

plt.title("Sales vs Price with Profit")

price = np.asarray([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])
sales_per_day = np.asarray([34, 62, 49, 22, 13, 19])
profit = np.asarray([20, 35, 40, 20, 27.5, 15])

plt.scatter(x=price, y=sales_per_day, s=profit * 20,c='r',marker = '*', edgecolor='b')

plt.xlabel("Chocolates Price",fontsize=15)
plt.ylabel("Sales Per Day",fontsize=15)

plt.xticks(price)
plt.yticks(sales_per_day)

plt.savefig(r'..\output\04_Matplotlib_Bar_Scatter\04b_scatter_plot.png')
plt.show()