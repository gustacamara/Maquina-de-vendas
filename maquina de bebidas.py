bebidas = [[1, "Coca-Cola", 3.75, 2],
            [2, "Pepsi", 3.67, 5],
            [3, "Monster", 9.96, 1],
            [4, "Café", 1.25, 100],
            [5, "Redbull", 13.99, 2]]

notasTroco = [["Notas de R$100", 0, 2, 100],
                ["Notas de R$50", 0, 1, 50],
                ["Notas de R$20", 0, 5, 20],
                ["Notas de R$10", 0, 3, 10],
                ["Notas de R$5", 0, 10, 5],
                ["Notas de R$2", 0, 20, 2],
                ["moedas de R$1", 0, 5, 1],
                ["moedas de R$0,50", 0, 5, 0.5],
                ["moedas de R$0,25", 0, 7, 0.25],
                ["moedas de R$0,10", 0, 10, 0.10],
                ["moedas de R$0,5", 0, 1, 0.05]]

def Usuario():#seleciona se é um cliente ou um administrador
    while True: #entrada do tipo de usuário
        usuario = input("cliente = 1\
                        \nadministrador = 2\
                        \nVocê é cliente ou um administrador? ")
        if usuario == "1":
            seleçãoDeBebidas()
            break
        elif usuario == "2":
            admin = input("Você é um administador! Deseja 'remover', 'adicionar' ou 'editar' um dos itens?")
            if admin == "remover" or admin =="adicionar" or "editar":
                print('')
                administrador(admin)
                break
        else:
            print("opção invalida! Tente novamente.")

def cliente(codigoBebida):#def que o cliente seleciona a bebida dele
    while True:
        pagarBebida = int(input(f"Entre com o valor deseja pagar seu {bebidas[codigoBebida][1]}: "))
        if pagarBebida < bebidas[codigoBebida][2]:
            print(f"\
                \nDinheiro insuficiente, entre com um valor maior ou igual ao da bebida!\
                \n")
        else:
            troco(pagarBebida, codigoBebida)
            break      
  
def seleçãoDeBebidas():#Seleciona bebidas a partir do modo cliente
    while True:
        print("As bebidas que podem ser escolhidos são:")
        for i in range(len(bebidas)):
            print(bebidas[i][0], " = ", bebidas[i][1])
        codigoBebida = int(input(f"Entre com algum código de bebida!\
                                \nEntre com um codigo: "))
        codigoBebida -= 1
        if codigoBebida not in range(len(bebidas)):
            print("\
                  \nOpção invalida, tente novamente!\
                  \n")
        elif codigoBebida in range(len(bebidas)):
            if bebidas[codigoBebida][3] > 0:
                print(f"\
                      \nbebida disponivel!\
                      \nO valor da bebida {bebidas[codigoBebida][1]} é: {bebidas[codigoBebida][2]}\
                      \n")
                cliente(codigoBebida)
                break
            else:
                print("\
                      \nNão temos mais unidades dessa bebida\
                      \n")
        else:
            break

def troco(pagarBebida, codigoBebida):# calcula o troco e caso n tenha moedas suficientes ele pede para trocar a bebida
    troco = pagarBebida - bebidas[codigoBebida][2]
    global notasTroco
    notastrocoCopia = []
    for i in notasTroco:
        notastrocoCopia.append(i.copy())
    for t in range(len(notasTroco)):# Parte que faz os contabiliza os trocos
        while troco - notastrocoCopia[t][3] >= 0 and  notastrocoCopia[t][2] > 0:
            troco -= notastrocoCopia[t][3]
            notastrocoCopia[t][1] += 1
            notastrocoCopia[t][2] -= 1
    if  troco >= 0.05:
        print("Que pena 😥, a maquina não tem troco o suficiente.\
            \nPor favor, escolha outra bebida😍")
        Usuario()
    else:
        notasTroco = notastrocoCopia
    for i in range(len(notasTroco)):
            if notasTroco[i][1] > 0:
                print(notasTroco[i][0], ' = ',notasTroco[i][1])
    bebidas[codigoBebida][3] -= 1
    print(f"A quantidade da bebida {bebidas[codigoBebida][1]} = {bebidas[codigoBebida][3]}")
    outraBebida = input("Deseja usar a máquina novamente?\
                        \nSim ou não :")
    if outraBebida == "sim" or outraBebida == "Sim":
        Usuario()
    elif outraBebida == "não" or outraBebida == "nao" or outraBebida == "Não" or outraBebida == "Nao":
        print("Que pena :( ")    

def administrador(admin):# função admnistrador, tem a capacidade de editar, remover ou apagar algum item da lista 
    while True:
# opção remover        
        if admin == "remover":
            for i in range(len(bebidas)):
                print(bebidas[i][0], " = ", bebidas[i][1])
            codigoBebida = int(input(f"Qual bebida quer remover?\
                                    \nEntre com o codigo dela: "))
            bebidas.remove(bebidas[codigoBebida - 1])
            renumeracao = 1
            for i in range(len(bebidas)):
                bebidas[i][0] = renumeracao
                renumeracao += 1
            Usuario()
            break
# opção adicionar
        elif admin == "adicionar":
            adicionar = input("Entre com as informações desse produto.\
                \n(nome, preço, unidades): ")
            ultimoCodigo = int(len(bebidas))
            adicionar = adicionar.split(", ")
            criarNovaBebida(adicionar, ultimoCodigo)
            break         
# opção editar
        elif admin == "editar":
            print("Os bebidas que podem ser escolhidos são:")
            for i in range(len(bebidas)):
                print(bebidas[i][0], " = ", bebidas[i][1])
            edição = int(input(f"Entre com o codigo da bebida que deseja editar!\
                                    \nEntre com um codigo: "))
            tipoDeEdição = int(input(f"\
                                 \n1 = {bebidas[edição - 1][1]}\
                                 \n2 = {bebidas[edição - 1][2]}\
                                 \n3 = {bebidas[edição - 1][3]}\
                                 \nQual desses voce deseja editar?"))
            if tipoDeEdição == 1:
                modificção = input(f"Entre com o novo nome da bebida {bebidas[edição - 1][1]}: ")
                bebidas[edição - 1][1] = modificção
                print("Prontinho! Agora você voltara para o Menu de usuario.")
                Usuario()
                break
            elif tipoDeEdição == 2:
                modificção = int (input(f"Entre com o novo valor da bebida {bebidas[edição - 1][2]}: "))
                bebidas[edição - 1][2] = modificção
                print("Prontinho! Agora você voltara para o Menu de usuario.")
                Usuario()
                break
            elif tipoDeEdição == 3:
                modificção = int (input(f"Entre com o nova quantidade da bebida {bebidas[edição - 1][3]}: "))
                bebidas[edição - 1][3] = modificção
                print("Prontinho! Agora você voltara para o Menu de usuario.")
                Usuario()
                break
            else:
                print("Opção invalida! Tente novamente.")
        else:
            print("Opção invalida! Tente novamente.")
            Usuario()
            break

def criarNovaBebida(adicionar, ultimoCodigo):#funçã que cria uma nova bebida
    adicionar[1] = float(adicionar[1])
    adicionar[2] = float(adicionar[2])
    bebidas.append([ultimoCodigo + 1, adicionar[0], adicionar[1], adicionar[2]])
    print("Mudança feita! A atulização ficou assim:")
    for j in range(len(bebidas)):
        print(bebidas[j][0], " = ", bebidas[j][1])
    print('')
    print("Agora você voltara para o menu de usuários!")
    Usuario()
Usuario()