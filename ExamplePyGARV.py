from PyGARV import *

"""
This class implements a Genetic Algorithm to maximize the following
function.

max f = 20x + 60y

subject to:

30x + 20y >= 2700
5x + 10y <= 850
x + y >= 95
x, y >= 0
"""
class Example(PyGARV):

    def __init__(self):
        #You can find out what each parameter does
        #looking at the source code of PyGARV class.
        super().__init__( popSize = 60,
                          values = 2, 
                          mutationRate = 0.1, #10%
                          fullMutation = True,
                          symmetricCut = True,
                          crossoverRate = 1,
                          elitism = 0.3, #30%
                          digits = 6 )
                            
    def fitness(self, chromosome):
        #gets the first integer value stored on the chromosome and divides
        #it by 100 to change the value to a float with two decimal places.
        x = chromosome[0]/100

        #gets the second integer value stored on the chromosome and divides
        #it by 100 to change the value to a float with two decimal places.
        y = chromosome[1]/100
        
        #computes the funciont to be maximized.
        f = 20*x + 60*y
        
        if(
            30*x + 20*y >= 2700 and
            5*x + 10*y <= 850 and
            x + y >= 95 and
            x > 0 and
            y > 0
        ):
            #the f value will be used as a rating for the chromosome. As bigger
            #value assumes better will be the rating of this specific chromosome.
            #IMPORTANT NOTE: the rating value can never be zero.
            rating = f

            
        else:
            #it's not permited to have chromosomes that dont respect the restrictions
            #so, if any restriction is broken the chromosome is severily penalized.
            
            rating = 1/(f+1) #IMPORTANT NOTE: the rating value can never be zero.


        #the fitness function always must returns the
        #chromosome being assesed and it's rating value
        return [chromosome, rating] 
        

    def finishedGA(self, bestChromosome):
        #gets the first integer value stored on the best chromosome
        #created by the Genetic Algorithm after all generations.
        x = bestChromosome[0]/100
            
        #gets the second integer value stored on the best chromosome
        #created by the Genetic Algorithm after all generations.
        y = bestChromosome[1]/100
        
        print("x: %f    y: %f    max(f): %f" % (x, y, (20*x + 60*y)))


garv = Example()
garv.runGA(1000) #runs the Genetic Algorithm for 1000 generations
