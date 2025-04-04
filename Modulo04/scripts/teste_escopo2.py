"""
Programa de teste de escopo de variáveis - 2
Author: Richard Brosler
Version: 2025-04-03
"""
from click import clear
def calculo():
    global c, d # variáveis globais são "enxergadas" por qualquer parte do código
    a = 5
    b = a + c # c=10 variavel global
    c = 30 # c é alterada
    d = 50
    return b
# programa principal
c = 10
print(calculo())
print("Valor de c=",c,"Valor de D=",d)

# Variáveis globais pode ser dificeis de ser gerenciadas por isso não é muito recomendado a utilização