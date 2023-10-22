class NeuronalCell: #Create a class

    def __init__(self, cell_type, soma, dendrites, axon, spines): #def __init__ is the class constructor (it allows to create the class)
        self.cell_type = cell_type #self. refers to the class created above
        self.soma = soma
        self.dendrites = dendrites
        self.axon = axon
        self.spines = spines

    def Neuron(self):
        return f"A {self.cell_type} consists of a cell body ({self.soma}) with mutliple structures called {self.dendrites} that receveie incoming signals, and projection called an {self.axon}, responsible for transmitting electrical impulses. Dendrites often adorned with small protusions know as {self.spines}"
        # return f to prin in one lign strings and results

N1 = NeuronalCell("Neuronal Cell", "soma", "dendrites", "axon", "spines")
N1.Neuron() #Pour print N1

class PyramidalNeuron(NeuronalCell): #Create a child class (class derived from the first one)

    def __init__(self, cell_type, soma, dendrites, axon, spines):
        self.cell_type = cell_type
        self.axon = axon
        self.dendrites = dendrites
        self.soma = soma
        self.spines = spines

    def Pyramidal(self):
        return f"A {self.cell_type} is a type of neuron with a {self.soma}, {self.dendrites} that receive incoming signals, and a single long {self.axon} for transmitting signals, often characterized by small protusions called {self.spines} on its dendrites."

P1 = PyramidalNeuron("Pyramidal Neuron", "triangular-shape cell body", "multiple dendrites", "single long axon", "spines")
P1.Pyramidal() #Pour print P1

class OvoidNeuron(NeuronalCell): #Create a child class (class derived from the first one)

    def __init__(self, cell_type, soma, dendrites, spines, axon):
        self.cell_type = cell_type
        self.axon = axon
        self.dendrites = dendrites
        self.soma = soma
        self.spines = spines 
    
    def Ovoid(self):
        return f"The {self.cell_type} had {self.soma} with {self.dendrites} are characterized by {self.dendrites}. We observe {self.spines} and {self.axon}"


O1 = OvoidNeuron("Ovoid Cell", "spherical to ovoid somata", "two to five thin primary dendrites", "spine-sparse dendrites", "fairly dense local axonal arborizations") #Pour print O1
O1.Ovoid()
