import socket as sck                            #client/server

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)     #client/server

s.bind(('localhost', 5000))                     #solo server

while True:
    data, addr = s.recvfrom(4096)               #data --> stringa binaria || addr --> tupla (ip client, porta client)
    s.sendto(data, addr)                        #invia i data e i addr al client
    print(data)