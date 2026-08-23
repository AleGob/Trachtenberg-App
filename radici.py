import random

class GeneratoreRadici:
    
    @staticmethod
    def genera_radice(min_d, max_d):
        # Scegliamo un numero di cifre casuale per il radicando
        cifre = random.randint(min_d, max_d)
        
        min_val = 10 ** (cifre - 1) if cifre > 1 else 1
        max_val = (10 ** cifre) - 1
        
        # Generiamo il numero di cui trovare la radice
        numero = random.randint(min_val, max_val)
        
        # Calcoliamo la radice intera e il resto
        radice = int(numero ** 0.5)
        resto = numero - (radice ** 2)
        
        if resto == 0:
            risposta = str(radice)
        else:
            risposta = f"{radice} R {resto}"
            
        # Formattazione con il simbolo di radice quadrata
        testo_problema = f"√{numero}"
        
        return testo_problema, risposta