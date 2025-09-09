class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    

    def maximo(self, lista):
        if not lista:
            return None  
        return max(lista)