from veicolo import *
from auto import *
from moto import *
import datetime

class PostoMezzo:
    def __init__(self , occupato:bool=False , occupante:Veicolo=None , dataOraFine:datetime.datetime=None):
        self.__occupato = occupato
        #------------------------------------------------------------------
        if occupato == True and occupante != None:
            self.__occupante = occupante
        elif occupato == False and occupante != None:
            raise ValueError('Il parcheggio non è occupato')
        elif occupato == True and occupante == None:
            raise ValueError('Il parcheggio da chi è occupato?')
        #------------------------------------------------------------------
        if occupato:
            if dataOraFine > datetime.datetime.now():
                self.__dataOraFine = dataOraFine
            else:
                self.__occupato = False
                self.__occupante = None
                self.__dataOraFine = None
        else:
            if dataOraFine == None:
                self.__dataOraFine = dataOraFine
            else:
                raise ValueError('Il parcheggio non è occupato')
    
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
    
    @property
    def occupato(self):
        return self.__occupato
    @property
    def occupante(self):
        return self.__occupante
    @property
    def dataOraFine(self):
        return self.__dataOraFine
    
    @occupato.setter
    def occupato(self,nuovoOccupato):
        self.__occupato = nuovoOccupato
        return
    @occupante.setter
    def occupante(self,nuovoOccupante):
        self.__occupante = nuovoOccupante
        return
    @dataOraFine.setter
    def occupato(self,nuovaDataOraFine):
        self.__dataOraFine = nuovaDataOraFine
        return 
    
    def parcheggia(self , veicolo:Veicolo, dataOraFine):
        if self.__occupato == False:
            self.__occupato = True
            self.__occupante = veicolo
            if dataOraFine > datetime.datetime.now():
                self.__dataOraFine = dataOraFine
            else:
                raise ValueError ('Data e ora non valide')
        else:
            return 'Posto Occupato'
    def targaOccupante(self):
        if self.__occupato == True:
            return self.__occupante.targa
        else:
            return 'Parcheggio libero'
    def termineOccupazione(self):
        if self.__occupato == True:
            return self.__dataOraFine
        else:
            return 'Parcheggio libero'
    def liberaParcheggio(self , autoDaEliminare):
        if self.__occupante == autoDaEliminare:
            self.__occupato = False
            self.__occupante = None
            self.__dataOraFine = None
            return 'posto Liberato'
    
#---------------------------------------
if __name__ == '__main__':
    veicolo1 = Auto(targa='PR000VA') 
    posto = PostoMezzo(occupato=True , occupante=veicolo1 , dataOraFine=datetime.datetime(2025 , 1 , 31 , 16 , 47 , 0))
    print(posto)
    print(posto.targaOccupante())
    print(posto.termineOccupazione())
    print(posto.liberaParcheggio(veicolo1))
    print(posto)
            











