import random
import math

###################
# Uniform mutator #
###################
def uniform(individual, probability):
    numMut = 0
    for i in range(len(individual)):
        if random.random() <= probability:
            upper = individual.upper
            lower = individual.lower
            individual.setGene(i,random.uniform(individual.lower,individual.upper))
            numMut += 1
    if numMut > 0:
        individual.evaluated = False
    return numMut

####################
# Gaussian mutator #
####################
def gaussian(individual, probability):
    numMut = probability * len(individual)
    
    if random.random() <= (numMut-int(numMut)):
        numMut += 1

    for i in range(int(numMut)):
        idx = random.randint(0,len(individual)-1)
        geneValue = individual.getGene(idx)

        alleleRegion = individual.upper - individual.lower
        while True:
            newValue = geneValue + unitGaussian()*alleleRegion
            if (newValue <= individual.upper and newValue >= individual.lower):
                break

        individual.setGene(idx, newValue)
    return int(numMut)

#################
# Unit Gaussian #
#################
def unitGaussian():
    while True:
        var1 = 2.0 * random.random() - 1.0
        var2 = 2.0 * random.random() - 1.0
        rsquare = var1**2 + var2**2
        if (rsquare < 1.0 and rsquare != 0.0):
            break

    val = -2.0 * math.log(rsquare) / rsquare
    if (val > 0.0):
        factor = math.sqrt(val)
    else:
        factor = 0.0
    
    return (var2 * factor)
 
