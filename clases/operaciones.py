class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def eliminarDuplicados(self, lista):
        return list(set(lista))
    '''
    def operacionesAsignada(self):
        #Realizar la operación asignada
    '''
    
    def ordenarLista(self, lista):
        return sorted(lista)    

    def esImpar(self,entero):
        numero = int(entero)
        if numero %2 != 0:
            return True
        else:
            return False   

