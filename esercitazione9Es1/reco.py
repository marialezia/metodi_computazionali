import numpy as np

class Hit:
    """ 
    oggetto di tipo Hit ha informazioni su 
    - Id Modulo
    - Id sensore
    - Time Stamp rivelazione
    """
    def __init__(self, modulo, sensore, time):
        self.modulo = modulo
        self.sensore = sensore
        self.time = time

    def __gt__(self, altro):
        return self.time > altro.time

    


class Event:
    """ oggetto di tipo Event ha informazioni su: 
    - numero di Hit
    - time stamp primo hit
    - time stamp ultimo hit
    - durata temporale
    - array di tutti gli hit
    """
    def __init__(self):
        self.numero = 0
        self.time_p = -1
        self.time_u = -1 
        self.durata = -1
        self.hit = np.empty(0)
        
    def aggiungi_hit(self, hit):
        '''
        aggiungo un elemento hit e aggiorna gli attributi: 
        - aggiunge elemento con np.append(),gli hit devono essere già ordinati temporaneamente
        - numero = lunghezza array
        - time stamp del primo: controllo se l'array è vuoto significa che è il primo elemento --> diventa time_p --> se non è vuoto non cambio nulla
        -  aggiorno durata = differenza tra ultimo tempo e primo tempo
        - time stamp dell'ultimo è hit.time di quello che aggiungo
        '''
        self.hit = np.append(self.hit, hit)
        self.numero = len(self.hit)
        if len(self.hit) == 1:
            self.time_p = hit.time
        self.time_u = hit.time
        self.durata = self.time_u - self.time_p

    def __str__(self):
        return 'Evento con ' + str(self.numero) + ' hits \n time stamp primo hit = ' + str(self.time_p) + ' \n time stamp ultimo hit =  ' + str(self.time_u) + ' \n durata = ' + str(self.durata)

    
