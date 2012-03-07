import random

###########################
# Permutation initializer #
###########################
def permutation(individual):
    for i in range(len(individual)):
        individual.setGene(i,i+1)
    for i in range(len(individual)):
        dest = random.choice(range(len(individual)))
        tmp = individual.getGene(dest)
        individual.setGene(dest,individual.getGene(i))
        individual.setGene(i,tmp)

#######################
# Uniform initializer #
#######################
def uniform(individual):
    for i in range(len(individual)):
        individual.setGene(i,random.uniform(individual.lower,individual.upper))
