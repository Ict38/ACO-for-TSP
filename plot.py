import math
from matplotlib import pyplot as plt

def plot(aco):
        x = [aco.nodes[i][0] for i in aco.global_best_tour]
        x.append(x[0])
        y = [aco.nodes[i][1] for i in aco.global_best_tour]
        y.append(y[0])
        plt.plot(x, y, linewidth=1)
        plt.scatter(x, y, s=math.pi * (math.sqrt(2.0) ** 2.0))
        for i in aco.global_best_tour:
            plt.annotate(aco.labels[i], aco.nodes[i], size=8)
        plt.show()
        plt.gcf().clear()