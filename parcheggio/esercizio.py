from posto_mezzo import *

class Parcheggio:
    def __init__(self):
        self.__postiAutoLiberi = 1000
        self.__postiMotoLiberi = 200
        self.__guadagno = 0
    
    def __str__(self):
        return str(self.__dict__)
     
    def __repr__(self):
        return str(self.__dict__)
    
    @property
    def postiAutoLiberi(self):
        return self.__postiAutoLiberi

    @property
    def postiMotoLiberi(self):
        return self.__postiMotoLiberi
    
    @property
    def guadagno(self):
        return self.__guadagno
    
    def parcheggia(self , veicolo:Veicolo):
        if type(veicolo) == Auto and self.__postiAutoLiberi != 0:
            self.__postiAutoLiberi -= 1
            orePermanenza = datetime.datetime.today() - veicolo.dataOraFine
            saldoDaPagare = orePermanenza.hour() * 1.5
        
        elif type(veicolo) == Moto and self.__postiMotoLiberi != 0:
            self.__postiMotoLiberi -= 1
            orePermanenza = datetime.datetime.today() - veicolo.dataOraFine
            saldoDaPagare = orePermanenza.hour() * 1.2
        
        else:
            raise ValueError('Non abbiamo posti liberi per quel veicolo')
        
        self.__guadagno += saldoDaPagare
        return f'Si devono pagare {saldoDaPagare} euro'


















