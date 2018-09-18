import pandas as pd
import matplotlib.pyplot as plt
import firebase_admin
import numpy as np
import scipy.stats as st
from scipy.signal import medfilt
from firebase_admin import credentials
from firebase_admin import db

######################################## Conecta ao banco de dados ########################################

cred = credentials.Certificate("./bletestebruno-firebase-adminsdk-29wsy-0b9cf3b411.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bletestebruno.firebaseio.com'
})

######################################## Recupera valores do banco ########################################

#ref = db.reference('/RssiTxpower2metros/Resultados')
reftxpower = db.reference('/RssiTxpower/Resultados')
ref2metros = db.reference('/RssiTxpower2metros/Resultados')
ref3metros = db.reference('/RssiTxpower3metros/Resultados')
ref4metros = db.reference('/RssiTxpower4metros/Resultados')
ref5metros = db.reference('/RssiTxpower5metros/Resultados')




#obtém o dicionário no formato (chave:rssi)
resultadotxpower = reftxpower.get()
resultados2metros = ref2metros.get()
resultados3metros = ref3metros.get()
resultados4metros = ref4metros.get()
resultados5metros = ref5metros.get()

######################################## RSSI Tx Power ########################################
print("---------- Informações TX POWER ----------")
#separa a chave dos valores RSSI para TxPower
all_items=[]
for i,j in resultadotxpower.items():
    all_items.append(j)
valorestxpower = all_items
#print(valorestxpower)

tamanhobancotxpower = len(valorestxpower)
txpower = np.mean(valorestxpower)
print(f"\nA lista de TxPower possui {tamanhobancotxpower} valores" )
print(f"TxPower vale {txpower:0.3f} dBm")

n = 1.6

######################################## RSSI 2 METROS ########################################
print("\n---------- Informações 2 METROS ----------")
#separa a chave dos valores RSSI para 2 metros
all_items=[]
for i,j in resultados2metros.items():
    all_items.append(j)
valores2metros = all_items
#print(valores)


#retorna quantas medições estão salvas no banco de dados
tamanhobanco2metros = len(valores2metros)
print(f"\nA lista possui {tamanhobanco2metros} valores")


#retorna a média da soma dos valores RSSI
media2metros = np.mean(valores2metros)
print(f"A média da soma dos valores sem filtro é de {media2metros:0.2f} dBm")

#filtro
df = pd.DataFrame(valores2metros) #transforma os dados em DataFrame
filtromediamovel = df.rolling(window=11).mean() #calcula a média móvel com coeficiente 5
cdataframe2metros = list(filtromediamovel.values.flatten()) #converte DataFrame para Lista
valoresfiltrados2metros = [cdataframe2metros for cdataframe2metros in cdataframe2metros if str(cdataframe2metros) != 'nan'] #remove os valores NaN da lista
mediafiltrado2metros = np.mean(valoresfiltrados2metros)
print(f"A média da soma dos valores filtrados é de {mediafiltrado2metros:0.2f} dBm")

#retorna o melhor e pior valores
melhorvalor2metros = max(valores2metros)
piorvalor2metros = min(valores2metros)
print(f"O melhor valor sem filtro foi {melhorvalor2metros} dBm, e o pior valor sem filtro foi {piorvalor2metros} dBm")
melhorvalorfiltrado2metros = max(valoresfiltrados2metros)
piorvalorfiltrado2metros = min(valoresfiltrados2metros)
print(f"O melhor valor filtrado foi {melhorvalorfiltrado2metros} dBm, e o pior valor filtrado foi {piorvalorfiltrado2metros} dBm")

#retorna a distância estimada
#n é a cte de propagação, ar livre = 2
#txpower = -66

distanciaestimada2metros = 10 ** ((txpower - media2metros) / (10 * n))
print(f"A distância estimada sem filtros é de {distanciaestimada2metros:0.3f} metros")
distanciafiltradoestimada2metros = 10 ** ((txpower - mediafiltrado2metros) / (10 * n))
print(f"A distância estimada filtrada é de {distanciafiltradoestimada2metros:0.3f} metros")

