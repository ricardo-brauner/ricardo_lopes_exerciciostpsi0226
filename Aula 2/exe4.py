entrada = 3.14

if type(entrada) == int:
    print("Número inteiro")

elif type(entrada) == float:
    print("Número decimal")

elif type(entrada) == list:
    print("Lista")

elif type(entrada) == str:
    print("String")

else:
    print("Desconhecido")