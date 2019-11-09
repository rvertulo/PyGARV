import PyGARV as pygarv

"""
max: 120x + 160y

x + 1,5y <= 150
4x + 3y <= 360
x, y >= 0
"""


class Example_PyGARV(pygarv.PyGARV):
    def __init__(self):
        super().__init__(popSize=40,
                         values=2,
                         mutationRate=0.15,
                         fullMutation=True,
                         symmetricCut=True,
                         elitism=0.1,
                         digits=6)

    def fitness(self, chromosome):
        x = int(int(chromosome[0]) / 100)
        y = int(int(chromosome[1]) / 100)

        f = (120 * x) + (160 * y)

        if(x + 1.5 * y > 150 or
           4 * x + 3 * y > 360 or
           x < 0 or
           y < 0):

            rating = 1 / (f + 0.001)

        else:

            rating = f + 10000

        return [chromosome, rating]

    def finishGeneration(self, getBestChromosome):
        x = int(int(getBestChromosome[0]) / 100)
        y = int(int(getBestChromosome[1]) / 100)

        f = (120 * x) + (160 * y)

        print("x: %f   y: %f   f: %f)" % (x, y, f))


pygarv = Example_PyGARV()
pygarv.runGA(500)

bc = pygarv.getBestChromosome()
x = int(int(bc[0]) / 100)
y = int(int(bc[1]) / 100)

result = (120 * x + 160 * y)

print("X: %s, Y: %s" % (x, y))
print(result)
