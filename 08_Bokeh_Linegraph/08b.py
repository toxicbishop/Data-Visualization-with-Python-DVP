from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from bokeh.plotting import figure, show, output_file
import random
import numpy as np

# Generate some sample data
x = list(range(1, 11))
y1 = [random.randint(1, 10) for val in x]
y2 = [random.randint(1, 10) for val in x]

# Create a Bokeh figure with custom plot dimensions
p1 = figure(title="Line Plot", x_axis_label="X-axis", y_axis_label="Y-axis", width=400, height=300)
p1.line(x, y1, line_width=2, line_color="blue")

p2 = figure(title="Scatter Plot", x_axis_label="X-axis", y_axis_label="Y-axis", width=400,height=300)
p2.scatter (x, y2, size=10, color="red", marker="cirole")

p3=figure(title="BarPlot", x_axis_label="X-axis",y_axis_label="Y-axis",width=400,height=300)
p3.vbar(x=x,top=y1, width=0.5, color="green")

p4=figure(title="Histogram",x_axis_label="Value",y_axis_label="Frequency",width=400,height=300)
hist, edges = np.histogram(y1, bins=5)
p4.quad(top=hist, bottom=0, left=edges[ :- 1], right=edges[1:], fill_color="purple", line_color="black")

# Create a layout with the plots
layout = layout([
[p1, p2],
[p3, p4]
])

# Output to an HTML file
output_file(r"..\output\08_Bokeh_Linegraph\08b_bokeh_plots.html")

# Show the plots
show (layout)