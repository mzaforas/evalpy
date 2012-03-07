import random

###################
# Class Technique #
###################
class Technique:
    def __init__(self, id, genomeType, genome, initializer, evaluator, logger):
        self.id = id
        self.genomeType = genomeType
        self.genome = genome
        self.initializer = initializer
        self.evaluator = evaluator
        self.logger = logger
        self.participation = 0.0
        self.quality = 0.0

    def initialize(self, individual):
        return self.initializer(individual)

    def evaluate(self, individual):
        return self.evaluator(individual)

    def getGenome(self):
        return self.genome.clone()

    def getGenomeType(self):
        return self.genomeType

#################
# Class Genetic #
#################
class Genetic(Technique):
    """Abstraccion de una tecnica basada en teoria de algoritmos geneticos"""

    def __init__(self, id, encoding, baseIndividual, initializer, evaluator, logger, crossover, mutator, crossprob, mutprob):
        Technique.__init__(self, id, encoding, baseIndividual, initializer, evaluator, logger)
        self.crossover = crossover
        self.mutator = mutator
        self.crossprob = crossprob
        self.mutprob = mutprob

    # Generar descendencia
    def offspring(self, origPop, destPop, size, offset):
        acumFitness = 0.0
        acumImprove = 0.0
        newIndividuals = 0

        for i in range(0,size,2):
            dad = origPop.select().getDefaultGenome()
            self.logger.printIndividual(dad,"dad")
            mom = origPop.select().getDefaultGenome()
            self.logger.printIndividual(mom,"mom")
            child1 = destPop.getIndividual(i+offset).getDefaultGenome()
            if (i+1) == size:
                child2 = 0
            else:
                child2 = destPop.getIndividual(i+offset+1).getDefaultGenome()

            # Cruce o herencia segun probabilidad
            if random.random() <= self.crossprob:
                self.crossover(dad,mom,child1,child2)
                child1.evaluated = False
                if child2:
                    child2.evaluated = False
                self.logger.numCross += 1
            else:
                child1.inherit(dad)
                if child2:
                    child2.inherit(mom)
            self.logger.printIndividual(child1,"child1 after crossover")
            if child2:
                self.logger.printIndividual(child2,"child2 after crossover")

            # Mutacion
            numMut = self.mutator(child1,self.mutprob)
            self.logger.numMut += numMut 
            self.logger.printIndividual(child1,"child1 after mutation")
            if child2:
                numMut = self.mutator(child2,self.mutprob)
                self.logger.numMut += numMut 
                self.logger.printIndividual(child2,"chil2 after mutation")
            
            # Reevaluacion si corresponde y acumulacion del nuevo fitness generado (mejora)
            if not child1.evaluated:
                child1.setFitness(self.evaluator(child1))
                self.logger.numEval += 1
                acumImprove += child1.getFitness() - ((dad.getFitness() + mom.getFitness()) / 2)
                newIndividuals += 1
            if child2:
                if not child2.evaluated:
                    child2.setFitness(self.evaluator(child2))
                    self.logger.numEval += 1
                    acumImprove += child2.getFitness() - ((dad.getFitness() + mom.getFitness()) / 2)
                    newIndividuals += 1

            # Acumulacion del fitness de todos los individuos
            acumFitness += child1.getFitness()
            if child2:
                acumFitness += child2.getFitness()
                    
        # Establecer nueva calidad de la tecnica tras esta generacion
        if newIndividuals:
            self.quality  += ((acumFitness / size) + (acumImprove / newIndividuals)) / 20.0
        else:
            self.quality  += (acumFitness / size) / 20.0

        return size
