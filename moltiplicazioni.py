import random

class GeneratoreMoltiplicazioni:
    
    @staticmethod
    def genera_regola_rapida(regola, min_d, max_d):
        cifre = random.randint(min_d, max_d)
        min_val = 10 ** (cifre - 1) if cifre > 1 else 1
        max_val = (10 ** cifre) - 1
        
        base_number = random.randint(min_val, max_val)
        
        risposta = str(base_number * regola)
        testo_problema = f"{base_number}\n x {regola}"
        
        return testo_problema, risposta

    @staticmethod
    def genera_diretta(min_d, max_d):
        cifre1 = random.randint(min_d, max_d)
        cifre2 = random.randint(min_d, max_d)
        
        min_val1 = 10 ** (cifre1 - 1) if cifre1 > 1 else 1
        max_val1 = (10 ** cifre1) - 1
        num1 = random.randint(min_val1, max_val1)
        
        min_val2 = 10 ** (cifre2 - 1) if cifre2 > 1 else 1
        max_val2 = (10 ** cifre2) - 1
        num2 = random.randint(min_val2, max_val2)
        
        risposta = str(num1 * num2)
        testo_problema = f"{num1}\n x {num2}"
        
        return testo_problema, risposta