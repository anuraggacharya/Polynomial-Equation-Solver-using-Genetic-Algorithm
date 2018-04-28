# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:08:39 2017

@author: Anurag Acharya
"""
import random
population_size=10
chromosomes_length=4    #dont forget to change the number of variables i.r chromosomes length given the equation
tournament_size=3
population=[]
crossover_rate=.8
mutation_rate=0.5
for i in range(population_size):
    population.append([random.randint(0,30) for i in range(chromosomes_length)])

#print("Initial Population:",population)
def evaluation(population):
    fitness=[]
    f_objective=[]
    for individual in population:
        #f_objective.append((individual[0]**3)+(individual[1]**3)+(3*individual[0]**2*individual[1])+(3*individual[0]*individual[1]**2)-27) #for cubic sustem
        #f_objective.append((individual[0]**2)-(2*individual[0]*individual[1])+(individual[1]**2)-4) #for qaudratic system
        f_objective.append(abs((individual[0]+2*individual[1]+3*individual[2]+4*individual[3])-30)) #for linear system
    #print(f_objective)

    for health in f_objective:
        fitness.append(1.0/(1+health))
    #print("Fitenss: ",fitness)
    
    return fitness

def check(fitness,population):
    for health in fitness:
        if health==1:
            print("Solution Found:")
            print(population[fitness.index(1)])
            return 1
        else: 
            return 0
            
def tournament(probablity,population):
    gen=[]
    parents=[]
    for j in range(population_size):
        team=[]
        for i in range(tournament_size):
            x=random.randint(0,population_size-1)
            team.append(probablity[x])
        gen.append(max(team))
        del team
    for parent in gen:
        parents.append(population[probablity.index(parent)])
    return parents

def selection(fitness):
    probablity=[]
    total_fitness=sum(fitness)
    for fit in fitness:
        probablity.append(fit/total_fitness)
    #print("Probablity:",probablity)
    parents=tournament(probablity,population)  
    return parents
    
def mutation(parents):
    for i in range(int(population_size*mutation_rate)):
        mutant=random.randint(0,len(parents)-1)
        #print("Mutant ",mutant)
        mutant_gene=random.randint(0,chromosomes_length-1)
        parents[mutant][mutant_gene]=random.randint(0,30)
        return parents
        
def crossover(parents):
    i=0
    cross_number=int(crossover_rate*population_size)    
    for i in range(cross_number):
        cross_location=random.randint(0,chromosomes_length-1)
        father=random.randint(0,len(parents)-1)
        mother=random.randint(0,len(parents)-1)
        #print("father %d,mother %d location=%d"%(father,mother,cross_location))
        if mother != father:
            geneF=parents[father][cross_location]
            geneM=parents[mother][cross_location]
            parents[father][cross_location]=geneM
            parents[mother][cross_location]=geneF    
    return parents
   
for i in range(5000):  
    fitness=evaluation(population)
    parents=selection(fitness)
    if check(fitness,population)==1:
        break;
    #print("After Selection, parents: ",parents)
    parents=crossover(parents)
    #print("After cross",parents)
    parents=mutation(parents)
    #print("After mutation: ",parents)
    population[:]=parents[:]
    #print(population)
    #print("-------------------------------------------")   
print("after %d generation :"%(i))
