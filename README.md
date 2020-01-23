# PyGARV
PyGARV is a Python module that provides all resources needed to develop Genetic Algorithms in an easy and fast way.

Created by Rodrigo Cesar Vertulo on November 7, 2019.
<br/>
Copyright(c) 2019. Rodrigo Cesar Vertulo
<br/>
You can contact me on rvertulo@gmail.com


# **How to use the PyGARV module**
To use PyGARV module, the first thing you must to do is import it into your code. The easiest way to do it, is putting the PyGARV folder inside your project folder and use the following code.


```python
from PyGARV import *
```

The next step is create your own subclass of PyGARV class. The constructor has the following parameters:

1.   **popSize**: Total number of chromosomes
2.   **values**: Quantity of values to be stored on each chromosome
3.   **mutationRate**: Probability to occur a mutation
4.   **fullMutation**: Defines if the mutation will be applied or not on all values
5.   **symmetricCut**: Defines if the cross over operation will be symmetric or not
6.   **crossoverRate**: Probability to occur the cross over operation
7.   **elitism**: Percentage of chromosomes to be included in the elitism operation
8.   **digits**: Total of digits (integer part plus fractional part) of each value stored on each chromosome. i.e. The number 1977,11 has 6 digits.

For the example in this tutorial we are going to create the subclass in the following way:


```python
class ExamplePyGARV(PyGARV):
    def __init__(self):
        super().__init__(popSize = 60,
                         values = 2,
                         mutationRate = 0.1,
                         fullMutation = True,
                         symmetricCut = True,
                         crossoverRate = 1,
                         elitism = 0.3,
                         digits = 6)

```

The goal of this Genetic Algorithm is to maximize the following function:

f = 20x + 60y

subject to the following restrictions:

* 30x + 20y >= 2700
* 5x + 10y <= 850
* x + y >= 95
* x, y >= 0

We need to implement the superclass method called "fitness". This method has as parameter the current chromosome being processed. Inside this method we need to extract from the chromosome the values of our problem stored on it and make any calculation concerning the problem that we want to solve. The last thing we must to do inside this method is to return a list containing the chromosome processed and its rating.


```python
    def fitness(self, chromosome):
        #Gets the first integer value stored on the chromosome and divides
        #it by 100 to change the value to a float with two decimal places.
        x = chromosome[0]/100

        #Gets the second integer value stored on the chromosome and divides
        #it by 100 to change the value to a float with two decimal places.
        y = chromosome[1]/100
        
        #computes the function to be maximized.
        f = 20*x + 60*y
        
        if(
            30*x + 20*y >= 2700 and
            5*x + 10*y <= 850 and
            x + y >= 95 and
            x > 0 and
            y > 0
        ):
            #The f value will be used as a rating for the chromosome. As bigger the
            #value assumes better will be the rating of this specific chromosome.
            #IMPORTANT: the rating value can never be zero.
            rating = f
            
        else:
            #It's not permited to have chromosomes that don't respect the restrictions
            #so, if any restriction is broken the chromosome is severily penalized.
            rating = 1/(f+1) #IMPORTANT: the rating value can never be zero.

        #The fitness function always must returns the
        #chromosome being assesed and it's rating value
        return [chromosome, rating]
```

When the Genetic Algorithm finishes its processing, we need to show the result stored on the best chromosome. After the processing the superclass method called "finishedGA" is executed and inside this one we can get the final result of the processing.


```python
    def finishedGA(self, bestChromosome):
        #Gets the first integer value stored on the best chromosome
        #created by the Genetic Algorithm after all generations.
        x = bestChromosome[0]/100
            
        #Gets the second integer value stored on the best chromosome
        #created by the Genetic Algorithm after all generations.
        y = bestChromosome[1]/100
        
        print("x: %f    y: %f    max(f): %f" % (x, y, (20*x + 60*y)))

```

Now our subclass is ready to be executed. To run the Genetic Algorithm we need instantiate our subclass to create a new object from this. Then, we can execute the method "runGA" informing the number of generations we desire.


```python
pygarv = ExamplePyGARV()
pygarv.runGA(1000) #runs the Genetic Algorithm for 1000 generations
```
