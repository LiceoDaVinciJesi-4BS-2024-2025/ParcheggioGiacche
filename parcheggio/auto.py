from veicolo import *

class Auto(Veicolo):
    def __init__(self, marca='Fiat', modello='Panda', colore='Giallo', cilindrata:int=1000, alimentazione='parolacce', targa='', passeggeriMax:int=4 , passeggeri:int=1 , capacitaMax:int=100 , merce:int=0):
        super().__init__(marca, modello, colore, cilindrata, alimentazione, targa)
        #-----------------------------------------------------------------
        self.passeggeriMax = passeggeriMax
        #-----------------------------------------------------------------
        if passeggeri <= self.passeggeriMax:
            self.passeggeri = passeggeri
        else:
            raise ValueError('Non bastano i posti')
        #-----------------------------------------------------------------
        self.capacitaMax = capacitaMax
        #-----------------------------------------------------------------
        if merce <= self.capacitaMax:
            self.merce = merce
        else:
            raise ValueError('Non basta lo spazio')
    
#----------------------------------------------------------------------
if __name__ == '__main__':
    veicolo1 = Auto(targa='AA123AA' , cilindrata=1100 , capacitaMax=1000 , merce=900)
    veicolo2 = Auto(targa='BB456BB' , cilindrata = 900)
    
    print(veicolo1)
    print(veicolo2)
    print(veicolo1 >= veicolo2)
    
        
        