#intervalo de confiança
mediafiltrada2metros = np.mean(valoresfiltrados2metros)
intconf = st.t.interval(0.95, len(valoresfiltrados2metros) - 1, loc=np.mean(valoresfiltrados2metros), scale=st.sem(valoresfiltrados2metros))
print(intconf)

######################################## RSSI 3 METROS ########################################
print("\n---------- Informações 3 METROS ----------")




#separa a chave dos valores RSSI para 3 metros
all_items=[]
for i,j in resultados3metros.items():
    all_items.append(j)
valores3metros = all_items
#print(valores)


#retorna quantas medições estão salvas no banco de dados
tamanhobanco3metros = len(valores3metros)
print(f"\nA lista possui {tamanhobanco3metros} valores")


#retorna a média da soma dos valores RSSI
media3metros = np.mean(valores3metros)
print(f"A média da soma dos valores sem filtro é de {media3metros:0.2f} dBm")

#filtro
df = pd.DataFrame(valores3metros) #transforma os dados em DataFrame
filtromediamovel3metros = df.rolling(window=2).mean() #calcula a média móvel com coeficiente 5
cdataframe3metros = list(filtromediamovel3metros.values.flatten()) #converte DataFrame para Lista
valoresfiltrados3metros = [cdataframe3metros for cdataframe3metros in cdataframe3metros if str(cdataframe3metros) != 'nan'] #remove os valores NaN da lista
mediafiltrado3metros = np.mean(valoresfiltrados3metros)
print(f"A média da soma dos valores filtrados é de {mediafiltrado3metros:0.2f} dBm")

#retorna o melhor e pior valores
melhorvalor3metros = max(valores3metros)
piorvalor3metros = min(valores3metros)
print(f"O melhor valor sem filtro foi {melhorvalor3metros} dBm, e o pior valor sem filtro foi {piorvalor3metros} dBm")
melhorvalorfiltrado3metros = max(valoresfiltrados3metros)
piorvalorfiltrado3metros = min(valoresfiltrados3metros)
print(f"O melhor valor filtrado foi {melhorvalorfiltrado3metros} dBm, e o pior valor filtrado foi {piorvalorfiltrado3metros} dBm")

#retorna a distância estimada
#n é a cte de propagação, ar livre = 2
#txpower = -66

distanciaestimada3metros = 10 ** ((txpower - media3metros) / (10 * n))
print(f"A distância estimada sem filtros é de {distanciaestimada3metros:0.3f} metros")
distanciafiltradoestimada3metros = 10 ** ((txpower - mediafiltrado3metros) / (10 * n))
print(f"A distância estimada filtrada é de {distanciafiltradoestimada3metros:0.3f} metros")

#intervalo de confiança
mediafiltrada3metros = np.mean(valoresfiltrados3metros)
intconf3metros = st.t.interval(0.95, len(valoresfiltrados3metros) - 1, loc=np.mean(valoresfiltrados3metros), scale=st.sem(valoresfiltrados3metros))
print(intconf3metros)

######################################## RSSI 4 METROS ########################################
print("\n---------- Informações 4 METROS ----------")

#separa a chave dos valores RSSI para 4 metros
all_items=[]
for i,j in resultados4metros.items():
    all_items.append(j)
valores4metros = all_items
#print(valores)


#retorna quantas medições estão salvas no banco de dados
tamanhobanco4metros = len(valores4metros)
print(f"\nA lista possui {tamanhobanco4metros} valores")


#retorna a média da soma dos valores RSSI
media4metros = np.mean(valores4metros)
print(f"A média da soma dos valores sem filtro é de {media4metros:0.2f} dBm")

