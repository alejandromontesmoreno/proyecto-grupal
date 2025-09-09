class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"


        self.num=0


    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    


    def generarTablaMultiplicar(self):
        self.num = int(input("Dame un numero: "))    
        print(f"\nTabla de multiplicar del {self.num}:")
        print("-" * 25)
        for i in range(1, 11):  # desde 1 hasta 10
            resultado = self.num * i
            print(f"{self.num} x {i} = {resultado}")


    

    '''
    def operacionesAsignada(self):
        #Realizar la operación asignada
    '''

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (n-1) + (n-2)


    def minimoLista(self, lista):
        return f"El mínimo es: {min(lista)}"

    
    def numeroMayo(self,a,b,c):
        mayor=a
        if (b>mayor):
            mayor=b
        if (c>mayor):
            mayor=c
        return mayor
    


    def eliminarDuplicados(self, lista):
        return list(set(lista))

    def ordenarLista(self, lista):
        return sorted(lista)    

    def esImpar(self,entero):
        numero = int(entero)
        if numero %2 != 0:
            return True
        else:
            return False   

    def contarPalabrasTexto(self, texto, palabra):
        texto=texto.lower()
        palabra=palabra.lower()
        palabras=texto.split()
        print("En el texto " + texto + ", la palabra "+palabra+" aparece "+str(palabras.count(palabra)) + " veces")
        return palabras.count(palabra)

     #Regresar True si el número es par False en caso contrario
    def esPar(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def maximo(self, lista):
        if not lista:
            return None  
        return max(lista)


