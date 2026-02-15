import matplotlib.pyplot as plt

state=['Assam', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland','Tripura', 'Nagaland']
forest_cover=[67353,27692,17280,17321,19240,13464,8073]

ex=[0.0,0.0,0.2,0.0,0.0,0.0,0.0]

plt.pie(forest_cover,labels=state,explode=ex,
autopct="%0.2f%%",shadow=True,
radius=1.0,labeldistance=1,
startangle=90, textprops={"fontsize":10},counterclock=False,
wedgeprops={'linewidth':1})

plt.title("Forest Cover in States of India")

plt.legend(bbox_to_anchor =(1, 0, 0.5, 1))

plt.savefig(r'..\output\05_Matplotlib_Histogram_Pie\05b_pie_chart.png')
plt.show()