#filtro
df = pd.DataFrame(valores4metros) #transforma os dados em DataFrame
filtromediamovel4metros = df.rolling(window=11).mean() #calcula a média móvel com coeficiente 5
cdataframe4metros = list(filtromediamovel4metros.values.flatten()) #converte DataFrame para Lista
valoresfiltrados4metros = [cdataframe4metros for cdataframe4metros in cdataframe4metros if str(cdataframe4metros) != 'nan'] #remove os valores NaN da lista
mediafiltrado4metros = np.mean(valoresfiltrados4metros)
print(f"A média da soma dos valores filtrados é de {mediafiltrado4metros:0.2f} dBm")

#retorna o melhor e pior valores
melhorvalor4metros = max(valores4metros)
piorvalor4metros = min(valores4metros)
print(f"O melhor valor sem filtro foi {melhorvalor4metros} dBm, e o pior valor sem filtro foi {piorvalor4metros} dBm")
melhorvalorfiltrado4metros = max(valoresfiltrados4metros)
piorvalorfiltrado4metros = min(valoresfiltrados4metros)
print(f"O melhor valor filtrado foi {melhorvalorfiltrado4metros} dBm, e o pior valor filtrado foi {piorvalorfiltrado4metros} dBm")

#retorna a distância estimada
#n é a cte de propagação, ar livre = 2
#txpower = -66

distanciaestimada4metros = 10 ** ((txpower - media4metros) / (10 * n))
print(f"A distância estimada sem filtros é de {distanciaestimada4metros:0.3f} metros")
distanciafiltradoestimada4metros = 10 ** ((txpower - mediafiltrado4metros) / (10 * n))
print(f"A distância estimada filtrada é de {distanciafiltradoestimada4metros:0.3f} metros")

#intervalo de confiança
mediafiltrada4metros = np.mean(valoresfiltrados4metros)
intconf4metros = st.t.interval(0.95, len(valoresfiltrados4metros) - 1, loc=np.mean(valoresfiltrados4metros), scale=st.sem(valoresfiltrados4metros))
print(intconf4metros)


######################################## RSSI 5 METROS ########################################
print("\n---------- Informações 5 METROS ----------")

#separa a chave dos valores RSSI para 5 metros
all_items=[]
for i,j in resultados5metros.items():
    all_items.append(j)
valores5metros = all_items
#print(valores)


valores5metros = []

for elem in valores5metros:
    if elem > -72:
        valores5metros.append(elem)



#retorna quantas medições estão salvas no banco de dados
tamanhobanco5metros = len(valores5metros)
print(f"\nA lista possui {tamanhobanco5metros} valores")


#retorna a média da soma dos valores RSSI
media5metros = np.mean(valores5metros)
print(f"A média da soma dos valores sem filtro é de {media5metros:0.2f} dBm")

#filtro
df = pd.DataFrame(valores5metros) #transforma os dados em DataFrame
filtromediamovel5metros = df.rolling(window=12).mean() #calcula a média móvel com coeficiente 5
cdataframe5metros = list(filtromediamovel5metros.values.flatten()) #converte DataFrame para Lista
valoresfiltrados5metros = [cdataframe5metros for cdataframe5metros in cdataframe5metros if str(cdataframe5metros) != 'nan'] #remove os valores NaN da lista
mediafiltrado5metros = np.mean(valoresfiltrados5metros)
print(f"A média da soma dos valores filtrados é de {mediafiltrado5metros:0.2f} dBm")

#retorna o melhor e pior valores
melhorvalor5metros = max(valores5metros)
piorvalor5metros = min(valores5metros)
print(f"O melhor valor sem filtro foi {melhorvalor5metros} dBm, e o pior valor sem filtro foi {piorvalor5metros} dBm")
melhorvalorfiltrado5metros = max(valoresfiltrados5metros)
piorvalorfiltrado5metros = min(valoresfiltrados5metros)
print(f"O melhor valor filtrado foi {melhorvalorfiltrado5metros} dBm, e o pior valor filtrado foi {piorvalorfiltrado5metros} dBm")

