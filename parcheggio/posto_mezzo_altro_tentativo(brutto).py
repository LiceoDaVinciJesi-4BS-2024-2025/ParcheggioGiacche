from veicolo import *
from auto import *
from moto import *
import datetime

class PostoMezzo:
    def __init__(self , occupato:bool=False , occupante:Veicolo=None , dataOraArrivo:datetime.datetime=None):
        self.__occupato = occupato
        #------------------------------------------------------------------
        if occupato == True and occupante != None:
            self.__occupante = occupante
        elif occupato == False and occupante != None:
            raise ValueError('Il parcheggio non è occupato')
        elif occupato == True and occupante == None:
            raise ValueError('Il parcheggio da chi è occupato?')
        #------------------------------------------------------------------
        if dataOraArrivo == None:
            self.__dataOraArrivo = datetime.datetime.now()
        else:
            self.__dataOraArrivo = dataOraArrivo
            
    
    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return str(self.__dict__)
        
    def parcheggia(self , veicolo:Veicolo, dataOraArrivo):
        if self.__occupato == False:
            self.__occupato = True
            self.__occupante = veicolo
            self.__dataOraArrivo = dataOraArrivo
        else:
            return 'Posto Occupato'
    
    def targaOccupante(self):
        if self.__occupato == True:
            return self.__occupante.targa
        else:
            return 'Parcheggio libero'
    
    def inizioOccupazione(self):
        if self.__occupato == True:
            return self.__dataOraArrivo
        else:
            return 'Parcheggio libero'
    
#---------------------------------------
if __name__ == '__main__':
    veicolo1 = Auto(targa='PR000VA') 
    posto = PostoMezzo(occupato=True , occupante=veicolo1)
    print(posto)
    print(posto.targaOccupante())
    print(posto.inizioOccupazione())