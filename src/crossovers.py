import random

#####################
# Uniform crossover #
#####################
def uniform(dad, mom, child1, child2):
    for i in range(len(dad)):
        if random.getrandbits(1):
            child1.setGene(i,mom.getGene(i))
            if child2:
                child2.setGene(i,dad.getGene(i))
        else:
            child1.setGene(i,dad.getGene(i))
            if child2:
                child2.setGene(i,mom.getGene(i))

###################
# Blend crossover #
###################
def blend(dad, mom, child1, child2):
    dist = 0
    for i in range(len(dad)):
        if mom.getGene(i) > dad.getGene(i):
            dist = mom.getGene(i) - dad.getGene(i)
            lo = dad.getGene(i) - 0.5 * dist
            up = mom.getGene(i) + 0.5 * dist
        if mom.getGene(i) <= dad.getGene(i):
            dist = dad.getGene(i) - mom.getGene(i)
            lo = mom.getGene(i) - 0.5 * dist
            up = dad.getGene(i) + 0.5 * dist
            
        if lo < dad.lower:
            lo = dad.lower

        if up > dad.upper:
            up = dad.upper

        child1.setGene(i,random.uniform(lo,up))
        if child2:
            child2.setGene(i,random.uniform(lo,up))
