from funções_da_biblioteca import *
banco_de_dados=[]
espaço="|----------------------|"
while True:
    print("\n +----------------------+")
    print(" |1.Cadastrar livro     |\n", espaço)
    print(" |2.Consultar livro     |\n", espaço)
    print(" |3.Alterar dados       |\n", espaço)    
    print(" |4.Remover livro       |\n", espaço)
    print(" |5.Listar todos        |\n", espaço)
    print(" |6.Realizar empréstimo |\n", espaço)
    print(" |7.Realizar devolução  |\n", espaço)
    print(" |8.Sair                |")
    print(" +----------------------+\n")
    condição=int(input("Selecione o número da seção que deseja acessar: "))
    if condição==8:
        print("+----------------------+\n|                      |")
        print("|  Programa encerrado  |")
        print("|                      |\n+----------------------+")
        break
    else:
        if condição==1:
            banco_de_dados.append(book_register(banco_de_dados))
            print("----------------------")
            print("Livro cadastrado")
            banco_de_dados=ordenar(banco_de_dados)
        else:
            if condição==2:
                Codigo=input("Insira o Codigo do livro ou nome do autor: ")
                consultar(Codigo,banco_de_dados)
            else:
                if condição==3:
                    banco_de_dados=alterar_(banco_de_dados)
                    banco_de_dados=ordenar(banco_de_dados)
                else:
                    if condição==4:
                        Codigo=input("Insira o código do livro para remover: ")
                        banco_de_dados=remove_book(Codigo,banco_de_dados)
                        banco_de_dados=ordenar(banco_de_dados)
                    else:
                        if condição==5:
                            list_of_book(banco_de_dados)
                        else:
                            if condição==6:
                                Codigo=input("Insira o código do livro para o empréstimo: ")
                                banco_de_dados=loan_book(Codigo,banco_de_dados)    
                            else:
                                if condição==7:
                                    Codigo=input("Insira o código do livro para o devolução: ")
                                    banco_de_dados=devol_book(Codigo,banco_de_dados)
                                else:
                                    continue