""" Probando Pyflakes
Probando pycodestyle
Probando pylint
Probando flake8
Probando """


def sumar(a, b):
    resultado = a+b
    return resultado


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a/b


x = 10
y = 0
print(dividir(x, y))
