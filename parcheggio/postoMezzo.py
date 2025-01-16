from veicolo import *
from auto import *
from moto import *
import datetime

class PostoMezzo:
    def __init__(self , occupato:bool=False , occupante:Veicolo=None , dataOraFine:datetime.datetime=None):
        self.occupato = occupato
        #------------------------------------------------------------------
        if occupato == True and occupante != None:
            self.occupante = occupante
        elif occupato == False and occupante != None:
            raise ValueError('Il parcheggio non è occupato')
        elif occupato == True and occupante == None:
            raise ValueError('Il parcheggio da chi è occupato?')
        #------------------------------------------------------------------
        if occupato:
            if dataOraFine > datetime.datetime.today():
                self.dataOraFine = dataOraFine
            else:
                self.occupato = False
                self.occupante = None
                self.dataOraFine = None 
        else:
            if dataOraFine == None:
                self.dataOraFine = dataOraFine
            else:
                raise ValueError('Il parcheggio non è occupato')
    
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
        
    def parcheggia(self , veicolo:Veicolo, dataOraFine):
        if self.occupato == False:
            self.occupato = True
            self.occupante = veicolo
            self.dataOraFine = dataOraFine
        else:
            return 'Posto Occupato'
    def targaOccupante(self):
        if self.occupato == True:
            return self.occupante.targa
        else:
            return 'Parcheggio libero'
    def termineOccupazione(self):
        if self.occupato == True:
            return self.dataOraFine
        else:
            return 'Parcheggio libero'
    
#---------------------------------------
if __name__ == '__main__':
    veicolo1 = Auto(targa='PR000VA') 
    posto = PostoMezzo(occupato=True , occupante=veicolo1 , dataOraFine=datetime.datetime(2025 , 1 , 16 , 16 , 47 , 0))
    print(posto)
    print(posto.targaOccupante())
    print(posto.termineOccupazione())
            











