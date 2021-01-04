"""
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 15 posizioni più avanti nell'alfabeto.
Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.
"""

import string

def funzRot15(f):
    fApp = ""
    for cnt in range (len(f)):
        if(ord(f[cnt]) + 15 > ord('z')):
            fApp += chr(96 + (ord(f[cnt]) + 15 - ord('z')))
        else:
            fApp += chr(ord(f[cnt]) + 15)

    return fApp


def funzNorm(f):
    fApp = ""
    for cnt in range (len(f)):
        if(ord(f[cnt]) - 15 < ord('a')):
            fApp += chr(123 - (ord('a') - (ord(f[cnt]) - 15)))
        else:
            fApp += chr(ord(f[cnt]) - 15)

    return fApp


x = int(input("0 - Frase da criptare\n1 - Frase da decrifrare\nInserisci la tipologia della frase: "))

frase = input("\nInserisci frase: ")

if(x == 0):
    print(funzRot15(frase))
else:
    print(funzNorm(frase))