#!/usr/bin/env python

#import psyco
#psyco.full()

import random 
import sys

sys.path.append('genomes/') 
sys.path.append('problems/') 


from algorithm import Algorithm
from population import Population
from terminator import Terminator
from logger import Logger
import crossovers
import mutators
import selectors
from arrayGenome import ArrayGenome
import techniques


# Config file
if len(sys.argv) < 2:
    execfile('config.py')
else:
    execfile(sys.argv[1])

# Problem's definition
execfile("problems/"+problemName.lower()+".py")

# TODO optimizar esto para carga dinamica
if problemName == 'Griewank':
    problem = Griewank(problemSize)
if problemName == 'Rastrigin':
    problem = Rastrigin(problemSize)
if problemName == 'TSP':
    problem = TSP(dataset,optimun)


logger = Logger(logger_level)
genome = ArrayGenome(problem.size, problem.lower, problem.upper)
techniqueSet = []

# Technique's definition 
if 'RealUCUM' in techs:
    techniqueSet.append(techniques.Genetic('RealUCUM','RealEncoding',genome,problem.initialize,problem.objective,logger,crossovers.uniform,mutators.uniform,0.9,0.01))
if 'RealBCUM' in techs:
    techniqueSet.append(techniques.Genetic('RealBCUM','RealEncoding',genome,problem.initialize,problem.objective,logger,crossovers.blend,mutators.uniform,0.9,0.01))
if 'RealUCGM' in techs:
    techniqueSet.append(techniques.Genetic('RealUCGM','RealEncoding',genome,problem.initialize,problem.objective,logger,crossovers.uniform,mutators.gaussian,0.9,0.01))
if 'RealBCGM' in techs:
    techniqueSet.append(techniques.Genetic('RealBCGM','RealEncoding',genome,problem.initialize,problem.objective,logger,crossovers.blend,mutators.gaussian,0.9,0.01))

# Build algorithm and evolve
algorithm = Algorithm(Terminator(fitnessEvals), selectors.uniform, problem, populationSize, techniqueSet, logger)
algorithm.evolve()

logger.printResult(algorithm, problem)
