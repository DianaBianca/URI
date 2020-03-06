testes = int(input("digite o numero de testes que ira fazer : "))
led = input("digite o numero de leds :")
listNum = list(led)
dicionario = {'1': 2, '2': 5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '0':6}

totLed = 0

    

for i in listNum:
    totLed = totLed + dicionario.get(i) 

print(totLed)
               