# Bibliotecas
import json

import pytest
import requests
#biblioteca pra testes API

# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

# Definições de funções (defs)

def teste_incluir_pet():
    # Configura / Prepara
    # Dados de entrada provem de pet1.json

    # Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 2166513
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('//Users//eduardo//PycharmProjects//134inicial//vendors//json//pet1.json')
    )


    # Valida

    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_consultar_pet():
    # Configura
    # Entrada
    pet_id = '2166513'

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 2166513
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"


    # Executa
    resultado_obtido = requests.get(
        url=url + '/'+ pet_id,
        headers=headers

    )

    # Valida

    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))


    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def teste_alterar_pet():
    # Configura
    # Dados de Entrada virão do pet2.json

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 2166513
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"
    pet_status_esperado = 'pending'

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('//Users//eduardo//PycharmProjects//134inicial//vendors//json//pet2.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado