import plotly. express as px
import pandas as pd

df = px.data. stocks ()
print (df.head(5))
fig = px.line (df, x="date", y=df. columns,
hover_data={ "date": "|%B %d, %Y"},
title='custom tick labels')
fig. update_xaxes (
dtick="M1",
tickformat="&b\n%Y")
fig.write_html(r"..\output\10_Plotly_TimeSeries_Maps\10a_line_chart.html")
fig. show ()

fig = px.scatter (df, x = "date", y = df. columns)

fig.write_html(r"..\output\10_Plotly_TimeSeries_Maps\10a_scatter_chart.html")
fig. show ()

fig = px.bar (df, x = "date", y = df. columns, barmode='group' )

fig.write_html(r"..\output\10_Plotly_TimeSeries_Maps\10a_bar_chart.html")
fig. show ()