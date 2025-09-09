from clases.operaciones import Operaciones

def main():
    test = Operaciones()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    #Realiza aquí tu prueba
    a=float(input('dame el primer número: '))
    b=float(input('dame el segundo número: '))
    c=float(input('dame el tercer número: '))
    print(test.numeroMayo(a,b,c))
    
if __name__ == '__main__':
    main()    