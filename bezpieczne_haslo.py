import random
import string

def generuj_bezpieczne_haslo():
    min_dlugosc = 8
    znaki = string.ascii_letters + string.digits + string.punctuation

    haslo = ''.join(random.choice(znaki) for _ in range(min_dlugosc))

    while not (any(c.isupper() for c in haslo) and
               any(c.islower() for c in haslo) and
               any(c.isdigit() for c in haslo) and
               any(c in string.punctuation for c in haslo) and
               len(haslo) >= min_dlugosc and
               not any(slowo in haslo.lower() for slowo in ["haslo", "admin", "123"])):
        haslo += random.choice(znaki)

    return haslo

# Przykład użycia
bezpieczne_haslo = generuj_bezpieczne_haslo()
print("Bezpieczne hasło:", bezpieczne_haslo)
