from pycep_correios import get_address_from_cep, WebService
import requests


def get_empresa_from_cnpj(cnpj):
    response = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    return response


def get_endereco(cep):
    address = get_address_from_cep(cep, webservice=WebService.CORREIOS)
    return address
