def checkout(placa):
    arquivo = open('estacionamento.txt')

    placaEncontrada = False
    for linha in arquivo:
        if placa == eval(linha)['placa']:
            placaEncontrada = True
            relatorio = linha # Customizar informações
            print(relatorio)
            horarioSaida = input("HORARIO SAÍDA: ")
            # if entrada - horarioSaida < 2:
            #     valorHora = 5
            # else:
            #     valorHora = 
            # valor = (entrada - saida) * valor
            # caixa(valor)
            with open('estacionamento.txt') as arquivo:
                linhas = arquivo.readlines()

            if placa == eval(linha)['placa']:
                del linhas['placa']
            
            with open('estacionamento.txt', 'w') as arquivo:
                for linha in linhas:
                    arquivo.write(linha)        

    if placaEncontrada == False:
        print("PLACA NÃO ENCONTRADA.")

    

 
