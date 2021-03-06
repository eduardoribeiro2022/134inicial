import csv

import pytest

from main import somar, subtrair, multiplicar, dividir


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


def teste_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_subtrair():
    # 1 - Configura
    # 1.1 - Dados de entrada / Valores do teste
    numero_a = 8
    numero_b = 7

    # 1.2 - Resultados Esperados
    resultado_esperado = 1

    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('//Users//eduardo//PycharmProjects//134inicial//vendors//csv//massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = subtrair(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)


def teste_multiplicar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 56

    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 3

    # 1.2 - Resultados esperado
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 0

    # 1.2 - Resultados esperado
    resultado_esperado = 'Não dividiras por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


# lista para uso como massa de teste (Tupla)
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('//Users//eduardo//PycharmProjects//134inicial//vendors//csv//massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)

# TDD - Test Drive Development
#       Desenvolvimento Direcionado por Teste
#
# - Criar todos os tester de unidade do começo
# - Executar todos os testes pelo menos 1 vez por dia
#
# Imagine que você no 1º dia (nada pronto)
# Você executa todos os tester - o que acontece?
# Dia 01 - Falhou 100 - Passou 000
# Dia 02 - Falhou 095 - Passou 005
# Dia 03 - Falhou 090 - Passou 010
# Dia 04 - Falhou 088 - Passou 012
# Dia 05 - Falhou 081 - Passou 019
# Dia 06 - Falhou 075 - Passou 025
# Informação sobre o progresso
# Insistir mais um dia      1 + 1 = 2?
# Pedir ajuda               1 + 2 = 3
# Devolver e pegar outra    1 + 1 = 2!
# Tudo certo!               1 + 2 = 4
# TDD: Teste é uma medida de progresso

# CI: Continuou Integration
# IC: Integração Continua

# (Build) --> Suite de Testes --------> (Build)
#               Automatizada   Passou
# Ambiente                              Então, move >> Ambiente
# de Desenvolvimento                                    de Teste

# CD: Continuou Delivery
# EC: Entrega continua

# (Build)  -->   Suite  ->>  (Build) ------>  (Build)
#   DEV         de Teste      Teste   Muitos   Produção
#                                     Testes
