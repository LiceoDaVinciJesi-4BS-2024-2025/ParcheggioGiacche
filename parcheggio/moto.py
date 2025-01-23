from veicolo import *

listaMarcheMoto = ['Aprilia' , 'Ducati' , 'Malaguti' , 'Ktm' , 'Tm' , 'Aerox' , 'Bmw']

class Moto(Veicolo):
    def __init__(self, targa,  marca='Aprilia', modello='sx', colore='Giallo', cilindrata:int=1000, alimentazione='parolacce', passeggeriMax:int=2 , passeggeri:int=1 , capacitaMax:int=100 , merce:int=0):
        if len(targa) == 7 and targa[0] in lettere and targa[1] in lettere and targa[2] in numeri and targa[3] in numeri and targa[4]  in numeri and targa[5] in numeri and targa[6] in numeri:
            self.__targa = targa
        else:
            raise ValueError('Targa non valida')
        #------------------------------------------------------------------
        if marca.capitalize() in listaMarcheMoto:
            self.__marca = marca
        else:
            raise ValueError('Non è una marca')
        #------------------------------------------------------------------
        self.__modello = modello
        #------------------------------------------------------------------
        if colore.capitalize() in listaColori:
            self.__colore = colore
        else:
            raise ValueError('Il colore non è accettabile')
        #------------------------------------------------------------------
        if cilindrata%100 == 0:
            self.__cilindrata = cilindrata
        else:
            raise ValueError('La cilindrata non è accettabile')
        #------------------------------------------------------------------
        self.__alimentazione = alimentazione        #-----------------------------------------------------------------
        
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
    def targa(self):
        return self.__targa
    
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self , marcaNuova):
        if marcaNuova in listaMarche:
            self.__marca = marcaNuova
        else:
            raise ValueError('Marca non accettabile')
    
    @property
    def modello(self):
        return self.__modello
    @modello.setter
    def modello(self , altroModello):
        self.__modello = altroModello
        return
    
    @property
    def colore(self):
        return self.__colore
    @colore.setter
    def colore(self , altroColore):
        self.__colore = altroColore
        return
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    @modello.setter
    def cilindrata(self , altraCilindrata):
        self.__cilindrata = altraCilindrata
        return
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    @modello.setter
    def alimentazione(self , altraAlimentazione):
        self.__modello = altraAlimentazione
        return
    
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

#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    veicolo1 = Moto(targa='AA12345')
    veicolo2 = Moto(targa='BB12345' , cilindrata=900)
    print(veicolo1 >= veicolo2)