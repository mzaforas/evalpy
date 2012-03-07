from problem import *

##################
# Class Griewank #
##################
class Griewank(Problem):
    def __init__(self, size):
        self.lower = -600.0
        self.upper = 600.0
        self.size = size

    def describe(self):
        return "Griewank"

    def objective(self, individual):
        score = 1
        prod  = 1.0
        for i in range(len(individual)):
            score += (individual.getGene(i)**2) / 4000.0
            prod  *= math.cos(individual.getGene(i) / math.sqrt(i + 1.0))
        score -= prod
        return 1 / (score+1)

    def initialize(self, individual):
        initializers.uniform(individual)
