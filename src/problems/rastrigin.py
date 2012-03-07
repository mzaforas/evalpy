from problem import *

###################
# Class Rastrigin #
###################
class Rastrigin(Problem):
    def __init__(self, size):
        self.lower = -5.12
        self.upper = 5.12
        self.size = size

    def describe(self):
        return "Rastrigin"

    def objective(self, individual):
        result = 10.0 * len(individual)
        for i in range(len(individual)):
            result = result+(math.pow(individual.getGene(i),2)-10*math.cos(2*math.pi*individual.getGene(i)))
        return 1/(result+1)

    def initialize(self, individual):
        for i in range(len(individual)):
            individual.setGene(i,random.uniform(self.lower,self.upper))