#retorna a distância estimada
#n é a cte de propagação, ar livre = 2
#txpower = -66

distanciaestimada5metros = 10 ** ((txpower - media5metros) / (10 * n))
print(f"A distância estimada sem filtros é de {distanciaestimada5metros:0.3f} metros")
distanciafiltradoestimada5metros = 10 ** ((txpower - mediafiltrado5metros) / (10 * n))
print(f"A distância estimada filtrada é de {distanciafiltradoestimada5metros:0.3f} metros")

#intervalo de confiança
mediafiltrada5metros = np.mean(valoresfiltrados5metros)
intconf5metros = st.t.interval(0.95, len(valoresfiltrados5metros) - 1, loc=np.mean(valoresfiltrados5metros), scale=st.sem(valoresfiltrados5metros))
print(intconf5metros)


plt.subplot(2, 2, 1)
plt.subplot(2, 2, 1).set_title("2 metros")
plt.ylabel("RSSI [dBm]")
plt.plot(cdataframe2metros, 'r', label ="Valores Filtrados", linewidth=3.0)
plt.plot(valores2metros, 'g--', label ="Valores sem Filtro")
plt.legend(loc='best')

plt.subplot(2, 2, 2)
plt.subplot(2, 2, 2).set_title("3 metros")
plt.ylabel("RSSI [dBm]")
plt.plot(cdataframe3metros, 'r', label ="Valores Filtrados", linewidth=3.0)
plt.plot(valores3metros, 'g--', label ="Valores sem Filtro")
plt.legend(loc='best')

plt.subplot(2, 2, 3)
plt.subplot(2, 2, 3).set_title("4 metros")
plt.xlabel("Número de Medições")
plt.ylabel("RSSI [dBm]")
plt.plot(cdataframe4metros, 'r', label ="Valores Filtrados", linewidth=3.0)
plt.plot(valores4metros, 'g--', label ="Valores sem Filtro")
plt.legend(loc='best')

plt.subplot(2, 2, 4)
plt.subplot(2, 2, 4).set_title("5 metros")
plt.xlabel("Número de Medições")
plt.ylabel("RSSI [dBm]")
plt.plot(cdataframe5metros, 'r', label ="Valores Filtrados", linewidth=3.0)
plt.plot(valores5metros, 'g--', label ="Valores sem Filtro")
plt.legend(loc='best')

plt.suptitle('GRÁFICOS GERADOS')
plt.show()



#plota boxplots na mesma figura
plt.subplot(2, 1, 1)
data_to_plot = [valorestxpower, valores2metros, valores3metros, valores4metros, valores5metros]
plt.ylabel("RSSI [dBm]")
plt.xlabel("Metros")
plt.boxplot(data_to_plot)


plt.subplot(2, 1, 2)
data_to_plot = [valorestxpower, valoresfiltrados2metros, valoresfiltrados3metros, valoresfiltrados4metros, valoresfiltrados5metros]
plt.ylabel("RSSI [dBm]")
plt.xlabel("Metros")
plt.boxplot(data_to_plot)

plt.suptitle("BOXPLOTS - 1: Sem filtro  2: Com filtro")
plt.show()


#plot boxplot sem filtro
data_to_plot = [valorestxpower, valores2metros, valores3metros, valores4metros, valores5metros]
plt.title("BOXPLOT SEM FILTRAGEM")
plt.ylabel("RSSI [dBm]")
plt.xlabel("Metros")
plt.boxplot(data_to_plot)
plt.show()

#plot boxplot com filtro
data_to_plot = [valorestxpower, valoresfiltrados2metros, valoresfiltrados3metros, valoresfiltrados4metros, valoresfiltrados5metros]
plt.title("BOXPLOT FILTRADO")
plt.ylabel("RSSI [dBm]")
plt.xlabel("Metros")
plt.boxplot(data_to_plot)
plt.show()







