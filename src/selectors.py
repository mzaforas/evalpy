import random

####################
# Uniform selector #
####################
def uniform(population):
    return population.getIndividual(random.randint(0,len(population)-1))


#########################
# Proportional selector #
#########################
def proportional(population):
    fitnessAcum = 0
    for ind in population.individuals:
        fitnessAcum = fitnessAcum + ind.getFitness()
        res = random.random()
        probAcum = 0
    for ind in population.individuals:
        probAcum = probAcum + ind.getFitness() / fitnessAcum
        if res <= probAcum:
            return ind
