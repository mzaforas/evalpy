import random

####################
# Class Population #
####################
class Population:
    def __init__(self, selector):
        self.selector = selector
        self.individuals = list()

    def __len__(self):
        return len(self.individuals)

    # Obtener individuo
    def getIndividual(self, i):
        return self.individuals[i]

    # Poner nuevo individuo en la poblacion
    def addIndividual(self, individual):
        self.individuals.append(individual)

    # Mover individuos de la poblacion dada a esta
    def addIndividuals(self, auxPopulation):
        self.individuals.extend(auxPopulation.individuals)
        auxPopulation.individuals=[]

    # Seleccionar padres. De momento aleatoriamente TODO meter algo mas sofisticado
    def select(self):
        return self.selector(self)

    def __str__(self):
        #return str(self.individuals)
        aux = str()
        for individual in self.individuals:
            aux = aux + str(individual) + ' Fit: ' + str(individual.getFitness())+'\n'
        return aux
    
    # Ordenar individuos por fitness
    def sortIndividuals(self):
        self.individuals.sort(cmp=self.fitnessCmp)
        
    def fitnessCmp(self, a, b):
        if a.getFitness() == b.getFitness():
            return 0
        if a.getFitness() > b.getFitness():
            return -1
        if a.getFitness() < b.getFitness():
            return 1

    # Mover la mitad peor de la poblacion a la poblacion dada
    def removeWorst(self, auxPopulation):
        auxPopulation.individuals = self.individuals[len(self.individuals)/2:]
        self.individuals = self.individuals[:len(self.individuals)/2]

    # Devuelve el mejor individuo
    def getBest(self):
        self.sortIndividuals()
        return self.individuals[0]

    # Devuelve el peor individuo
    def getWorst(self):
        self.sortIndividuals()
        return self.individuals[len(self.individuals)-1]

    # Devuelve el fitness medio de la poblacion
    def getAvgFitness(self):
        acum=0
        for individual in self.individuals:
            acum=acum+individual.getFitness()
        return acum/len(self.individuals)

    # Evalua la poblacion (discriminando si es necesario)
    def evaluate(self):
        for individual in self.individuals:
            individual.evaluate()
                
