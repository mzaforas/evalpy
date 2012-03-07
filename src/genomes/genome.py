################
# Class Genome #
################
class Genome:
    """Abstraccion de un genoma"""

    def __init__(self):
        self.fitness = 0
        self.evaluated = False

    def setFitness(self, fitness):
        self.fitness = fitness
        self.evaluated = True

    def getFitness(self):
        return self.fitness

    def isEvaluated(self):
        return self.evaluated
