from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    print(test.esImpar(7))
    print(test.esImpar(4))
    
    
if __name__ == '__main__':
    main()    