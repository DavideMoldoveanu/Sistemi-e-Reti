import socket as sck

#protocollo UDP non è affidabile, perché non garantisce la consegna del dato
#protocollo TCP è affidabile, perché garantisce la consegna (sempre)
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
    frase = input("Inserisci: ")
    f = frase.encode()
    s.sendto(f, ('localhost', 5000))

    data, addr = s.recvfrom(4096)

s.close() 
    

"""
TELEFONO SENZA FILI:
creare un programma che sia server/client (insieme) (actor)
"""
