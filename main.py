import math
import random

from plot import plot
from aco import SolveTSPUsingACO
from matplotlib import pyplot as plt

if __name__ == '__main__':
    #tạo random input
    _nodes = [(random.uniform(-400, 400), random.uniform(-400, 400)) for _ in range(0, 30)]
    
    #Lấy input từ file có sẵn
    
    # _nodes = []
    # with open('E:/Ant_Colony/input.txt') as f:
    #     for line in f.readlines():
    #         print(line)
    #         city = line.split(' ')
    #         city[1].replace("\n","")
    #         print(city)
    #         a = (float(city[0]) , float(city[1]))
    #         _nodes.append(a)
    
    # Lưu lại input nếu muốn kiểm tra
    with open("E:/Ant_Colony/input.txt", "w") as output:
        for element in _nodes:
            output.writelines(str(element[0]) +" " +  str(element[1]) + "\n")
    
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