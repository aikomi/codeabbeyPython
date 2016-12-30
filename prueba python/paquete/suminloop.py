'''
Created on Dec 29, 2016

@author: emp
'''
entradas=int(input("numero de entradas"))
lista=input('ingrese los numeros')
arreglo=lista.split()
total=0
for elemento in arreglo:
    total=total+int(elemento)
print(total)
       
