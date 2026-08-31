def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro n'est pas autorisée.")
    return a / b


if __name__ == "__main__":
    print("Bienvenue dans la calculatrice !")
    print("Addition : 5 + 3 =", addition(5, 3))
    print("Soustraction : 10 - 4 =", soustraction(10, 4))
    print("Multiplication : 6 * 7 =", multiplication(6, 7))
    print("Division : 20 / 4 =", division(20, 4))