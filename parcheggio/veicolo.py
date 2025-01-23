#Mattia Giacchè
#4BS
#Veicolo

listaMarche = ['Fiat' , 'Citroen' , 'Audi' , 'Volkswagen' , 'Mercedes']
listaColori = ['Rosso' , 'Bianco' , 'Blu' , 'Verde' , 'Giallo' , 'Nero' , 'Grigio']
lettere = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeri = '0123456789'

class Veicolo:
    def __init__(self, targa , marca='Fiat', modello='Panda', colore='Giallo', cilindrata:int=1000, alimentazione='parolacce'):
        
        if len(targa) == 7 and targa[0] in lettere and targa[1] in lettere and targa[2] in numeri and targa[3] in numeri and targa[4] in numeri and targa[5] in lettere and targa[6] in lettere and len(targa) == 7:
            self.__targa = targa
        else:
            raise ValueError('La targa non è accettabile')
        #------------------------------------------------------------------
        if marca.capitalize() in listaMarche:
            self.__marca = marca
        else:
            raise ValueError('Non è una marca')
        #------------------------------------------------------------------
        self.modello = modello
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
        self.__alimentazione = alimentazione
        #------------------------------------------------------------------
  
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
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

    def __le__(self , altroVeicolo):
        if self.marca > altroVeicolo.marca:
            return False
        elif self.modello > altroVeicolo.modello:
            return False
        elif self.cilindrata > altroVeicolo.cilindrata:
            return False
        else:
            return True
    
    def __lt__(self , altroVeicolo):
        if self.marca < altroVeicolo.marca:
            return True 
        elif self.marca == altroVeicolo.marca:
            if self.modello < altroVeicolo.modello:
                return True
            elif self.modello == altroVeicolo.modello:
                if self.cilindrata < altroVeicolo.cilindrata:
                    return True
        return False


#-------------------------------------------------
if __name__ == '__main__':
    veicolo1 = Veicolo(targa='AA123AA')
    veicolo2 = Veicolo(cilindrata=1100 , targa='BB456BB')
    print(veicolo1 <= veicolo2)
    veicolo3 = Veicolo(cilindrata=1200 , targa='BB345BB')
    listaVeicoli = [veicolo1 , veicolo2 , veicolo3]
    listaVeicoli.sort()
    print(listaVeicoli)























