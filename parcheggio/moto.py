from veicolo import *

listaMarcheMoto = ['Aprilia' , 'Ducati' , 'Malaguti' , 'Ktm' , 'Tm' , 'Aerox' , 'Bmw']

class Moto(Veicolo):
    def __init__(self, marca='Aprilia', modello='sx', colore='Giallo', cilindrata:int=1000, alimentazione='parolacce', targa='', passeggeriMax:int=2 , passeggeri:int=1 , capacitaMax:int=100 , merce:int=0):
        #------------------------------------------------------------------
        if marca.capitalize() in listaMarcheMoto:
            self.marca = marca
        else:
            raise ValueError('Non è una marca')
        #------------------------------------------------------------------
        self.modello = modello
        #------------------------------------------------------------------
        if colore.capitalize() in listaColori:
            self.colore = colore
        else:
            raise ValueError('Il colore non è accettabile')
        #------------------------------------------------------------------
        if cilindrata%100 == 0:
            self.cilindrata = cilindrata
        else:
            raise ValueError('La cilindrata non è accettabile')
        #------------------------------------------------------------------
        self.alimentazione = alimentazione        #-----------------------------------------------------------------
        if targa[0] in lettere and targa[1] in lettere and targa[2] in numeri and targa[3] in numeri and targa[4]  in numeri and targa[5] in numeri and targa[6] in numeri:
            self.targa = targa
        else:
            raise ValueError('Targa non valida')
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
    
#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    veicolo1 = Moto(targa='AA12345')
    veicolo2 = Moto(targa='BB12345' , cilindrata=900)
    print(veicolo1 >= veicolo2)