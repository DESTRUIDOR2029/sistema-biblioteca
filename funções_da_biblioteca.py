class livro:
    Titulo=""
    Autor=""
    Ano=0
    Codigo=""
    Quantidade=0
    Quantidade_disponivel=0
    Quantidade_emprestimo=0
# cadastro de livros
def book_register(banco):
    regt_book=livro()

    regt_book.Titulo=input("Nome do livro: ")
    regt_book.Autor=input("Autor do livro: ").split(",")[0].strip()
    regt_book.Ano=int(input("Ano da publicação do livro: "))
    regt_book.Quantidade=int(input("Quantidade de exemplares: "))
    regt_book.Quantidade_disponivel=regt_book.Quantidade
    regt_book.Codigo=input("Codigo/Id do livro:")

    while True:
        verifica=0
        for verifc_repeat_book_id in banco:
            if verifc_repeat_book_id.Codigo==regt_book.Codigo:
                verifica=1
                break
        if verifica==1:
            print("Codigo de livro já exitente insira outro Codigo não existente")
            regt_book.Codigo=input("Outro Codigo/Id para o livro:")
        else:
            break
    
    return regt_book

#consulta dados do livro
def consultar(code_or_author,banco_de_dd):
        encontrar=False
        posição=0

        for conslt in banco_de_dd:
            posição+=1
            # procura pelo codigo
            if conslt.Codigo==code_or_author:
                print(f"Titulo: {conslt.Titulo}\nAutor: {conslt.Autor}\nAno: {conslt.Ano}\nCodigo: {conslt.Codigo}\nExemplares disponíveis: {conslt.Quantidade_disponivel}\nExemplares em empréstimo: {conslt.Quantidade_emprestimo}")
                encontrar=True
                break
            else:
                 #procura pelo autor
                 if conslt.Autor.lower()==code_or_author.lower():
                    print(f"Titulo: {conslt.Titulo}\nAutor: {conslt.Autor}\nAno: {conslt.Ano}\nCodigo: {conslt.Codigo}\nExemplares disponíveis: {conslt.Quantidade_disponivel}\nExemplares em empréstimo: {conslt.Quantidade_emprestimo}")
                    encontrar=True
                    break

        if encontrar==False:
             print("Livro não encontrado")
        else:
            return posição
        

#altera dados
def alterar_(banco_de_dd):
    id_or_author=input("Qual o id ou nome do autor: ")
    localização=consultar(id_or_author,banco_de_dd)

    if localização==None:
        return
    
    else:
        localização-=1
        banco_de_dd[localização].Titulo=input("Nome do livro: ")
        banco_de_dd[localização].Autor=input("Autor do livro: ").split(",")[0].strip()
        banco_de_dd[localização].Ano=int(input("Ano da publicação do livro: "))
        banco_de_dd[localização].Quantidade=int(input("Quantidade de exemplares: "))
        banco_de_dd[localização].Quantidade_disponivel=int(input("Quantidade de exemplares para emprestimo: "))
        banco_de_dd[localização].Quantidade_emprestimo=banco_de_dd[localização].Quantidade-banco_de_dd[localização].Quantidade_disponivel

        return banco_de_dd
    

# Remove a posição do livro
def remove_book(code, banco_de_dd):
    conta=0
    enconntrar=False
    
    for conslt in range(len(banco_de_dd)):
        conta+=1
        if banco_de_dd[conslt].Codigo==code:
            enconntrar=True
            break
    if enconntrar==True:
        banco_de_dd.pop(conta-1)
        print("Livro removido")
    else:
        print("Livro não encontrado")
    return banco_de_dd   
    
#lista livros
def list_of_book(banco_de_dd):
    conta=0
    print("Dados")
    print("----------------------")
    if len(banco_de_dd)==0:
        print("Inventário vazio")
        return
    else:
        
        for book in banco_de_dd:
            conta+=1
            print(f"Livro {conta}:")
            print(f"\nTitulo: {book.Titulo}\nAno: {book.Ano}\nCódigo: {book.Codigo}\nNúmero de exemplares: {book.Quantidade}")
            print("----------------------")

# emprestimo
def loan_book(code,banco_de_dd):
    encontrado = False
    
    for consulta in range(len(banco_de_dd)):
        if banco_de_dd[consulta].Codigo == code:
            encontrado = True
            if banco_de_dd[consulta].Quantidade_disponivel>0 and banco_de_dd[consulta].Quantidade_disponivel<=banco_de_dd[consulta].Quantidade:
                banco_de_dd[consulta].Quantidade_disponivel-=1
                banco_de_dd[consulta].Quantidade_emprestimo+=1
                print(f"Restam {banco_de_dd[consulta].Quantidade_disponivel} exemplares desse")
                return banco_de_dd
            else:
                print("Todas as cópias desse livro estão em empréstimo")
            return banco_de_dd
    if encontrado==False:
        print("Livro não encontrado")
        return banco_de_dd

#devolução
def devol_book(code,banco_de_dd):
    encontrar=False
    return banco_de_dd
    
    for consulta in range(len(banco_de_dd)):
        if banco_de_dd[consulta].Codigo==code:
            encontrar=True
            if banco_de_dd[consulta].Quantidade_emprestimo>0 and banco_de_dd[consulta].Quantidade_emprestimo<=banco_de_dd[consulta].Quantidade:
                banco_de_dd[consulta].Quantidade_emprestimo-=1
                banco_de_dd[consulta].Quantidade_disponivel+=1
                print(f"Restam {banco_de_dd[consulta].Quantidade_emprestimo} exemplares desse em empréstimo")
                return banco_de_dd
            else:
                if banco_de_dd[consulta].Quantidade_emprestimo==0:
                    print("Nenhum copia desse exemplar está em empréstimo")
                    return banco_de_dd
    if encontrar==False:
        print("Livro não encontrado")
        return banco_de_dd

#ordena os elementos achando o maior valor neles e colocando na ultima posição
def ordenar(banco_de_dd):
    tamanho=len(banco_de_dd)

    for percorrer in range(tamanho):

        for indice in range(tamanho-(percorrer+1)):
            Titulo1=banco_de_dd[indice].Titulo
            prox_Titulo=banco_de_dd[indice+1].Titulo
            #analise os caracteres e o tamanho
            if Titulo1>prox_Titulo:
                memoria_antiga=banco_de_dd[indice] 
                banco_de_dd[indice]=banco_de_dd[indice+1]
                banco_de_dd[indice+1]=memoria_antiga
                
    return banco_de_dd
