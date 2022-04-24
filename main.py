import math
import random

from plot import plot
from aco import SolveTSPUsingACO
from matplotlib import pyplot as plt

if __name__ == '__main__':
    _nodes = [(random.uniform(-400, 400), random.uniform(-400, 400)) for _ in range(0, 15)]
    print("List of City:")
    for i in range(len(_nodes)):
        print('{} {}'.format(i,_nodes[i]))
    acs = SolveTSPUsingACO(mode='ACS', nodes=_nodes)
    acs.run()
    plot(acs)
    elitist = SolveTSPUsingACO(mode='Elitist', nodes=_nodes)
    elitist.run()
    plot(elitist)
    max_min = SolveTSPUsingACO(mode='MaxMin', nodes=_nodes)
    max_min.run()
    plot(max_min)