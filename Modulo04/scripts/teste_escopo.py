"""
Código para demonstrar escopo de variáveis no python
Author> Richard Brosler
Version: 2025-04-03
"""
from click import clear
# Definindo uma função, será usada posteriormente
def calculo():
    a = 5 # variável é criada dentro da função
    b = a + c # variável é criada dentro da função
    # c = 30 # Se descomentado dá erro porque a variável c passa a ser local
    return b
# Programa principal
c = 10 # Dentro do programa principal, desde que definida antes de chamada. 
clear()
print(calculo()) # chamada da função
# print(a) # Erro, pois a variavel a esta apenas definida dentro da função