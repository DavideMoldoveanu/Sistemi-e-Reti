import matplotlib.pyplot as plt
import csv

anni = []
anomaliaTemp = []

totalEmissions = []
gasEmissions = []
liquidEmissions = []
solidEmissions = []
cement = []
gasFlaring = []
perCapita = []


dataEmissioni = open("C:\\Users\\david\\OneDrive\\Materie ITIS - Sync\\anno 20-21\\sistemi e reti\\teoria\\esercizi\\edCivica\\CO2_emissions.csv")
dataReader2 = csv.reader(dataEmissioni, delimiter=',')
next(dataReader2)

for row in dataReader2:
    temp = (int(row[0]))
    if temp <= 2010 and temp >= 1880:
        totalEmissions.append(float(row[1]))
        gasEmissions.append(float(row[2]))
        liquidEmissions.append(float(row[3]))
        solidEmissions.append(float(row[4]))
        cement.append(float(row[5]))
        gasFlaring.append(float(row[6]))
        if(temp >= 1950):
            perCapita.append(float(row[7]))


dataAnomalie = open("C:\\Users\\david\\OneDrive\\Materie ITIS - Sync\\anno 20-21\\sistemi e reti\\teoria\\esercizi\\edCivica\\Temperature_Anomaly.csv")
dataReader1 = csv.reader(dataAnomalie, delimiter=',')
for _ in range(5):
    next(dataReader1)


for row in dataReader1:
    temp = (int(row[0]))
    if temp <= 2010 and temp >= 1880:
        anni.append(temp)
        anomaliaTemp.append(float(row[1]))


fig, (ax12) = plt.subplots(1,1)
fig.suptitle('Scostamento temperature ed emissioni')

'''ax1.plot(anni,anomaliaTemp, '-m') 
ax1.set_xlabel('Anni')
ax1.set_ylabel('Anomalie temperature')'''

'''ax2.plot(anni,totalEmissions, '-m')
ax2.set_xlabel('Anni')
ax2.set_ylabel('Totali Emissioni')'''

'''
ax3.plot(anni,gasEmissions, '-m')
ax3.set_xlabel('Anni')
ax3.set_ylabel('Emissioni Gas')

ax4.plot(anni,liquidEmissions, '-m')
ax4.set_xlabel('Anni')
ax4.set_ylabel('Emissioni Liquidi')
'''

'''ax5.plot(anni,solidEmissions, '-m')
ax5.set_xlabel('Anni')
ax5.set_ylabel('Emissioni Solidi')'''

'''
ax6.plot(anni,cement, '-m')
ax6.set_xlabel('Anni')
ax6.set_ylabel('Emissioni da cemento')

ax7.plot(anni,gasFlaring, '-m')
ax7.set_xlabel('Anni')
ax7.set_ylabel('Emissioni da Gas Flaring')

ax8.plot(anni,perCapita, '-m')
ax8.set_xlabel('Anni')
ax8.set_ylabel('Emissioni Per Capita')


ax9.plot(anomaliaTemp, totalEmissions, '. m')
ax9.set_xlabel('Anomalia Temperatura')
ax9.set_ylabel('Emissioni Totali')
'''

'''ax10.plot(anomaliaTemp, gasEmissions, '. m')
ax10.set_xlabel('Anomalia Temperatura')
ax10.set_ylabel('Emissioni Gas')'''

'''
ax11.plot(anomaliaTemp, liquidEmissions, '. m')
ax11.set_xlabel('Anomalia Temperatura')
ax11.set_ylabel('Emissioni Liquidi')
'''

ax12.plot(anomaliaTemp, solidEmissions, '. m')
ax12.set_xlabel('Anomalia Temperatura')
ax12.set_ylabel('Emissioni Solidi')

'''
ax13.plot(anomaliaTemp, gasFlaring, '. m')
ax13.set_xlabel('Anomalia Temperatura')
ax13.set_ylabel('Emissioni Gas Flaring')

ax14.plot(anomaliaTemp, cement, '. m')
ax14.set_xlabel('Anomalia Temperatura')
ax14.set_ylabel('Emissioni Cemento')
'''

plt.show()