from veicolo import *

class Auto(Veicolo):
    def __init__(self, targa, marca='Fiat', modello='Panda', colore='Giallo', cilindrata:int=1000, alimentazione='parolacce', passeggeriMax:int=4 , passeggeri:int=1 , capacitaMax:int=100 , merce:int=0):
        super().__init__(targa, marca, modello, colore, cilindrata, alimentazione)
        #-----------------------------------------------------------------
        self.__passeggeriMax = passeggeriMax
        #-----------------------------------------------------------------
        if passeggeri <= self.__passeggeriMax:
            self.__passeggeri = passeggeri
        else:
            raise ValueError('Non bastano i posti')
        #-----------------------------------------------------------------
        self.__capacitaMax = capacitaMax
        #-----------------------------------------------------------------
        if merce <= self.__capacitaMax:
            self.__merce = merce
        else:
            raise ValueError('Non basta lo spazio')
    
    @property
    def passeggeriMax(self):
        return self.__passeggeriMax
    @passeggeriMax.setter
    def passeggeriMax(self, altroPasseggeriMax):
        self.__passeggeriMax = altroPasseggeriMax
        return
    
    @property
    def passeggeri(self):
        return self.__passeggeri
    @passeggeri.setter
    def passeggeri(self, altroPasseggeri):
        if altroPasseggeri <= self.__passeggeriMax:
            self.__passeggeri = altroPasseggeri
        return
    
    @property
    def capacitaMax(self):
        return self.__capacitaMax
    @capacitaMax.setter
    def capacitaMax(self, altraCapacitaMax):
        self.__capacitaMax = altraCapacitaMax
        return
    
    @property
    def merce(self):
        return self.__merce
    @merce.setter
    def merce(self, altraMerce):
        if altraMerce <= self.__capacitaMax:
            self.__merce = altraMerce
        return
#----------------------------------------------------------------------
if __name__ == '__main__':
    veicolo1 = Auto(targa='AA123AA' , cilindrata=1100 , capacitaMax=1000 , merce=900)
    veicolo2 = Auto(targa='BB456BB' , cilindrata = 900)
    
    print(veicolo1)
    print(veicolo2)
    print(veicolo1 >= veicolo2)
    
        
        












