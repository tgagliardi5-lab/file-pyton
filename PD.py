# Programma che, dato un qualsiasi numero in input, calcola se è pari o dispari
numero = int(input ("Inserisci un numero: "))
resto = numero % 2
if resto == 0:
    print("Il numero", numero, "è pari")
else:
    print ("Il numero", numero, "è dispari")
print ("---FINE PROGRAMMA---")