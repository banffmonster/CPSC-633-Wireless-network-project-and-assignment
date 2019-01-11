import math
#
# alpha = 1
# maxdic = { 'distance':  70,
#            'quality': 10
# }
# min = {'distance': 0,
#         'quality': 0}
# class Serviceprovider:
#     alpha = 1
#     max_distance = 70
#     max_time = 24
#     max_quality = 10
#
#     min_distance = 0
#     min_time = 0
#     min_quality = 0
#
#     def __init__(self, type, distance, quality, time):
#         self.type = type
#         self.quality = quality
#         self.time = time
#         self.distance = distance
#
#
#     def get_utility(self):
#         for
#
#
#
#         return utility
#
#
#
#     def u(self, min, max, x):
#        beta = self.alpha*(max-x)/(x-min)

alpha = 1

max_distance = 100
max_time = 25
max_quality = 31


medium_distance = 35
medium_time = 12
medium_quality = 15


min_distance = -1
min_time = -1
min_quality = -1


min_alpha = 0
medium_alpha = 50
max_alpha = 100

min_beta = 0
medium_beta = 50
max_beta = 100

min_energy = 29
medium_energy = 40
max_energy = 51

max_cost = 91
medium_cost = 70
min_cost = 49

def ux(x, max, medium, min):
    #print(x)
    #print(x)
    u = 0
    beta = alpha*(max - medium)/(x - min)
    if x <= min:
        u = 0
    elif x > min and  x < medium:
        u = 1/(1 + math.exp(alpha*(medium-x)/(x-min)))
    elif x > medium and x < max:
        u = 1 - 1/(1 + math.exp(beta*(x - medium)/(max - x)))
    elif x >= max:
        u = 1

    return u

def utility(distance, quality):

    uty = 0.5*(1- ux(distance, max_distance, medium_distance, min_distance)) + 0.5*ux(quality, max_quality, medium_quality, min_quality)

    #print('uty:', uty)
    return uty


def utility2(a, b):

   uty = a/(a+0.1 *b)
   return uty

def utilitycost(cost, energyi, energyj):
    #print(cost, energyi, energyj)
    uty = 0.5*ux(cost, max_cost, medium_cost, min_cost) + 0.25*ux(energyi, max_energy, medium_energy, min_energy) + 0.25*ux(energyj, max_energy, medium_energy, min_energy)
    return uty

#print(utility2(1,50))





