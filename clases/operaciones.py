class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    '''
    def operacionesAsignada(self):
        #Realizar la operación asignada
    '''
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (n-1) + (n-2)

