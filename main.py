from clases.operaciones import Nombres

def main():
    test = Nombres()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    #Realiza aquí tu prueba
    lista = [1, 2, 2, 3, 4, 4, 5]
    print("Lista original:", lista)
    print("Lista sin duplicados:", test.eliminarDuplicados(lista))
    
    
if __name__ == '__main__':
    main()    