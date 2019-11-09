from PyGARV import *
from Produto import *
import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, space, value):
        self.name = name
        self.space = space
        self.value = value


class Example_PyGARV(PyGARV):
    def __init__(self):
        super().__init__(popSize=20,
                         values=14,
                         mutationRate=0.03,
                         fullMutation=True,
                         symmetricCut=False,
                         elitism=0.2,
                         digits=2)

        self.lista_products = []
        self.lista_products.append(Product("Refrigerator Dako", 0.751, 999.90))
        self.lista_products.append(Product("IPhone 6", 0.0000899, 2911.12))
        self.lista_products.append(Product("TV 55", 0.400, 4346.99))
        self.lista_products.append(Product("TV 50", 0.290, 3999.90))
        self.lista_products.append(Product("TV 42", 0.200, 2999.00))
        self.lista_products.append(Product("Notebook Dell", 0.00350, 2499.90))
        self.lista_products.append(Product("Fan Panasonic", 0.496, 199.90))
        self.lista_products.append(Product("Microwave Electrolux", 0.0424, 308.66))
        self.lista_products.append(Product("Microwave LG", 0.0544, 429.90))
        self.lista_products.append(Product("Microwave Panasonic", 0.0319, 299.29))
        self.lista_products.append(Product("Refrigerator Brastemp", 0.635, 849.00))
        self.lista_products.append(Product("Refrigerator Consul", 0.870, 1199.89))
        self.lista_products.append(Product("Notebook Lenovo", 0.498, 1999.90))
        self.lista_products.append(Product("Notebook Asus", 0.527, 3999.00))

        self.maxSpace = 3
        self.values = []

    def fitness(self, chromosome):
        chromosome = self.convertToBin(chromosome)

        space = 0
        value = 0.001

        for i in range(len(chromosome)):
            if chromosome[i] == 1:
                space = space + self.lista_products[i].space
                value = value + self.lista_products[i].value


        if space > self.maxSpace:
            rating = 1 / space
        else:
            rating = value

        return [chromosome, rating]

    def finishedGeneration(self, bestChromosome):
        space = 0
        value = 0

        for i in range(len(bestChromosome)):
            if bestChromosome[i] == 1:
                space = space + self.lista_products[i].space
                value = value + self.lista_products[i].value

        self.values.append(value)


    def finishedGA(self, bestChromosome):
        space = 0
        value = 0

        for i in range(len(bestChromosome)):
            if bestChromosome[i] == 1:
                space = space + self.lista_products[i].space
                value = value + self.lista_products[i].value

        print("Space: %f    Value: %f" % (space, value))
        print(bestChromosome)

        plt.plot(self.values)
        plt.show()


pygarv = Example_PyGARV()
pygarv.runGA(300)
