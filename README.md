# Estimador de distância através do RSSI de dispositivos Bluetooth Low Energy

Esse script desenvolvido em Python foi desenvolvido como parte do trabalho de conclusão de curso para Engenharia de Telecomunicações. Basicamente sua função é recuperar e realizar cálculos estatísticos com os valores RSSI armazenados no banco de dados do Firebase Realtime Database, que foram enviados pelo scanner BLE desenvolvido por mim no seguinte link: https://github.com/brunoalvaress/ble-scanner.

# Tecnologias utilizadas

- Python 3
- Firebase Realtime Database

# Requisitos 

- PyCharm ou outra IDE

# Bibliotecas

- Pandas
- Matplotlib
- Numpy
- Firebase_admin

# Guia

1. Clonar o projeto em sua pasta com `https://github.com/brunoalvaress/rssi-calculator.git`
2. Configurar o código para acessar o seu banco de dados próprio no Firebase
3. Compilar o projeto 

# Resultados

O script gerará os seguintes resultados para cada distância medida assim que compilado:

- Quatro gráficos contendo a variação dos valores RSSI filtrados e não filtrados em função do número de medições
- Boxplots dos valores filtrados e não filtrados
- Melhor e pior valores filtrados e não filtrados
- Distância estimada filtrada e não filtrada
- Número de dados no banco
- Intervalo de confiança de 95%

# Variáveis

- Pode-se variar o valor do coeficiente de perda **n** dependendo do ambiente escolhido
- O valor da janela temporal do filtro média móvel pode ser variável
