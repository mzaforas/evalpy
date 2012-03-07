####################
# Class Terminator #
####################
class Terminator:
    def __init__(self, fitnessEvals):
        self.fitnessEvals = fitnessEvals
#         self.acumGen = 0
#         self.generations = generations
#         self.convergence = convergence

#     def done(self, algorithm):
#         if (algorithm.population.getBest().getFitness() - algorithm.population.getWorst().getFitness()) < self.convergence:
#             if self.generations == self.acumGen:
#                 return True
#             else:
#                 self.acumGen += 1
#                 return False
#         else:
#             self.acumGen = 0
#             return False
    def done(self, algorithm):
        if (self.fitnessEvals > algorithm.logger.numEval) and (algorithm.population.getBest().getFitness() < 1.0):
            return False
        else:
            return True
