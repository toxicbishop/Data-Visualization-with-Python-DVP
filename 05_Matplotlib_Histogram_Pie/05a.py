import matplotlib.pyplot as plt
import numpy as np

# Sample data: Student grades
grades = [75, 82, 92, 88, 78, 90, 85, 95, 70, 87, 93, 79, 81, 86, 89, 94, 73, 84, 91, 77]

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(grades, bins=[70, 75, 80, 85, 90, 95, 100], edgecolor='black', alpha=0.7, color='skyblue')

# Customize labels and title
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.title('Grade Distribution in a Class')

# Set the x-axis limits
plt.xlim(70, 100)

# Display the plot
plt.savefig(r'..\output\05_Matplotlib_Histogram_Pie\05a_histogram.png')
plt.show()