# Importing and Using the Plotly Library
# Nefunguje
import plotly.graph_objs as go
import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)
iplot=([go.Histogram2dContour(x=x, y=y, contours=dict (coloring='heatmap')), 
go.Scatter(x=x, y=y, mode='markers',
marker=dict(color='white', size=3, opacity=0.3))])

iplot.show()