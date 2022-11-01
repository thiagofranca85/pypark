from datetime import datetime, date, time
import os

# Pega Data e Horário Atual do Sistema
horaAtual = datetime.now()

def disponivel():
    os.system('cls')
    with open('estacionamento.txt') as file:
        lines = file.readlines()
    
    if len(lines)<10:
        pass
    else:
        print("Não há vagas disponíveis no momento!")
    print(f"Existem vagas disponíveis")
    
def entrada(carro):
    with open('estacionamento.txt', 'a') as arquivo:
        arquivo.write(str(carro)+"\n")

def tabelaPrecos():
    os.system('cls')
    print(f"\n{'*'*10} Tabela de Preços {'*'*10}\n\t1a e 2a Horas = R$5\n\tHoras Adicionais = R$2\n")

def saida(placa):
    arquivo = open('estacionamento.txt')

    placaEncontrada = False
    # Verifica se existe a placa no estacionamento e mostra os dados do veiculo
    for linha in arquivo:
        aux = eval(linha)

        if placa == aux['placa']:
            entradaHora = aux['entradaHora']
            entradaMinuto = aux['entradaMinuto']          
            placaEncontrada = True
            relatorio = linha # Customizar informações (Essa linha adiciona é pra customizar o TXT depois com o Nested Replace)
            print(relatorio)
        
        # Se não encontrar a placa mostra a mensagem abaixo
        if placaEncontrada == False:
            pass

    while True:
        # Hora de entrada vinda do txt pelas chaves acima
        horaEntrada = datetime.combine(date.today(), time(entradaHora, entradaMinuto))
        # Salva o Horário de Saída em Horas e Minutos usando o horaAtual.hour e horaAtual.minute como parametros.
        horaSaidaAtual = datetime.combine(date.today(), time(horaAtual.hour, horaAtual.minute)) 
      
        opcao = input("[1] Efetuar Pagamento\n[2] Voltar ao Menu\n>> ")

        match opcao:
            case '1':
                horaSaida = horaSaidaAtual - horaEntrada
                # Transforma as horas em um numero float através dos segundos pra calcular o valor a pagar
                calcHora = (horaSaida.seconds/60)/60 

                valor = 0
                if calcHora < 1:
                    valor = 5
                    print(f"O carro ficou estacionado por {horaSaida.seconds/60} minutos.")
                elif calcHora < 2:
                    valor = 10
                    print(f"O carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} hora(s).")
                elif calcHora > 2:
                    valor = ((round(calcHora) * 2) - 4) + 10
                    print(f"O carro ficou estacionado por {(horaSaida.seconds/60)/60:.1f} horas.")
                
                print(f"Valor R${valor:.2f}\n")
                # Caixa (valor)
            #variavel criada recebendo valor inteiro 
                index=0

                #variavel criada recebendo valor inteiro 
                flag=0

                #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
                arquivo = open("estacionamento.txt", "r") 

                #estrutura repeticao recebendo uma variavel line para ler o arquivo(txt)
                for line in arquivo:

                    #variavel index recebendo operador relacional de incremento
                    index +=1

                    #if condicional recebendo o clinteFind, que é o atributo principal da funcao,
                    # que recebe funcao interna do python eval(), permitindo assim manipular a linha atravez da chave condicional nome, ultilindo o meu dicionario inserido como um objeto
                    if placa == eval(line)['placa']:

                        #Variavel chave criada recebendo incremento do indice atraves da variavel index
                        chave = index

                        #variavel flag recendo incremento do dicionario

                        flag =1

                #variavel arquivo que representa arquivo txt recebendo funcao internalizada do python.        
                #close() fecha o arquivo aberto. Um arquivo fechado não pode mais ser lido ou escrito
                arquivo.close()

                # condional da variavel flag atribuindo atraves de operador relacional condicao de cliente nao encontrado 
                if flag == 0:
                    pass

                #condicional else, se nenhuma das condicoes estiverem nas condicionais acima o programa irá entra nesta condiçao
                else:

                    #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
                    with open('estacionamento.txt', 'r') as arquivo:

                        # variavel lines criada, recebendo a variavel que representa o caminho do txt.
                        # funcao readlines() Retorna todas as linhas do arquivo, como uma lista onde cada linha é um item  objeto de lista:
                        lines = arquivo.readlines()
                            
                        #Variavel criada recebendo valor inteiro igual a 1
                        posicao = 1
                
                        #funcao open recebendo  o caminho do arquivo, variavel referencia  arquivo txt letra(w) tem a funcao de escrever no arquivo
                        with open('estacionamento.txt', 'w') as arquivo:

                            #estrutura de repeticao com variavel criada lendo as linhas atraves da chave do dicionario
                            for line in lines:
                                # condicao if se a posicao for diferente da chave
                                if posicao != chave:

                                    #variavel arquivo recebendo a funcao escrita, ira percorrer linha a linha identificando se o valor digitado contem na lista
                                    arquivo.write(line)

                                #variavel posicao incrementando, se o valor da chave que foi digitado  o cliente é deletado
                                posicao += 1

                        #Print de saida do bloco           
                        print("Estacionamento Finalizado\n")
                break
            case _:
                print("Digite uma opção valida")
                

    
            






            # with open('estacionamento.txt') as arquivo:
            #     linhas = arquivo.readlines()

            # if placa == eval(linha)['placa']:
            #     del linhas['placa']
            
            # with open('estacionamento.txt', 'w') as arquivo:
            #     for linha in linhas:
            #         arquivo.write(linha)        