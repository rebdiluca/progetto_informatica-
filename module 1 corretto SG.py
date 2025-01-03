import random
from abc import ABC, abstractmethod


class Species(ABC):
    pass


class Speciex(Species):
    def __init__(self, genome:str, gender_f: bool, fertility: float, generation: int):
        self.genome = genome
        bases = ["A", "C", "G", "T"]
        if not all(base in bases for base in self.genome):
            raise ValueError(f"Genome contains invalid characters: {genome}. Bases must be A, G, T, C.")
        if len(self.genome) != 10:
            raise ValueError('genome must be of 10 characters')
        self.gender_f = gender_f
        self.fertility = fertility
        self.generation = generation
        self.trait1 = self.genome[2:5]
        self.trait2 = self.genome[-3:-1]
        #dizionari:{sequenza: frequenza}



def inheritance_trait1(orga: Speciex, orgb:Speciex):
    dict_trait1 = {
        'AAA': 50,
        'CCC': 30,
        'TTT': 20
    }
    tot = dict_trait1.get(orga.trait1, 0) + dict_trait1.get(orgb.trait1, 0)
    if tot == 0:
        new1 = list('---')
    else:
        number = random.randint(1,tot)
        new1 = '---'
        if number <= dict_trait1.get(orga.trait1, 0):
            new1 = list(orga.trait1)
        elif number > dict_trait1.get(orga.trait1, 0):
            new1 = list(orgb.trait1)
    return new1



def inheritance_trait2(orga: Speciex, orgb:Speciex):
    dict_trait2 = {
        'AA': 50,
        'CC': 30,
        'TT': 20
    }
    tot = dict_trait2.get(orga.trait2, 0) + dict_trait2.get(orgb.trait2, 0)
    if tot == 0:
        new2 = list('---')
    else:
        number = random.randint(1,tot)
        new2 = '---'
        if number <= dict_trait2.get(orga.trait2, 0):
            new2 = list(orga.trait2)
        elif number > dict_trait2.get(orga.trait2, 0):
            new2 = list(orgb.trait2)
    return new2



def new_genome(orga: Speciex, orgb: Speciex):
        bases = ["A", "C", "G", "T"]
        bases = ["T"]
        new_genome = []
        for x in range(10):
            new_genome.append(random.choice(bases))
        trait1 = inheritance_trait1(orga, orgb)
        trait2 = inheritance_trait2(orga,orgb)
        new_genome[2:5] = trait1
        new_genome[-3:-1] = trait2
        return new_genome
#poi dovrò fare nuovo_organismo.genome = new_genome (e in automatico mi assegna i tratti)


def mutate(new_genome):
    bases = ["A", "C", "G", "T"]
    mutable_index = [2, 3, 4, -3, -2]
    for i in mutable_index:
        if random.randint(1, 10) < 3:
            new_base = random.choice(bases)
            while new_base == new_genome[i]:
                new_base = random.choice(bases)
            #print(i)
            #print(new_base)
            new_genome[i] = new_base
    return new_genome


#Esempielli
luca = Speciex('AAAAAAAATA', False, 1, 5 )
lucy = Speciex('CCCTCCCCCC', True, 2)
print(luca.generation)
print(lucy.generation)
print('')
print(inheritance_trait1(luca, lucy))
print('')
print(inheritance_trait2(luca, lucy))
print('')
print(new_genome(luca, lucy))
print(mutate(new_genome(luca, lucy)))
