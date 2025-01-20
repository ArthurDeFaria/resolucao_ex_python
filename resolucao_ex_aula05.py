def soma(a, b):
    return a + b

def verificarPrimo(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True

def validarlogin(usuario_inserido, senha_inserida):
    usuario = "Arthur"
    senha = "senhaMuitoDificil"
    if usuario == usuario_inserido:
        if senha == senha_inserida:
            return True
    return False