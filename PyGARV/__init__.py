import random
import abc

""" PyGARV - Python Genetic Algorithm by Rodrigo Vertulo
    ====================================================
    
	This class provides all resources needed to develop
	Genetic Algorithms.
	
	To use this class you must create a subclass that inherits
	from this one. You also must to implement the "fitness" method
	in the subclass.
	
	
	Created by Rodrigo Cesar Vertulo
	Date: November, 7 2019
	
	Copyright(c) 2019. Rodrigo Cesar Vertulo """

__author__    = "Rodrigo C. Vertulo"
__copyright__ = "Copyright (c) 2019. Rodrigo Vertulo"
__credits__   = "Rodrigo Vertulo"
__version__   = "1.0.2"
__maintener__ = "Rodrigo Vertulo"
__email__     = "rvertulo@gmail.com"
__status__    = "beta"

class PyGARV(object):
    __metaclass__ = abc.ABCMeta

    """
    popSize: Total number of chromosomes 
    values: Quantity of values to be stored on each chromosome
    mutationRate: Probability to occur a mutation
    fullMutation: Defines if the mutation will be applied or not on all values
    symmetricCut: Defines if the cross over operation will be symmetric or not
    crossoverRate: Probability to occur the cross over operation
    elitism: Percentage of chromosomes to be included in the elitism operation
    digits: Total of digits (integer part plus fractional part) of each value stored on
            each chromosome. i.e. The number 1977,11 has 6 digits.
    """
    def __init__(self,
                 popSize = 30, 
                 values = 1, 
                 mutationRate = 0.01,
                 fullMutation = False,
                 symmetricCut = True,
                 crossoverRate = 1,
                 elitism = 0.1,
                 digits = 3):

        self.mutationRate = mutationRate
        self.fullMutation = fullMutation
        self.crossoverRate = crossoverRate
        self.symmetricCut = symmetricCut
        self.elitism = elitism
        self.digits = digits
        self.popSize = popSize
        self.values = values
        
        self.bestChromosome = None
        self.bestRating = 0
        self.stopGA = False

        self.createPopulation()
             

    def getPopulation(self):
        return self.populacao
    
        
    def getMostFrequentChromosome(self):
        maisFreq = self.populacao[0]
        contagem = 0
        
        for c in self.populacao:
            if self.populacao.count(c) > contagem:
                maisFreq = c
                
        return maisFreq
        
        
    def getBestChromosome(self):
        return self.bestChromosome

            
    def setNewPopulation(self, novaPopulacao):
        self.populacao = novaPopulacao

     
    def createPopulation(self):
        populacao = []
        
        if(self.popSize % 2 != 0):
            self.popSize = self.popSize + 1
            
        for i in range(self.popSize):
            listaValores = []
            for v in range(self.values):
                valor = random.random()
                valor = int((valor * (pow(10, self.digits))))
                listaValores.append(valor)
                
            populacao.append(listaValores)
        
        self.setNewPopulation(populacao)


    def crossover(self, cromossomo1, cromossomo2):
        if(random.random() <= self.crossoverRate):
            if(len(cromossomo1) == len(cromossomo2)):

                if(self.symmetricCut == False):
                    corte = random.randint(0, len(cromossomo1))
                else:
                    corte = int(len(cromossomo1) / 2)
				
                cromossomo1Parte1 = cromossomo1[0:corte]
                cromossomo1Parte2 = cromossomo1[corte:len(cromossomo1)]

                cromossomo2Parte1 = cromossomo2[0:corte]
                cromossomo2Parte2 = cromossomo2[corte:len(cromossomo2)]

                filho1 = cromossomo1Parte1 + cromossomo2Parte2
                filho2 = cromossomo2Parte1 + cromossomo1Parte2

                return [filho1, filho2]
            else:
                return -1
        else:
            return [cromossomo1, cromossomo2]
			
    
    def mutation(self, cromossomo):
        novocromossomo = cromossomo

        if(self.fullMutation == False):
            i = random.randint(0, len(cromossomo)-1)
            
            if(random.random() <= self.mutationRate):
                novocromossomo[i] = self.changeGene(novocromossomo[i])
                    
        else:
            for i in range(len(novocromossomo)):
                if(random.random() <= self.mutationRate):
                    novocromossomo[i] = self.changeGene(novocromossomo[i])
                            
        return novocromossomo


    def changeGene(self, gene):        
        bits = "{0:b}".format(gene)
        bits = ((8-len(bits)) * "0") + "{0:b}".format(gene)
        bits = list(bits)
        indice = random.randint(0, len(bits)-1)
        mutacao = ""
        
        if(bits[indice] == "0"): mutacao = "1"
        else: mutacao = "0"
        
        bits[indice] = mutacao
        
        bits = "".join(bits)

        gene = int(bits, 2)

        return gene


    def __sort(self,elem):
        return elem[1]
    def makeDraw(self):
        listapopulacao = sorted(self.populacao, key = self.__sort)
        avaliacoes = [n for c, n in listapopulacao]
        
        somatoria = sum(avaliacoes) 
        probabilidades = [n/somatoria for n in avaliacoes]
                                
        indicesEscolhidos = []
        for s in range(len(avaliacoes)):
            sorteio = random.random()
            aux = probabilidades[0]
            i = 1
            
            while(aux <= sorteio):
                aux = aux + probabilidades[i]
                i = i + 1
        
            indicesEscolhidos.append(i - 1)
    
        cromossomosEscolhidos = [listapopulacao[i][0] for i in indicesEscolhidos]
            
        # Aplicação do elitism. Substitui aleatoriamente elementos
        # entre os cromossomosEscolhidos pelos melhores elementos da populacao
        # antes do sorteio ter sido realizado. A quantidade de elementos
        # a serem substituidos é determinada por self.elitism.
        qtdElementosParaElitismo = int(self.elitism * len(listapopulacao))
        for i in range(qtdElementosParaElitismo):
            indiceParaSubstituicao = random.randint(0, len(cromossomosEscolhidos) - 1)
            cromossomosEscolhidos[indiceParaSubstituicao] = listapopulacao[len(listapopulacao)-i-1][0]
            
            
        #Mantém o melhor cromossomo na população
        cromossomosEscolhidos[0] = self.getBestChromosome()
    			
        self.populacao = cromossomosEscolhidos


    def assessPopulation(self):            
        populacaoAvaliada = []
        
        for c in range(len(self.getPopulation())):
            if self.stopGA == True: break
            
            cromossomo = self.getPopulation()[c]
            cromossomoAvaliado = self.fitness(cromossomo)
            populacaoAvaliada.append(cromossomoAvaliado)
            
            if(cromossomoAvaliado[1] > self.bestRating):
                self.bestRating = cromossomoAvaliado[1]
                self.bestChromosome = cromossomoAvaliado[0]
        
        self.setNewPopulation(populacaoAvaliada)
        

    @abc.abstractmethod 
    def fitness(self, cromossomo):
        pass

    def finishedGeneration(self, melhorCromossomo):
        return melhorCromossomo
        
    def finishedGA(self, melhorCromossomo):
        return melhorCromossomo

    def interruptGA(self):
        self.stopGA = True
        self.finishGeneration(self.getBestChromosome())


    def runGA(self, geracoes = 1):
        if self.stopGA == False:
            
            for g in range(geracoes):
                self.assessPopulation()
                self.makeDraw()
                
                i = 0
                random.shuffle(self.populacao)
                novaPopulacao = []

                while(i < len(self.populacao)-1):
                    cromossomo1 = self.populacao[i]
                    cromossomo2 = self.populacao[i+1]

                    filhos = self.crossover(cromossomo1, cromossomo2)
                    novaPopulacao.append(filhos[0])
                    novaPopulacao.append(filhos[1])
                    
                    i = i + 2
                
                novaPopulacaoComMutacao = []
                for c in novaPopulacao:
                    novaPopulacaoComMutacao.append(self.mutation(c))
                    
                self.populacao = novaPopulacaoComMutacao

                self.finishedGeneration(self.bestChromosome)
                
                if self.stopGA == True:
                    break
        
        self.finishedGA(self.bestChromosome)

