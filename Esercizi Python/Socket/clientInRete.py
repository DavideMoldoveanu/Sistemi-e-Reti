import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
    frase = input("Inserisci: ")
    f = frase.encode()
    s.sendto(f, ('192.168.0.124', 5000))

    data, addr = s.recvfrom(4096)
    
    print(data)

s.close() 