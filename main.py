from clases.operaciones import Operaciones

def main():
    test = Operaciones()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    #Realiza aquí tu prueba
    
    numeros = [5, 1, 9, 3, 7]
    print("Lista original:", numeros)
    print("Lista ordenada:", test.ordenarLista(numeros))
    
if __name__ == '__main__':
    main()    
    
    
    