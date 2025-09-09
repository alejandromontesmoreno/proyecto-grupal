from clases.operaciones import Operaciones

def main():
    test = Operaciones()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    #Realiza aquí tu prueba
    
    #Prueba contarPalabraTexto
    ejemploDiego=Operaciones()
    print(ejemploDiego.contarPalabrasTexto("Hola como estas hola hola como hola","hola"))
    
if __name__ == '__main__':
    main()    