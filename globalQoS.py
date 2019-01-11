# -*- encoding: utf-8 -*-
import utility
import numpy as np
import random
import math
#import Tkinter
from WSNGene import GA
import matplotlib.pyplot as plt

b1 = 50
b2 = 0.000013
a = 4
c = 0.00001
Delay = [[0 for i in range(51)]for j in range(51)]
rho = 50

# for i in range(50):
#     for j in range(50):
#         if i == j:
#             Delay[i][j] = 0
#         else:
#             Delay[i][j] = random.random()

class TSP(object):
    def __init__(self, aLifeCount, aDelayRequest):
        self.initCitys()
        self.lifeCount = aLifeCount
        self.delayRequest = aDelayRequest
        self.ga = GA(aCrossRate=0.7,
                     aMutationRate=0.02,
                     aLifeCount=self.lifeCount,
                     aDelayReq = self.delayRequest,
                     aGeneLength=len(self.nodes),
                     aMatchFun=self.matchFun(),
                     aDelayFun = self.delaytest())

    # initialzation
    def initCitys(self):
        self.nodes = []
        self.Delay = []
        self.C = []
        self.D = []

        # load data from AFN.dat file
        data = np.loadtxt('AFN.dat')
        for i in data:
            self.nodes.append(i)
        delay = np.loadtxt('Delay.dat')
        for d in delay:
            self.Delay.append(d)


    # calculate end-to-end distance
    def distance(self, order):
        distance = 0.0
        for i in range(0, len(self.nodes) - 2):
            index1, index2 = order[i], order[i + 1]
            node1, node2 = self.nodes[index1], self.nodes[index2]
            distance += math.sqrt((node1[1] - node2[1]) ** 2 + (node1[2] - node2[2]) ** 2)
        print(distance)
        return distance
    # calculate link cost
    def linkcost(self, distance):
        costij = b1 + b2*(distance**a)
        return costij

    # calculate end-to-end cost
    def cost(self, order):
        u = 0.0
        for i in range(0, len(self.nodes)-1):
            index1, index2 = order[i], order[i+1]
            node1, node2 = self.nodes[index1], self.nodes[index2]
            lc = self.linkcost(math.sqrt((node1[1] - node2[1]) ** 2 + (node1[2] - node2[2]) ** 2))
            u += utility.utilitycost(lc, node1[3], node2[3])
        return u

    # calculate end-to-end delay
    def delay(self, order):
        d = 0.0
        for i in range(0, len(self.nodes)-1):
            index1, index2 = order[i], order[i+1]
            d += self.Delay[index1][index2]
        return d


    def delaytest(self):
        return lambda life: self.delay(life.gene)


    # fitness function
    def matchFun(self):
        return lambda life: 1.0 / self.cost(life.gene)

    # run GA for n iteration times
    def run(self, n=0):
        c = []
        d = []
        # iteration = [i for i in range(n)]
        while n > 0:

            self.ga.next()
            cost = self.cost(self.ga.best.gene)
            delay = self.delay(self.ga.best.gene)
            c.append(cost)
            d.append(delay)
            #print(("%d : %f") % (self.ga.generation-1, cost))
            #print(self.ga.best.gene)
            #print("\nthe end-to-end delay is:", self.delay(self.ga.best.gene))
            n -= 1
        #print("after %d times of iteration, the least cost is; %f" % (self.ga.generation-1, cost))
        #print("QoS routing order (node0 is the sink node: ",)

       # for i in self.ga.best.gene:
            #self.delaytest(i)
           # print('node%i->'%i, end=' ')
        #print("\nthe end-to-end delay is:", self.delay(self.ga.best.gene))
        # fig, ax = plt.subplots()
        # plt.xlabel("iteration times")
        # plt.ylabel("cost/delay")
        # ax.plot(iteration, c, '--', label='end-to-end cost')
        # ax.plot(iteration, d, '-', label='end-to-end delay')

        # update cost and delay of each iteration
        self.C = c
        self.D = d


# main function for one routing process with and without time requirement
def main(it = 0):
    iteration = [i for i in range(it)]
    # without time requirement
    tsp = TSP(aLifeCount=100, aDelayRequest=-1)
    tsp.run(it)
    C1 = tsp.C
    D1 = tsp.D
    fig1, ax1 = plt.subplots()
    plt.xlabel("iteration times")
    plt.ylabel("utility value/delay")
    ax1.plot(iteration, C1, '--', label='end-to-end cost')
    ax1.plot(iteration, D1, '-', label='end-to-end delay')
    legend = ax1.legend()
    plt.show()

    # with time requirement
    tsp2 = TSP(aLifeCount=100, aDelayRequest=20)
    tsp2.run(it)
    C2 = tsp2.C
    D2 = tsp2.D
    fig2, ax2 = plt.subplots()
    plt.xlabel("iteration times")
    plt.ylabel("utility value")
    ax2.plot(iteration, C1, '--', label='end-to-end cost without time requirement')
    ax2.plot(iteration, C2, '-', label='end-to-end cost with time requirement')
    legend = ax2.legend()
    plt.show()
    fig3, ax3 = plt.subplots()
    plt.xlabel("iteration times")
    plt.ylabel("end-to-end time delay")
    ax3.plot(iteration, D1, '--', label='end-to-end delay without time requirement')
    ax3.plot(iteration, D2, '-', label='end-to-end delay with time requirement')
    legend = ax3.legend()
    plt.show()

# population and iteration test
def mainPop(it=0, pop=0):
    tsp = TSP(aLifeCount=pop, aDelayRequest=-1)
    tsp.run(it)
    cost = tsp.C
    return cost[-1]


if __name__ == '__main__':

    # run 100x33 times of GA-population test and calculate the average of 33 times to determine optimal population
    popu = []
    for p in range(100, 1000, 50):
        pu = []
        for i in range(33):
            pu.append(mainPop(200, p))
        popu.append(np.mean(pu))
    x = [i for i in range(100, 1000, 50)]
    fig, ax = plt.subplots()
    plt.xlabel("initialized population")
    plt.ylabel("average end-to-end cost utility")
    ax.plot(x, popu, '-', label='end-to-end cost')

    # ax.plot(iteration, D1, '-', label='end-to-end delay')
    legend = ax.legend()
    plt.show()

    # run 100x33 times of GA-iteration test and calculate the average to determine the optimal iteration time
    x = [i for i in range(100, 1000, 50)]
    iteru =[]
    for it in range(100, 1000, 50):
        iu=[]
        for i in range(33):
            iu.append(mainPop(it, 100))
        iteru.append(np.mean(iu))
    fig1, ax1 = plt.subplots()
    plt.xlabel("iteration times")
    plt.ylabel("average end-to-end cost utility")
    ax1.plot(x, iteru, '-', label='end-to-end cost')
    # ax.plot(iteration, D1, '-', label='end-to-end delay')
    legend = ax1.legend()
    plt.show()

