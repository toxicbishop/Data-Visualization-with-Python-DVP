# i) Sine Wave

import seaborn as sns
from bokeh.plotting import figure, show, output_file
import plotly.graph_objects as go
import numpy as np

# Create data for the 3D surface plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create the 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Customize the layout
fig.update_layout(
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis',
    ),
    title='3D Surface Plot Example',
)

# Show the plot
fig.write_html(r"..\output\09_Plotly_3D\09a_surface_plot.html")
fig.show()

# ii) Scatter Plot

import plotly.express as px

# Load the Iris dataset
df = px.data.iris()

# Create a 3D scatter plot
fig = px.scatter_3d(df, x="petal_length", y="petal_width", z="sepal_length", color="species",     
                    title="3D Scatter Plot of Iris Dataset")
fig.update_layout(scene=dict(
    xaxis_title="Petal Length",
    yaxis_title="Petal Width",
    zaxis_title="Sepal Length"
))

# Show the plot
fig.write_html(r"..\output\09_Plotly_3D\09b_scatter_plot.html")
fig.show()