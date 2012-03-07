####################
# Class Individual #
####################
class Individual:
    """Abstraccion de un individuo MOS"""

    def __init__(self, technique):
        self.technique = technique
        self.encodingSet = dict({ technique.getGenomeType() : technique.getGenome() })

    def setFitness(self, fitness):
        self.encodingSet[self.technique.getGenomeType()].setFitness(fitness)

    def getFitness(self):
        return self.encodingSet[self.technique.getGenomeType()].getFitness()

    def isEvaluated(self):
        return self.encodingSet[self.technique.getGenomeType()].isEvaluated()

    def evaluate(self):
        if not self.isEvaluated():
            self.setFitness(self.technique.evaluate(self.encodingSet[self.technique.getGenomeType()]))

    def getDefaultGenome(self):
        return self.encodingSet[self.technique.getGenomeType()]

    def __str__(self):
        return "MOS Individual -> "+str(self.encodingSet[self.technique.getGenomeType()])

