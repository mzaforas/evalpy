from problem import *

#############
# Class TSP #
#############
class TSP(Problem):
    def __init__(self,dataset,optimun):
        self.dataset = dataset
        self.optimun = optimun
        # TODO parseo fichero matriz y tamaño

    def describe(self):
        return "TSP"

    def objective(self, individual):
        city_orig = individual.getGene(0)
        city_dest = individual.getGene(0)
        totaldist = self.matrix[0][individual.getGene(0)]
        for i in range(self.size):
            city_orig = individual.getGene(i-1)
            city_dest = individual.getGene(i)
            totaldist += self.matrix[city_orig][city_dest]
        totaldist += self.matrix[city_dest][0];
        return self.optimum / totaldist;

    def initialize(self, individual):
        initializers.permutation(individual)
