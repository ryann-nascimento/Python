"""
def mensagem1():
    print("Eu sou Vasco!")

def mensagem2():
    return 'Vai dar Vasco!'

mensagem1()

texto = mensagem2()
print(texto)
"""


def lernotas():
    n=float(input('Digite uma nota para o aluno: '))
    return n

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Congratulations!")
    else:
        print("You're reproved!")


a = lernotas()
b = lernotas()
resultado(a,b)