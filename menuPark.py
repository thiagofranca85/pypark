poli = "*" *28

def menu():
    #print ultilizando polimorfismo e quebra de linhas
    print(f"\n{poli} \nBem-vindo ao Menu do pyPark\n{poli}\n") 
    
    #variavel com input para escolher uma das opçoes
    escolha = input("Escolha a Opção Desejada:\n 1 => Entrada de Veículo\n 2 => Tabela de Preços\n 3 => Saída de Veículo\n 4 => Fechamento\n>>>") 
    
    #
    match escolha:
        case "1":
            entrada()
        case "2":
            tabelaPreços()
        case "3":
            saida()
        case "4":
            fechamento()
        case _:
            print("Ainda em desenvolvimento...")
menu()
    