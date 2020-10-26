from os import system

class Calculadora:
    
    def Numeros(self):
        Valor = input("Que quieres SUMAR, RESTAR, MULTIPLICAR, DIVIDIR:")
        NumeroUno = input("Inglesa el primer numero:")
        NumeroDos = input("Inglesa el segundo numero:")
        
        system ('cls')
        if Valor == 'sumar':
            print(int(NumeroUno) + int(NumeroDos))
        if Valor == 'restar':
            print(int(NumeroUno) - int(NumeroDos))
        if Valor == 'multiplicar':
            print(int(NumeroUno) * int(NumeroDos))   
        if Valor == 'dividir':
            print(int(NumeroUno) / int(NumeroDos))
        Calculadora1.Numeros()



Calculadora1 = Calculadora()
Calculadora1.Numeros()