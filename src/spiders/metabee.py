#!/usr/bin/python2
# -*- coding: utf-8 -*-
import requests
__author__ = 'Jose Augusto'
"""
Primeiro spider, responsável pelas bases monocráticas
"""


def spider():
    primeiro_processo = 000000001
    while True:
        arquivo = open('urls.txt', 'r')
        texto = arquivo.readlines()
        primeiro_processo = str(primeiro_processo)
        base_url = "http://www.stf.jus.br/portal/jurisprudencia/listarJurisprudenciaDetalhe.asp?s1=" \
                   + primeiro_processo + "&base=baseMonocraticas"
        primeiro_processo = int(primeiro_processo)
        response = requests.get(base_url)
        primeiro_processo += 1
        texto.append(base_url+"\n")
        arquivo = open('urls.txt', 'w')
        arquivo.writelines(texto)
        arquivo.close()

        if response.status_code != 200:
            if response.status_code == 500:
                primeiro_processo += 1
            break
        else:
            print(base_url)

if __name__ == "__main__":
    spider()
