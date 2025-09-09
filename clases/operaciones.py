class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    '''
    def operacionesAsignada(self):
        #Realizar la operación asignada
    '''

    def contarPalabrasTexto(self, texto, palabra):
        texto=texto.lower()
        palabra=palabra.lower()
        palabras=texto.split()
        print("En el texto " + texto + ", la palabra "+palabra+" aparece "+str(palabras.count(palabra)) + " veces")
        return palabras.count(palabra)

