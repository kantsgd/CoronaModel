import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from matplotlib import pyplot as plt

import pylab

pylab.ion()

g = nx.barabasi_albert_graph(1000, 1)

my_pos = nx.spring_layout(g, seed=100)

model = ep.SIRModel(g)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter("beta", 0.1)
cfg.add_model_parameter("gamma", 0.02)
cfg.add_model_parameter("percentage_infected", 0.01)
model.set_initial_status(cfg)

iterations = model.iteration_bunch(200, node_status=True)

i = 0
color_map = []

for iteration in iterations:
    for node in iteration['status']:
        if i == 0:
            if iteration['status'][node] == 0:
                color_map.insert(node, 'green')
            elif iteration['status'][node] == 1:
                color_map.insert(node, 'red')
            elif iteration['status'][node] == 2:
                color_map.insert(node, 'yellow')
        else:
            if iteration['status'][node] == 0:
                color_map[node] = 'green'
            elif iteration['status'][node] == 1:
                color_map[node] = 'red'
            elif iteration['status'][node] == 2:
                color_map[node] = 'yellow'
    i += 1

    nx.draw(g, pos=my_pos, node_color=color_map, node_size=14)
    plt.show()
    plt.pause(0.5)
    plt.clf()
