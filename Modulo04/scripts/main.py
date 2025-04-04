"""
Programa principal
Author: Richard Brosler
Version: 2025-04-03
"""

 # Lembre-se: Toda vez que alterar algo no código da função, é necessário salvar para as alterções surtirem efeito
import funcoes
from click import clear # importando somente a função clear, não o pacote inteiro
clear() # Limpa o console
funcoes.cabecalho(colunas=50,titulo="Bem vindo!")
funcoes.cabecalho("Olá turma, boa noite!",30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print("Fatorial de 5= ",funcoes.fatorial(1000)) # Não ocorre estouro de pilha
print("Fatorial de 6= ",funcoes.fatorial_rec(6)) # Stack  overflow para valor alto, teste com 1000. Encadeamento de chamada excedidocls