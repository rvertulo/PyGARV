import PyGARV as pygarv

"""
max: 20x + 60y

30x + 20y >= 2700
5x + 10y <= 850
x + y >= 95
x, y >= 0
"""


class Example_PyGARV(pygarv.PyGARV):
    def __init__(self):
        super().__init__(popSize=60,
                         values=2,
                         mutationRate=0.1,
                         fullMutation=True,
                         symmetricCut=True,
                         elitism=0.3,
                         digits=6)

    def fitness(self, chromosome):
        x = int(int(chromosome[0]) / 100)
        y = int(int(chromosome[1]) / 100)

        f = (20 * x) + (60 * y)

        if(
            30 * x + 20 * y >= 2700 and
            5 * x + 10 * y <= 850 and
            x + y >= 95 and
            x >= 0 and
            y >= 0
        ):

            rating = f

        else:

            rating = 1 / (f + 1)

        return [chromosome, rating]

    def finishedGeneration(self, bestChromosome):
        x = int(int(bestChromosome[0]) / 100)
        y = int(int(bestChromosome[1]) / 100)

        f = (20 * x) + (60 * y)

        print("x: %f   y: %f   f: %f)" % (x, y, f))


pygarv = Example_PyGARV()
pygarv.runGA(500)
