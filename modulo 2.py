import random
from module_1 import Speciex


class Ambiente:
    def __init__(self, epoca: int, generazione: int):
        self.epoca = epoca
        self.generazione = generazione
        self.organismi = []

        #fattori ambientali:
        self.temperatura = 0
        self.boh = 9
        self.bohh = 0


    def add_organism(self, organism: Speciex):
        self.organismi.append(organism)


    #forse è inutile questa funzione
    def copy_preview(self, preview):
        self.organismi = []
        for organism in preview.organismi:
            self.organismi.append(organism)
        return self.organismi



def next_ambiente(preview: Ambiente):
    next_epoca = preview.epoca + 3
    next_generazione = preview.generazione + 1
    next_amb = Ambiente(next_epoca, next_generazione)
    next_amb.organismi = preview.organismi
    next_amb.temperatura = preview.temperatura
    next_amb.boh = preview.boh
    next_amb.bohh = preview.bohh
    return next_amb


#organismo è di generation precedente a altro_organismo?
def confronto_generazioni(organismo: Speciex, altro_organismo: Speciex):
    if organismo.generation < altro_organismo.generation:
        output = True
    else:
        output = False
    return output



def accoppiamenti(amb: Ambiente):
    male = 'a'
    female = 'b'
    return male, female


#morte organismo con .pop dalla lista


#non so perché mi runna tutto il codice del modulo precedente (tutti gli esempielli)
print('')
print('')
print('')
luca = Speciex('AAAAAAAATA', False, 1, 5 )
lucy = Speciex('CCCTCCCCCC', True, 2, 0)
casa = Ambiente(0, 0)
casa2 = next_ambiente(casa)
print(casa2.generazione)
print('')
print(confronto_generazioni(luca, lucy))
print('')
casa.add_organism(luca)
casa.add_organism(lucy)
print(casa.organismi)
print('') #da sistemare!!!
print(casa2.epoca)
print(casa2.organismi)
print(accoppiamenti(casa))