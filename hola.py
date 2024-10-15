class Suma:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular_suma(self):
        return self.numero1 + self.numero2


if __name__ == "__main__":
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        
        suma = Suma(num1, num2)
        
        resultado = suma.calcular_suma()
        print(f"La suma de {suma.numero1} y {suma.numero2} es: {resultado}")

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
