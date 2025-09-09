from clases.operaciones import Nombres

def main():
    test = Nombres()
    
    #Prueba base
    print(test.saludoAlejandroMontes())

    numeros = [3, 8, 1, 15, 6]
    resultado = test.maximo(numeros)
    print(resultado)

    
    
if __name__ == '__main__':
    main()    