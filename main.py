from clases.operaciones import Operaciones

def main():
    test = Operaciones()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    #Prueba reemplazarEspacios
    resultado = test.reemplazarEspaciosPaulina("Probar función", "_")
    print(resultado)  

    
    
if __name__ == '__main__':
    main()    