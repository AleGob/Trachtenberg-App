import random

class GeneratoreDivisioni:
    
    @staticmethod
    def genera_divisione(min_d, max_d):
        cifre_dividendo = random.randint(min_d, max_d)
        max_cifre_divisore = max(1, cifre_dividendo - 1)
        cifre_divisore = random.randint(1, max_cifre_divisore)
        
        min_div = 10 ** (cifre_divisore - 1) if cifre_divisore > 1 else 2
        max_div = (10 ** cifre_divisore) - 1
        divisore = random.randint(min_div, max_div)
        
        min_divd = 10 ** (cifre_dividendo - 1)
        max_divd = (10 ** cifre_dividendo) - 1
        dividendo = random.randint(min_divd, max_divd)
        
        quoziente = dividendo // divisore
        resto = dividendo % divisore
        
        if resto == 0:
            risposta = str(quoziente)
        else:
            # Formato con gli spazi richiesto: "quoziente R resto"
            risposta = f"{quoziente} R {resto}"
            
        testo_problema = f"{dividendo}\n ÷ {divisore}"
        
        return testo_problema, risposta