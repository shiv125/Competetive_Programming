#import Graph

from jgraph import *
import plotly.plotly as py
import plotly.graph_objs as go

#import igraph
#from igraph import *
g = Graph.Tree(17,2) #Create tree graph with 127 vertices each with 2 children
layout = g.layout("tree")
plot(g, layout = layout)
