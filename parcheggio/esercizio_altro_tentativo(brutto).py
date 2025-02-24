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
        while '' in self.__listaVeicoliParcheggiati:
            self.__listaVeicoliParcheggiati.remove('')
        for x in self.__listaVeicoliParcheggiati:
            listaParametriMezzo = x.split(sep='_')
            if listaParametriMezzo[1] > str(datetime.datetime.now()):
                if 'Auto' in listaParametriMezzo[0]:
                    self.__postiAutoLiberi += 1
                elif 'Moto' in listaParametriMezzo[0]:
                    self.__postiMotoLiberi += 1
                self.__listaVeicoliParcheggiati.remove(x)
        lista.remove(lista[0])
        self.__guadagno = lista[0]
        if self.__guadagno == '':
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
    
    def parcheggia(self , veicolo:Veicolo , dataOraArrivo:datetime.datetime):
        if type(veicolo) == Auto and self.__postiAutoLiberi != 0:
            self.__postiAutoLiberi -= 1
            arrivo = dataOraArrivo.second()
            orePermanenza = (datetime.datetime.today().second() - arrivo) / 3600
            saldoDaPagare = orePermanenza * 1.5
            self.__listaVeicoliParcheggiati.append(f'{veicolo}_{dataOraArrivo}')
        
        elif type(veicolo) == Moto and self.__postiMotoLiberi != 0:
            self.__postiMotoLiberi -= 1
#             orePermanenza = posto.dataOraFine - datetime.datetime.today()
#             saldoDaPagare = (int(orePermanenza.total_seconds())/60) * 1.2
            self.__listaVeicoliParcheggiati.append(f'{veicolo}_{dataOraArrivo}')

        else:
            raise ValueError('Non abbiamo posti liberi per quel veicolo')
    
#     def parcheggia(self , veicolo:Veicolo , dataOraFine:datetime.datetime):
#         if type(veicolo) == Auto and self.__postiAutoLiberi != 0:
#             self.__postiAutoLiberi -= 1
#             orePermanenza = (dataOraFine - datetime.datetime.now()).seconds / 3600
#             saldoDaPagare = orePermanenza * 1.5
#             self.__listaVeicoliParcheggiati.append(f'{veicolo}_{dataOraFine}')
#         
#         elif type(veicolo) == Moto and self.__postiMotoLiberi != 0:
#             self.__postiMotoLiberi -= 1
# #             orePermanenza = posto.dataOraFine - datetime.datetime.today()
# #             saldoDaPagare = (int(orePermanenza.total_seconds())/60) * 1.2
#             self.__listaVeicoliParcheggiati.append(f'{veicolo}_{dataOraFine}')
# 
#         else:
#             raise ValueError('Non abbiamo posti liberi per quel veicolo')
#     self.
    
    def vaiVia(self , veicolo:Veicolo):
        if str(veicolo) in self.__listaVeicoliParcheggiati:
            for x in lista:
                if str(x) in self.__listaVeicoliParcheggiati:
                    veicoloCheSeNeVa = x
            
        
        self.__guadagno = float(self.__guadagno) + saldoDaPagare
        #-----------------------------------------------------------------
        file = open('parkdata.txt' , 'w')
        file.write(f'{self.__postiAutoLiberi}\n{self.__postiMotoLiberi}\n')
        for x in self.__listaVeicoliParcheggiati:
            file.write(f'{x};')
        file.write(f'\n{self.__guadagno}')
        file.close()
        #-----------------------------------------------------------------
        return f'Si devono pagare {saldoDaPagare} euro'

    
if __name__ == '__main__':
    autoMistica = Auto(targa='AA123AA')
    postoMistico = PostoMezzo(occupato=True , occupante=autoMistica , dataOraFine=datetime.datetime(2025,1,30,9,46,0))
    parcheggioMistico = Parcheggio()
    dataOraArrivo = datetime.datetime(2025,1,30,9,46,0)
    print(parcheggioMistico.parcheggia(autoMistica , dataOraArrivo))
    motoMistica = Moto(targa='BB12345')
    postoMistico2 = PostoMezzo(occupato=True , occupante=motoMistica , dataOraFine=datetime.datetime(2025,1,30,9,46,0))
#     print(parcheggioMistico.parcheggia(postoMistico2))















