import random

class GeneratoreAddizioni:
    
    @staticmethod
    def genera_colonna(min_d, max_d, righe):
        numeri = []
        
        # Genera 'n' righe, ognuna con un numero di cifre ricalcolato a caso
        for _ in range(righe):
            cifre = random.randint(min_d, max_d)
            min_val = 10 ** (cifre - 1) if cifre > 1 else 1
            max_val = (10 ** cifre) - 1
            numeri.append(random.randint(min_val, max_val))
            
        risposta = str(sum(numeri))
        
        # Incolonna i numeri
        testo_problema = "\n".join(f"+ {num}" if i > 0 else f"  {num}" for i, num in enumerate(numeri))
        
        return testo_problema, risposta