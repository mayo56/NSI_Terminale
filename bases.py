def n_to_bases(n, base) -> None:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n_converti = []

    while n > 0:
        n_converti.append(n % base)
        n //= base
    
    n_converti.reverse()

    n_str = ""
    for n_base in n_converti:
        n_str += alphabet[n_base]
    
    return n_str


print(n_to_bases(72710033293788371630651945970,35))

def base_to_n(n:str,base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    n_base_dix = 0

    for i, nombre in enumerate(n):
        puissance = len(n) - i - 1
        n_base_dix += alphabet.index(nombre) * (base ** puissance)
    
    print(n_base_dix)

base_to_n("MAYO", 35)