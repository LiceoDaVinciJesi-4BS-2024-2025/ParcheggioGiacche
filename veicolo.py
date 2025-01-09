#Mattia Giacchè
#4BS
#Veicolo

listaMarche = ['Fiat' , 'Citroen' , 'Audi' , 'Volkswagen' , 'Mercedes']
listaColori = ['Rosso' , 'Bianco' , 'Blu' , 'Verde' , 'Giallo' , 'Nero' , 'Grigio']
lettere = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ'
numeri = '0123456789'

class Veicolo:
    def __init__(self, marca='Fiat', modello='Panda', colore='Giallo', cilindrata:int=1000, alimentazione='parolacce', targa=''):
        if marca.capitalize() in listaMarche:
            self.marca = marca
        else:
            raise ValueError('Non è una marca')
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
        self.alimentazione = alimentazione
        #------------------------------------------------------------------
        if targa[0] in lettere and targa[1] in lettere and targa[2] in numeri and targa[3] in numeri and targa[4] in numeri and targa[5] in lettere and targa[6] in lettere and len(targa) == 7:
            self.targa = targa
        else:
            raise ValueError('La targa non è accettabile')
    
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __le__(self , altroVeicolo):
        if self.marca > altroVeicolo.marca:
            return False
        elif self.marca > altroVeicolo.marca:
            return False
        elif self.cilindrata > altroVeicolo.cilindrata:
            return False
        else:
            return True
    
#     def __ge__(self , altroVeicolo:Veicolo):
#         if self.marca < altroVeicolo.marca:
#             return False
#         elif self.marca < altroVeicolo.marca:
#             return False
#         elif self.cilindrata < altroVeicolo.cilindrata:
#             return False
#         else:
#             return True

#-------------------------------------------------
if __name__ == '__main__':
    veicolo1 = Veicolo(targa='AA123AA')
    
























