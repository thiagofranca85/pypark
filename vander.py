from datetime import datetime

import os

def disponivel():
    os.system('cls')
    with open('estacionamento.txt') as file:
        lines = file.readlines()
    
    dispo = 0
    if len(lines)<10:
        dispo = 10 - len(lines)
    else:
        print("Não há vagas disponíveis no momento!")
    print(f"Existem {dispo} vagas disponíveis")
    
def entrada():
    os.system('cls')
    carro = list()
    dados = dict()
    dados['placa'] = str(input("Placa do Veículo: ")).upper().strip()
    dados['modelo'] = str(input("Marca/Modelo: ")).upper().strip()
    dados['cor'] = str(input("Cor do veículo: ")).upper().strip()
    dados['hrentrada'],dados['minentrada']  = str(input("Entrada\nHora: ")) , str(input("Minuto: "))
    carro.append(dados.copy())
    print(carro)
    
    with open('estacionamento.txt', 'a') as arquivo:
        arquivo.write(str(carro)+"\n")
