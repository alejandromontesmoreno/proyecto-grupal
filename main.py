from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    

    print(test.esImpar(7))
    print(test.esImpar(4))

    #Realiza aquí tu prueba
    lista = [1, 2, 2, 3, 4, 4, 5]
    print("Lista original:", lista)
    print("Lista sin duplicados:", test.eliminarDuplicados(lista))

    
    numeros = [5, 1, 9, 3, 7]
    print("Lista original:", numeros)
    print("Lista ordenada:", test.ordenarLista(numeros))
    
if __name__ == '__main__':
    main()    
    
    
    