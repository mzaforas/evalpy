from genome import Genome

#####################
# Class ArrayGenome #
#####################
class ArrayGenome(Genome):
    """Abstraccion de un genome como un array"""
    
    def __init__(self, size, lower, upper):
        Genome.__init__(self)
        self.lower = lower
        self.upper = upper
        self.genome = [0]*size

    # Crear y devolver un nuevo individuo clonado de este
    def clone(self):
        cloned = ArrayGenome(len(self), self.lower, self.upper)
        for i in range(len(self)):
            cloned.setGene(i, cloned.getGene(i))
        return cloned

    # Heredar el genoma integro del individuo dado
    def inherit(self, originIndividual):
        for i in range(len(self)):
            self.setGene(i, originIndividual.getGene(i))
        self.Fitness = originIndividual.getFitness()
        self.evaluated = True

    def getGene(self, i):
        return self.genome[i]

    def setGene(self, i, value):
        self.genome[i]=value

    def __len__(self):
        return len(self.genome)

    def __str__(self):
        return "Array genome: "+str(map(lambda n: str(round(n,3)),self.genome))
        
