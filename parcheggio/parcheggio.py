from posto_mezzo import *
from pathlib import Path

class Parcheggio:
    def __init__(self):
        #-----------------------------------------------------------------
        if Path('park.data').exists():
                
             
            lista = []
            file = open('park.data' , 'r')
            contenuto = file.read().split(sep='\n')
            file.close()
            for riga in contenuto:
                lista.append(riga)
            #-----------------------------------------------------------------
            
            #-----------------------------------------------------------------
            self.__postiAutoLiberi = int(lista[0])
            lista.remove(lista[0])
            self.__postiMotoLiberi = int(lista[0])
            lista.remove(lista[0])
            self.__listaVeicoliParcheggiati = lista[0].split(sep=';')
            while '' in self.__listaVeicoliParcheggiati:
                self.__listaVeicoliParcheggiati.remove('')
            for x in self.__listaVeicoliParcheggiati:
                listaParametriMezzo = x.split(sep='_')
                if listaParametriMezzo[-1] <= str(datetime.datetime.now()):
                    if 'Auto' in listaParametriMezzo[0]:
                        self.__postiAutoLiberi += 1
                    elif 'Moto' in listaParametriMezzo[0]:
                        self.__postiMotoLiberi += 1
                    self.__listaVeicoliParcheggiati.remove(x)
            lista.remove(lista[0])
            self.__guadagno = lista[0]
            if self.__guadagno == '':
                self.__guadagno = 0
        
        else:
            self.__postiAutoLiberi = 1000
            self.__postiMotoLiberi = 500
            self.__listaVeicoliParcheggiati = []
            self.__guadagno = 0
        
            
        #-----------------------------------------------------------------
    
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
    
    def parcheggia(self, veicolo , dataOraFine1):
        posto = PostoMezzo(occupato=True , occupante=veicolo , dataOraFine=dataOraFine1)
        if type(posto.occupante) == Auto and self.__postiAutoLiberi != 0:
            self.__postiAutoLiberi -= 1
            orePermanenza = posto.dataOraFine - datetime.datetime.today()
            saldoDaPagare = (int(orePermanenza.total_seconds())/3600) * 1.5
            self.__listaVeicoliParcheggiati.append(f'{posto.occupante}_{posto.dataOraFine}')
        
        elif type(posto.occupante) == Moto and self.__postiMotoLiberi != 0:
            self.__postiMotoLiberi -= 1
            orePermanenza = posto.dataOraFine - datetime.datetime.today()
            saldoDaPagare = (int(orePermanenza.total_seconds())/3600) * 1.2
            self.__listaVeicoliParcheggiati.append(f'{posto.occupante}_{posto.dataOraFine}')

        else:
            raise ValueError('Non abbiamo posti liberi per quel veicolo')
        
        self.__guadagno = float(self.__guadagno) + saldoDaPagare
        return f'Si devono pagare {saldoDaPagare} euro'

        #-----------------------------------------------------------------
    def salva(self):
        file = open('park.data' , 'w')
        file.write(f'{self.__postiAutoLiberi}\n{self.__postiMotoLiberi}\n')
        for x in self.__listaVeicoliParcheggiati:
            file.write(f'{x};')
        file.write(f'\n{self.__guadagno}')
        file.close()
        #-----------------------------------------------------------------
        #-----------------------------------------------------------------
    
if __name__ == '__main__':
    autoMistica = Auto(targa='AA123AA')
    parcheggioMistico = Parcheggio()
    print(parcheggioMistico.parcheggia(autoMistica ,datetime.datetime(2025,3,30,9,46,0)))
    motoMistica = Moto(targa='BB12345')
    print(parcheggioMistico.parcheggia(motoMistica ,datetime.datetime(2025,3,30,9,46,0)))
    print(parcheggioMistico.guadagno)
    parcheggioMistico.salva()














