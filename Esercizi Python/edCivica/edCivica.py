import matplotlib.pyplot as plt
import csv

mesiN = []
mediaTemp = []
gGiacca= []
gScuola = []
gVideogioco = []

#https://docs.google.com/document/d/1k3IhPLsAsRNUK_L5hRF8zYkpKIcn89eihHSU5S8OjeE/edit

dataFile = open("C:\\Users\\david\\OneDrive\\Materie ITIS - Sync\\anno 20-21\\sistemi e reti\\teoria\\esercizi\\dati.csv")
dataReader = csv.reader(dataFile, delimiter=',')
next(dataReader)

for row in dataReader:
    mesiN.append(int(row[1]))
    mediaTemp.append(float(row[2]))
    gGiacca.append(int(row[3]))
    gScuola.append(int(row[4]))
    gVideogioco.append(int(row[5]))

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1)
fig.suptitle('Media delle temperature, giorni con la giacca, giorni di scuola e giorni di videogame nel periodo Gennaio-Dicembre')

ax1.plot(mesiN,mediaTemp, 'o-m') 
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura media')

ax2.plot(mesiN,gGiacca, 'o-r') 
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni con la giacca')

ax3.plot(mesiN,gScuola, 'o-g') 
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di scuola')

ax4.plot(mesiN,gVideogioco, 'o-b')  
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni di Videogame')

plt.show()