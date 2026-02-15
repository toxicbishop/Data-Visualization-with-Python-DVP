#a. Join Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset ("iris")

# Create a joint plot for sepal length and sepal width
sns. jointplot (x="sepal_length", y="sepal_width", data=iris, kind="reg")
plt.savefig(r'..\output\07_Seaborn_Customization\07a_joinplot.png')
plt.show ()

#b. Hexagon distribution.
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset ("iris")

# Create a hexbin distribution plot for sepal length and sepal width
sns. jointplot (x="sepal_length", y="sepal_width", data=iris, kind="hex", color="b")
plt.title ("Hexagon Distribution: Sepal Length vs. Sepal Width")
plt.savefig(r'..\output\07_Seaborn_Customization\07b_hex_distribution.png')
plt.show ()

#c. KDE Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset ("iris")

# Create a KDE plot for petal length
sns. kdeplot (iris ["petal_length"], shade=True)
plt.title ("KDE Plot of Petal Length")
plt.xlabel ("Petal Length (cm) ")
plt.ylabel("Density")
plt.savefig(r'..\output\07_Seaborn_Customization\07c_kde_plot.png')
plt. show ()

#d. Heat Map

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset ("iris")

# Calculate the correlation matrix
correlation_matrix = iris. corr ()

# Create a heatmap of the correlation matrix
sns. heatmap (correlation_matrix, annot=True, cmap="coolwarm")
plt.title ("Heatmap of Feature Correlations in the Iris Dataset")
plt.savefig(r'..\output\07_Seaborn_Customization\07d_heatmap.png')
plt. show ()

#e. Pair Plot

import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a pair plot
sns .pairplot (iris, hue="species")
plt.savefig(r'..\output\07_Seaborn_Customization\07e_pairplot.png')
plt. show ()

#f. Box Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Tips dataset
tips = sns.load_dataset ("tips")

# Create a box plot for total bill amounts by day
sns.boxplot (x="day", y="total_bill", data=tips)
plt.title ("Box Plot: Distribution of Total Bill Amount by Day")
plt.xlabel ("Day of the Week")
plt.ylabel ("Total Bill Amount ($)")
plt.savefig(r'..\output\07_Seaborn_Customization\07f_boxplot.png')
plt. show ()

#g. Regression Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Tips dataset
tips = sns.load_dataset ("tips")

# Create a linear regression plot
sns. lmplot (x="total_bill", y="tip", data=tips)
plt. title ("Linear Regression Plot: Total Bill vs. Tip")
plt.xlabel ("Total Bill Amount ($) ")
plt.ylabel ("Tip Amount ($) ")
plt.savefig(r'..\output\07_Seaborn_Customization\07g_regression_plot.png')
plt. show ()

#h. Bar Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data
data = sns.load_dataset("tips")

# Customize the color palette
sns.set_palette("pastel")

# Create a bar plot
sns.barplot(x="day",y="total_bill", data=data, ci=None)
plt.title("Customized Bar Plot with Color Palette")
plt.xlabel("Day of the Week")
plt.ylabel("TotalBillAmount($)")
plt.savefig(r'..\output\07_Seaborn_Customization\07h_bar_plot.png')
plt.show()