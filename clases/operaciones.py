class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    
    def esImpar(self,entero):
        numero = int(entero)
        if numero %2 != 0:
            return True
        else:
            return False


    