import time
import math
import population
import individual

###################
# Class Algorithm #
###################
class Algorithm:
    def __init__(self, terminator, selector, problem, populationSize, techniqueSet, logger):
        self.terminator = terminator
        self.problem = problem
        self.techniqueSet = techniqueSet
        self.logger = logger
        self.population = population.Population(selector)
        self.auxPopulation = population.Population(selector)

        # Rellenamos la poblacion
        for technique in techniqueSet:
            for i in range(populationSize / len(techniqueSet)):
                _individual = individual.Individual(technique)
                technique.initialize(_individual.getDefaultGenome())
                self.population.addIndividual(_individual)

        # Por el problema de redondeo, rellenamos los ultimos individuos
        for i in range(populationSize % len(techniqueSet)):
            _individual = individual.Individual(technique)
            technique.initialize(_individual.getDefaultGenome())
            self.population.addIndividual(_individual)

        # Evaluamos el fitness de la poblacion
        self.population.evaluate()
             
        # Construimos la poblacion auxiliar hueca (individuos sin inicializar)
        for i in range(populationSize):
            _individual = individual.Individual(technique)
            self.auxPopulation.addIndividual(_individual)

        self.generation = 0

    # Evolucionar
    def evolve(self):
        self.logger.initTime = time.time()
        self.initParticipation()
        while not self.done():
            self.logger.printPopulation(self)
            self.step()
            self.updateParticipation()
            self.generation = self.generation + 1
        self.logger.printPopulation(self)
        self.logger.endTime = time.time()

    # Convergencia alcanzada
    def done(self):
        return self.terminator.done(self)

    # Evolucionar una generacion
    def step(self):
        offset = 0
        for technique in self.techniqueSet:
            size = int(math.floor(len(self.auxPopulation)*technique.participation))
            offset = offset + technique.offspring(self.population, self.auxPopulation, size, offset)
        if offset < len(self.auxPopulation):
            self.techniqueSet[-1:][0].offspring(self.population, self.auxPopulation, len(self.auxPopulation)-offset, offset)
        self.population.addIndividuals(self.auxPopulation)
        self.population.sortIndividuals()
        self.population.removeWorst(self.auxPopulation)

    # Iniciar los ratios de participacion
    def initParticipation(self):
        participation = 1.0 / float(len(self.techniqueSet))
        for technique in self.techniqueSet:
            technique.participation = participation
    
    # Actualizar los ratios de participacion
    def updateParticipation(self):
        acumQuality = 0.0
        for technique in self.techniqueSet:
            acumQuality += technique.quality
        for technique in self.techniqueSet:
            technique.participation = technique.quality / acumQuality

