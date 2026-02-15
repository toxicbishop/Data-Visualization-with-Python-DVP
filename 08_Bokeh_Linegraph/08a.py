from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.annotations import Title, Legend, LegendItem
from bokeh.io import output_notebook, output_file

# Sample data
x = [1,2,3,4,5]
y1 = [2, 5, 3, 6, 7]
y2 = [4, 6, 7, 5, 9]

# Create a Bokeh figure
p = figure (title="Line Graph with Annotations and Legends", x_axis_label="X-axis", y_axis_label="Y-axis")

# Add data souroes
sourcel = ColumnDataSource(data=dict(x=x, y=y1) )
source2 = ColumnDataSource(data=dict(x=x, y=y2))

# Plot the first line
line1 = p.line('x', 'y', source=sourcel, line_width=2, line_color="blue", legend_label="Line 1")

# Plot the second line
line2 = p.line('x', 'y', source=source2, line_width=2, line_color='red', legend_label="Line 2")

# Add an annotation
annotation = Title(text="Annotation Example", text_font_size="14px")
p.add_layout(annotation, 'above')

# Create a legend
legend = Legend(items=[LegendItem(label="Line 1", renderers=[line1]), LegendItem(label="Line 2", renderers=[line2])])
p.add_layout(legend, 'above')

# Show the plot
# Show the plot
# output_notebook ()
output_file (r'..\output\08_Bokeh_Linegraph\08a_line_graph.html')
show (p)