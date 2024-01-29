import os

lista = []
continua = True

while continua:
    opcao = input("Escolha: [i]nserir, [a]pagar, [l]istar, [s]air\n").lower()

    if opcao == 'i':
        os.system('clear')
        item = input("Fale o item que deseja inserir:\n")
        lista.append(item)
    
    elif opcao == 'a':
        os.system('clear')
        apagar = input("Escolha o index que deseja deletar:\n")
        try:
            int_apagar=int(apagar)
            del lista[int_apagar]
        except:
            print("Não foi possível localizar este index:\n")
    
    elif opcao == 'l':
        os.system('clear')
        if len(lista) == 0:
            print("Lista vazia")
        else:
            for i , item in enumerate(lista):
                print(i,item)
    
    elif opcao == 's':
        os.system('clear')
        continua = False
    
    else:
        os.system('clear')
        print("Opção indisponível")