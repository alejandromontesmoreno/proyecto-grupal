from clases.operaciones import Operaciones

def main():

    test = Operaciones()


    test = Operaciones()
   
    #Prueba base
    #print(test.saludoAlejandroMontes())


    operaciones=Operaciones()


    
    #Prueba base
    print(operaciones.saludoAlejandroMontes())
    

    #Prueba reemplazarEspacios
    resultado = test.reemplazarEspaciosPaulina("Probado función", "_")
    print(resultado)  



    test = Operaciones()

    
    #Prueba base

    print(test.saludoAlejandroMontes())


    numeros = [3, 8, 1, 15, 6]
    resultado = test.maximo(numeros)
    print(resultado)

    #print(test.saludoAlejandroMontes())
   

    print(test.esImpar(7))
    print(test.esImpar(4))

    #Realiza aquí tu prueba

    print(test.promedioDiegoGarcia([1,2,3]))


    print(Operaciones.fibonacci(10))


    operaciones.generarTablaMultiplicar()


    print(test.minimoLista([2,4,5,100,1,30,5]))


    a=float(input('dame el primer número: '))
    b=float(input('dame el segundo número: '))
    c=float(input('dame el tercer número: '))


    print(test.esPar(4))  
    print(test.esPar(7))  

    lista = [1, 2, 2, 3, 4, 4, 5]
    print("Lista original:", lista)
    print("Lista sin duplicados:", test.eliminarDuplicados(lista))


    #Prueba contarPalabraTexto
    ejemploDiego=Operaciones()
    print(ejemploDiego.contarPalabrasTexto("Hola como estas hola hola como hola","hola"))

    numeros = [5, 1, 9, 3, 7]
    print("Lista original:", numeros)
    print("Lista ordenada:", test.ordenarLista(numeros))

    
if __name__ == '__main__':
    main()    
    
    
    