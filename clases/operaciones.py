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