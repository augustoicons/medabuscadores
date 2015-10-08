#!/usr/bin/python2
# -*- coding: utf-8 -*-
import requests
from time import sleep

__author__ = 'Jose Augusto'
"""
Primeiro spider, responsável pelas bases monocráticas
"""


def spider():
    global primeiro_processo
    primeiro_processo = 000000001

    while True:
        arquivo = open('urls.txt', 'r')
        texto = arquivo.readlines()
        primeiro_processo = str(primeiro_processo)
        base_url = "http://www.stf.jus.br/portal/jurisprudencia/listarJurisprudenciaDetalhe.asp?s1=" \
                   + primeiro_processo + "&base=baseMonocraticas"
        primeiro_processo = int(primeiro_processo)
        response = requests.get(base_url)
        sleep(0.3)
        primeiro_processo += 1
        # condição para verificar se o urls.txt está preenchido, não está funcionando.... hahahaha
        if len(texto) < primeiro_processo:
            texto.append(base_url+"\n")
            arquivo = open('urls.txt', 'w')
            arquivo.writelines(texto)
            print(base_url)
        else:
            pass
        '''
        while len(texto) < primeiro_processo:
            texto.append(base_url+"\n")
            arquivo = open('urls.txt', 'w')
            arquivo.writelines(texto)'''
        arquivo.close()

        if response.status_code == 500:
            primeiro_processo += 1
            pass

        elif response.status_code != 200:
            break

if __name__ == "__main__":
    spider()
