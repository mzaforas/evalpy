################
# Class Logger #
################
class Logger:
    def __init__(self,level):
        self.level = level
        self.numCross = 0
        self.numMut = 0
        self.numEval = 0
        self.initTime = 0
        self.endTime = 0

    def printPopulation(self, algorithm):
        population = algorithm.population
        generation = algorithm.generation
        pList = []
        qList = []
        for technique in algorithm.techniqueSet:
            pList.append(str(round(technique.participation,3)))
            qList.append(str(round(technique.quality,3)))
        if self.level == 'debug' or self.level == 'only_stats':
            print ">> Gen "+str(generation)+": [min=%.5f, avg=%.5f, max=%.5f], part=%s, quality=%s" % (population.getWorst().getFitness(),population.getAvgFitness(),population.getBest().getFitness(),pList,qList)

        if self.level == 'debug':
            print ">> Population:"
            print population

        if self.level == 'none':
            pass

    def printIndividual(self, individual, comment):
        if self.level == 'debug':
            print ">> Individual:", comment
            print individual

        if self.level == 'only_stats':
            pass

        if self.level == 'none':
            pass

    def printResult(self, algorithm, problem):
        bestIndividual = algorithm.population.getBest()
        print
        print 'Problem  :', problem.describe()
        print 'Size     :', problem.size
        print 'Pop size :', len(algorithm.population)
        print
        print 'Time    :', self.endTime - self.initTime
        print 'Fitness :', problem.objective(bestIndividual.getDefaultGenome())
        print 'Best    :', bestIndividual
        print
        print 'Stats:'
        print ' Generations :', algorithm.generation
        print ' Evaluations :', self.numEval
        print ' Crossovers  :', self.numCross
        print ' Mutations   :', self.numMut

