from PyGARV import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
This class implements a Genetic Algorithm to maximize the following
function. The result evolution is shown using a graph.

max f = 20x + 60y

subject to:

30x + 20y >= 2700
5x + 10y <= 850
x + y >= 95
x, y >= 0
"""
class Example(PyGARV):

    def __init__(self):
        #You can find out what each parameter do
        #looking at the source code of PyGARV class.
        super().__init__( popSize = 60,
                          values = 2, 
                          mutationRate = 0.5, #10%
                          fullMutation = True,
                          symmetricCut = True,
                          crossoverRate = 1,
                          elitism = 0.3, #30%
                          digits = 6 )
         
        self.maxF = []
               
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
        self.x = bestChromosome[0]/100
            
        #gets the second integer value stored on the best chromosome
        #created by the Genetic Algorithm after all generations.
        self.y = bestChromosome[1]/100
        
        self.maxF.append(20*self.x + 60*self.y)
        #print(self.maxF)
        print("x: %f    y: %f    max(f): %f" % (self.x, self.y, self.maxF[-1]))
        #input()


garv = Example()
c = 0
y = []
def animate(i):
	global c, garv
	
	c = c + 1
	garv.runGA(1)
	plt.cla()
	plt.plot(garv.maxF)
	
	if c == 1000:
		garv.interruptGA()
		
		
	
ani = FuncAnimation(plt.gcf(), animate, 1)
plt.show()
