import random

class GeneratoreQuadrati:
    
    @staticmethod
    def genera_quadrato(min_d, max_d):
        cifre = random.randint(min_d, max_d)
        min_val = 10 ** (cifre - 1) if cifre > 1 else 1
        max_val = (10 ** cifre) - 1
        
        base_number = random.randint(min_val, max_val)
        
        risposta = str(base_number ** 2)
        # Formattazione con il simbolo del quadrato
        testo_problema = f"{base_number}²"
        
        return testo_problema, risposta