



def suma(num1 : float, num2: float)-> float:
    suma = num1 + num2
    return suma

def restar(num1: float, num2: float)->float:
    resta = num1 - num2
    return resta

def multipicar(num1 : float, num2: float)-> float:
    multi = num1 * num2
    return multi

def division(num1 : int, num2: int)-> int:
    if num2 == 0:
        print("Error. No se puede dividir entre 0 ")
    else:
        divi = num1 / num2
        return divi

def main():
    try:
        numero1: float = float(input("Introduce el primer número: "))
        numero2: float = float(input("Introduce el segundo número: "))
        print(f"Suma: {suma(numero1,numero2)})")
        print(f"Resta: {restar(numero1,numero2)}")
        print(f"Multiplicar: {multipicar(numero1,numero2)}")
        print(f"Division: {division(numero1,numero2)}")
    except Exception as e:
        print(f"Introduce numeros. {e}")

if __name__ == "__main__":
    main()