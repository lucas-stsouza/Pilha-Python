from pilha import Pilha
from fila import Fila


def parenteses(paren):
    p1 = Pilha()
    for i in paren:
        if i == '(':
            p1.empilhe(i)
        elif i == ')':
            if p1.vazio() == False:
                p1.desempilhe()
            else:
                p1.empilhe(i)


    if p1.__len__() == 0:
        print("Correto")
    else:
        print("Incorreto") # #


def WcM(letras):
    p = Pilha()
    cont = 0
    for i in letras:
        if i == 'c':
            cont += 1
    if cont != 1:
        return False

    posicao = letras.index('c')

    w = letras[:posicao]
    m = letras[posicao + 1:]

    for elem in w:
        if elem not in ('a', 'b'):
            return False

    for elem in m:
        if elem not in ('a', 'b'):
            return False

    for elem in w:
        p.empilhe(elem)

    for elem in m:
        if p.vazio() or elem != p.topo():
            return False
        p.desempilhe()


    return p.vazio()


def posfixa(conta):
    p = Pilha()
    for elem in conta:
        if (elem >= '0') and (elem <= '9'):
            p.empilhe(int(elem))
        else:
            b = p.desempilhe()
            a = p.desempilhe()

            if elem == '+':
                p.empilhe(a + b)
            elif elem == '-':
                p.empilhe(a - b)
            elif elem == '*':
                p.empilhe(a * b)
            elif elem == '/':
                p.empilhe(a / b)

    return p.topo()


def elementosfila():
    f1 = Fila()
    n = int(input("Entre com a quantidade de elementos da sua Fila:"))
    cont = 0
    while cont < n:
        f1.insere(input(f"Entre com o {cont+1}º elemento da Fila: "))
        cont += 1
    return f1

def filainversa():
    # inverter uma fila sem usar a função reverse e utilizando Pilha
    f = elementosfila()
    p1 = Pilha()
    a = int(f.tamanho())
    print(f'A fila é: {f.elemento}')
    for i in range(a):
        elem = f.remove()
        p1.empilhe(elem)
    for i in range(a):
        elem = p1.desempilhe()
        f.insere(elem)
    print(f'A fila invertida é: {f.elemento}')
