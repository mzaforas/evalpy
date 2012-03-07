import sys

sys.path.append('../individuals/') 
sys.path.append('../')

from arrayindividual import *
import initializers

individual = ArrayIndividual(10,1,10)
initializers.permutation(individual)
print "Permutation initializer"
print individual
print

individual = ArrayIndividual(10,0.0,5.5)
initializers.uniform(individual)
print "Uniform initializer"
print individual
