# -*- coding: utf-8 -*-

import random
from life import Life


class GA(object):
    # class GA

    def __init__(self, aCrossRate, aMutationRate, aLifeCount, aGeneLength, aDelayReq, aMatchFun=lambda life: 1, aDelayFun = lambda life: 1):
        self.crossRate = aCrossRate  # cross rate
        self.mutationRate = aMutationRate  # mutation rate
        self.lifeCount = aLifeCount  # population number
        self.delayReq = aDelayReq
        self.geneLength = aGeneLength  # genelength
        self.matchFun = aMatchFun  # fitness function
        self.delayFun = aDelayFun
        self.lives = []  # population
        self.best = None  # the best life in the population
        self.generation = 1  #
        self.crossCount = 0  #
        self.mutationCount = 0  #
        self.bounds = 0.0  #

        self.initPopulation()  #

    def initPopulation(self):
        # initialize population
        n = 0
        self.lives = []
        if self.delayReq == -1:
            # no delay requirement
            for i in range(self.lifeCount):

                gene = [j+1 for j in range(self.geneLength-1)]
                # shuffle the gene
                random.shuffle(gene)
                # add node0 at the end
                gene.append(0)
                life = Life(gene)
                # put this gene into population
                self.lives.append(life)
        else:
            # delay requirement
            n = 0
            while n < self.lifeCount:
                gene = [j + 1 for j in range(self.geneLength - 1)]

                random.shuffle(gene)
                gene.append(0)
                life = Life(gene)

                # elimination
                if self.delayFun(life) < self.delayReq:
                    self.lives.append(life)
                    n += 1


    def judge(self):
        # evaluation population

        self.bounds = 0.0

        self.best = self.lives[0]
        for life in self.lives:
            life.score = self.matchFun(life)
            self.bounds += life.score
            # get the best one
            if self.best.score < life.score:
                self.best = life

    def cross(self, parent1, parent2):
        # cross

        index1 = random.randint(0, self.geneLength - 1)
        index2 = random.randint(index1, self.geneLength - 1)
        tempGene = parent2.gene[index1:index2]
        newGene = []
        p1len = 0
        for g in parent1.gene:
            if p1len == index1:
                newGene.extend(tempGene)
                p1len += 1
            if g not in tempGene:
                newGene.append(g)
                p1len += 1
        self.crossCount += 1
        return newGene

    def mutation(self, gene):
        # mutation

        index1 = random.randint(0, self.geneLength - 1)
        index2 = random.randint(0, self.geneLength - 1)
        # swap
        gene[index1], gene[index2] = gene[index2], gene[index1]

        self.mutationCount += 1
        return gene

    def getOne(self):
        # select an individual

        r = random.uniform(0, self.bounds)
        for life in self.lives:
            r -= life.score
            if r <= 0:
                return life

        raise Exception("selection error", self.bounds)

    def newChild(self):
        #get a new child
        parent1 = self.getOne()
        rate = random.random()

        # cross based on rate
        if rate < self.crossRate:

            parent2 = self.getOne()
            gene = self.cross(parent1, parent2)
        else:
            gene = parent1.gene

        # mutate based on rate
        rate = random.random()
        if rate < self.mutationRate:
            gene = self.mutation(gene)

        return Life(gene)

    def next(self):
        # reproduction for next generation
        self.judge()
        newLives = []
        newLives.append(self.best)  # 把最好的个体加入下一代
        if self.delayReq == -1:
            while len(newLives) < self.lifeCount:
                newLives.append(self.newChild())
        else:
            n = 0
            while n < self.lifeCount:
                newlife = self.newChild()
                if self.delayFun(newlife) < self.delayReq:
                    newLives.append(newlife)
                    n += 1
        self.lives = newLives
        self.generation += 1
