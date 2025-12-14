#Autor: Lucas dos Santos Souza
from funcoes import parenteses, WcM, posfixa, filainversa


print("Testes Função Parenteses:")
parenteses("(())-(()())-()()")
parenteses(")(-(()(-))((")
print("="*30)

print("Testes Função WcM:")
print(WcM("c"))
print(WcM("aca"))
print(WcM("bcb"))
print(WcM("bbabb"))
print(WcM("abcab"))
print("="*30)


print("Testes Função posfixa:")
print(posfixa("999*+"))
print(posfixa("34*52-/"))
print(posfixa("56+2*"))
print("="*30)


filainversa()