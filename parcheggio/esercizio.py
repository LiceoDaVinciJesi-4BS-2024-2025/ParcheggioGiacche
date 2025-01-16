from posto_mezzo import *

class Parcheggio:
    def __init__(self):
        #-----------------------------------------------------------------
        lista = []
        file = open('parkdata.txt' , 'r')
        contenuto = file.read().split(sep='\n')
        file.close()
        #-----------------------------------------------------------------
        for riga in contenuto:
            lista.append(riga)
        #-----------------------------------------------------------------
        self.__postiAutoLiberi = int(lista[0])
        lista.remove(lista[0])
        self.__postiMotoLiberi = int(lista[0])
        lista.remove(lista[0])
        self.__listaVeicoliParcheggiati = lista[0].split(sep=';')
        #-----------------------------------------------------------------
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
    
    def parcheggia(self , posto:PostoMezzo):
        if type(posto.occupante) == Auto and self.__postiAutoLiberi != 0:
            self.__postiAutoLiberi -= 1
            orePermanenza = datetime.datetime.today() - posto.dataOraFine
            saldoDaPagare = orePermanenza.hour * 1.5
        
        elif type(posto.occupante) == Moto and self.__postiMotoLiberi != 0:
            self.__postiMotoLiberi -= 1
            orePermanenza = datetime.datetime.today() - veicolo.dataOraFine
            saldoDaPagare = orePermanenza.hour() * 1.2
        
        else:
            raise ValueError('Non abbiamo posti liberi per quel veicolo')
        
        self.__guadagno += saldoDaPagare
        #-----------------------------------------------------------------
        file = open('parkdata.txt' , 'w')
        for x in self.__listaVeicoliParcheggiati:
            file.write(f'{x};')
        file.write(f'\n{self.__postiAutoLiberi}\n{self.__postiMotoLiberi}')
        file.close()
        #-----------------------------------------------------------------
        return f'Si devono pagare {saldoDaPagare} euro'

    
if __name__ == '__main__':
    autoMistica = Auto(targa='AA123AA')
    postoMistico = PostoMezzo(occupato=True , occupante=autoMistica , dataOraFine=datetime.datetime(2025,1,17,9,46,0))
    parcheggioMistico = Parcheggio()
    parcheggioMistico.parcheggia(postoMistico)














