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
    