class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def reemplazarEspaciosPaulina(self, text, caracter):
        return text.replace(" ", caracter)
    
    