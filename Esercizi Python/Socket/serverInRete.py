import socket as sck                            #client/server

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)     #client/server

s.bind(('0.0.0.0', 5000))                     #solo server

while True:
    frase = input("Inserisci: ")
    f = frase.encode()
    
    data, addr = s.recvfrom(4096)               #data --> stringa binaria || addr --> tupla (ip client, porta client)
    s.sendto(f, addr)                           #invia la frase e i addr al client
    print(data)