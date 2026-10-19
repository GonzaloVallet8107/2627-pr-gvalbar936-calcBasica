def suma(num1 : float, num2: float)-> float:
    """Calcula la suma de dos números.

    Args:
        num1: El primer número.
        num2: El segundo número.

    Returns:
        El resultado de la suma.
    """
    suma = num1 + num2
    return suma

def restar(num1: float, num2: float)->float:
    """Calcula la resta de dos números.

    Args:
        num1: El primer número (minuendo).
        num2: El segundo número (sustraendo).

    Returns:
        El resultado de la resta.
    """
    resta = num1 - num2
    return resta

def multipicar(num1 : float, num2: float)-> float:
    """Calcula la multiplicación de dos números.

    Args:
        num1: El primer factor.
        num2: El segundo factor.

    Returns:
        El resultado de la multiplicación.
    """
    multi = num1 * num2
    return multi

def division(num1 : float, num2: float)-> float:
    """Calcula la división de dos números enteros.

    Args:
        num1: El dividendo.
        num2: El divisor.

    Returns:
        El resultado de la división si es posible.
    """
    if num2 == 0:
        print("Error. No se puede dividir entre 0 ")
    else:
        divi = num1 / num2
        return divi

def menu(primero,segundo)-> bool:
    """Muestra el menú y hace la selección del usuario.

    Args:
        primero: El primer operando introducido.
        segundo: El segundo operando introducido.

    Returns:
        True si el usuario escribe "fin" para terminar, False en caso contrario.
    """
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    pregunta:str = input("Que quieres hacer? (Fin para terminar):")
    if pregunta.lower() == "suma" or pregunta == "1" or pregunta =="sumar":
        print(f"Suma: {suma(primero,segundo)}")
    elif pregunta.lower() == "resta" or pregunta == "2" or pregunta =="restar":
        print(f"Resta: {restar(primero,segundo)}")
    elif pregunta.lower() == "multiplicar" or pregunta == "3":
        print(f"Multiplicar: {multipicar(primero,segundo)}")
    elif pregunta.lower() == "dividir" or pregunta == "4":
        print(f"Division: {division(primero,segundo)}")
    elif pregunta.lower() == "fin":
        return True
    return False

def main():
    
    try:
        terminar = False
        while terminar == False:
            print("Calculadora")
            numero1: float = float(input("Introduce el primer número: "))
            numero2: float = float(input("Introduce el segundo número: "))
            terminar = menu(numero1,numero2)
    except Exception as e:
        print(f"Introduce numeros. {e}")

if __name__ == "__main__":
    main()
