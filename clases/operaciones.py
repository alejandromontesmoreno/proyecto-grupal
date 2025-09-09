class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    
    
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

