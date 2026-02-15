import matplotlib.pyplot as plt

# Data for the bar plot
categories = ['Science', 'Commerce', 'Arts', 'Literature' ]
values = [10, 25, 15, 30]

# Create a bar plot
plt.bar (categories, values, color='m')

# Add labels and a title
plt.xlabel ('Categories')
plt.ylabel ('Values')
plt.title ('Bar Plot Example' )

# Display the plot
plt.savefig(r'..\output\04_Matplotlib_Bar_Scatter\04a_bar_plot.png')
plt.show ()