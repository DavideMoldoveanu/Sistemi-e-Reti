MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]



def creaDict():
    dizionario = {}
    listaR = [] #lista riga
    post = 0
    like = 0
    for mese in MESI:
        file = open("C:\\Users\\david\\OneDrive\\Materie ITIS - Sync\\anno 20-21\\sistemi e reti\\teoria\\esercizi\\instagram.csv","r")
        like = 0
        post = 0
        for k, riga in enumerate(file):
            if k>0:
                listaR = riga.split(",")
                if mese == listaR[0]:
                    post += 1
                    like += int(listaR[-1])
                    dizionario[mese] = [post,like]
        
        file.close()
    return dizionario


def cerca(mese,diz):
    for element in diz.keys():
        if element == mese:
            print(diz[element])
            break


def main():

    dizionario = creaDict()

    mese = input("Inserisci mese: ")
    cerca(mese, dizionario)

    print(dizionario)

if __name__ == "__main__":
    main()