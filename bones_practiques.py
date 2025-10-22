#!/usr/bin/env python
'''
Divisió entera. Calcula la divisió de 2 números
Institut Icària
Programació - 1r Batxillerat - Curs 25-26
Mostra la divisió, calcula el quocient i el residu
'''
__author__ = "Maksym Kuznietsov"
__contact__ = "mkutznietsov@instituticaria.cat"
__date__ = "2025/22/10"

a = int(input("Escriu el teu dividend"))
b = int(input("Esciu el teu divisor"))
quocient = a // b
residu = a % b
print(f"Divisió: {a}/{b}")
print("Quocient:", quocient)
print("Residu:", residu)
