import pyodbc



def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Paolla Oliveira                                             |')
    print('|                                                             |')
    print('| Versão 1.0 de 30/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def connect() -> bool:
    
    try:
        global connection
        connection = pyodbc.connect(
            driver = "{SQL Server}", #fabricante
            server = "143.106.250.84", #maquina onde esta o banco de dados
            database = "BD23330", #banco de dados
            uid = "BD23330", #LOGIN
            pwd = "BD23330" #SENHA
        ) # xxxxx é seu RA
        return True
    except:
        return False

def esta_cadastrado (nom):
    # cursor e um objeto que permite que 
    #nosso programa executre comandos SQL
    #la no sevidor
    cursor = connection.cursor()
    
    command = f"SELECT * FROM crud.contatos WHERE nome='{nom}'"
        
    try:
        #tentar executar o comando no banco de dados
        cursor.execute(command)
        #como select não altera nada no BD, não faz sentido pensar
        #em aplicar as alterações; por isso não tem cursor.commit()
        dados_selecionados=cursor.fetchall() #fetchall da uma listona
                                             #contendo 0 ou mais listinhas;
                                             #cada listinha seria uma linha
                                             #trazida pelo select;
                                             #neste caso, dará uma listona
                                             #contendo 0 ou 1 listinha(s);
                                             #isso pq ou nao tem o nome
                                             #procurado, ou tem 1 só vez
        return [True,dados_selecionados]
    except:
        #em caso de erro ele vai retornar falso 
        return [False,[]]

def incluir ():
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=esta_cadastrado(nome)
        sucessoNoAcessoAoBD = resposta[0]
        dados_selecionados  = resposta[1]

        if not sucessoNoAcessoAoBD or dados_selecionados!=[]:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    try:
        # cursor e um objeto que permite que 
        #nosso programa executre comandos SQL
        #la no sevidor
        cursor = connection.cursor()

        command= "INSERT INTO crud.contatos "+\
                 "(nome,aniversario,endereco,telefone,celular,email) "+\
                 "VALUES"+\
                f"('{nome}','{aniversario}','{endereco}','{telefone}','{celular}','{email}')"

        cursor.execute(command)
        cursor.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("Cadastro mal sucedido!")


def procurar ():
    achou = False
    #posicaoPessoa = -1
    n = ""
    while True:
        n = input("Qual nome está procurando?: ")
        for i in range (len(dados_selecionados)):
            if n == [i][0]:
                achou = True
                #posicaoPessoa = i
                break
        if achou:
            break
        else:
            print("Nome nao cadastrado!")
            
    aniversario = [0][1]
    endereco = [0][2]
    telefone = [0][3]
    celular = [0][4]
    email = [0][5]       

    print(n,aniversario, endereco, telefone, celular, email)

    try:
        # cursor e um objeto que permite que 
        #nosso programa executre comandos SQL
        #la no sevidor
        cursor = connection.cursor()

        command= "INSERT INTO crud.contatos "+\
                 "(nome,aniversario,endereco,telefone,celular,email) "+\
                 "VALUES"+\
                f"('{nome}','{aniversario}','{endereco}','{telefone}','{celular}','{email}')"

        cursor.execute(command)
        cursor.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("Cadastro mal sucedido!")
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.

def atualizar (dadosSelecionados):
    n = input("Qual cadastro deseja atualizar? ")
    while True:
        
        for i in range(len(dadosSelecionados)):
            if n not in dadosSelecionados[i][0]:
                print("Nao existe essa pessoa!")
            else:
                print("Escolha uma opção para atualizar!")
                print("[0]Nome  "\
                    "[1]Aniversario  "\
                    "[2]Endereço  "\
                    "[3]Telefone  "\
                    "[4]celular  "\
                    "[5]Email  "\
                    "[6]Sair") 
                
        at = int(input("Qual dado quer atualizar? "))

        if at == 0:
            dadosSelecionados[0][0] =input("Qual nome? ")
            print(dadosSelecionados)
        elif at == 1:
            dadosSelecionados[0][1] = input("que dia de aniversario? ")
            print(dadosSelecionados)
        elif at == 2:
            dadosSelecionados[0][2] = input("qual enderço? ")
            print(dadosSelecionados)
        elif at == 3:
            dadosSelecionados[0][3] = input("Qual telefone? ")
            print(dadosSelecionados)
        elif at == 4:
            dadosSelecionados[0][4] = input("Qual celular? ")
            print(dadosSelecionados)
        elif at == 5:
            dadosSelecionados[0][5] = input("Qual email? ")
            print(dadosSelecionados)
        elif at == 6:
            break
    
    print(dadosSelecionados)

    try:
        # cursor e um objeto que permite que 
        #nosso programa executre comandos SQL
        #la no sevidor
        cursor = connection.cursor()

        command= "INSERT INTO crud.contatos "+\
                 "(nome,aniversario,endereco,telefone,celular,email) "+\
                 "VALUES"+\
                f"('{dadosSelecionados}')"

        cursor.execute(command)
        cursor.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("Cadastro mal sucedido!")


    # Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
    # endereco, ou telefone, ou celular, ou email, ou finalizar as
    # atualizações; ficar pedindo para digitar a opção até digitar uma
    # opção válida; realizar a atulização solicitada; até ser escolhida a
    # opção de finalizar as atualizações.
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU

def listar (dadosSelecionados):

    if len(dadosSelecionados):
        print(dadosSelecionados)
    else:
        print("Esse contato não está cadastrado")

    try:
        # cursor e um objeto que permite que 
        #nosso programa executre comandos SQL
        #la no sevidor
        cursor = connection.cursor()

        command= "INSERT INTO crud.contatos "+\
                 "(nome,aniversario,endereco,telefone,celular,email) "+\
                 "VALUES"

        cursor.execute(command)
        cursor.commit()
        print("Cadastro realizado com sucesso!")
    except:
        print("Cadastro mal sucedido!")

    # implementar aqui a listagem de todos os dados de todos
    # os contatos cadastrados
    # printar aviso de que não há contatos cadastrados se
    # esse for o caso

def excluir ():
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=esta_cadastrado(nome)
        sucessoNoAcessoAoBD = resposta[0]
        dados_selecionados  = resposta[1]

        if not sucessoNoAcessoAoBD or dados_selecionados==[]:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
            
    print('Aniversario:',dados_selecionados[0][2])
    print('Endereco...:',dados_selecionados[0][3])
    print('Telefone...:',dados_selecionados[0][4])
    print('Celular....:',dados_selecionados[0][5])
    print('e-mail.....:',dados_selecionados[0][6])
    
    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        try:
            #cursor e um objeto que permite que 
            #nosso programa executre comandos SQL
            #la no sevidor
            cursor = connection.cursor()

            command= "DELETE FROM crud.contatos "+\
                    f"WHERE nome='{nome}'"

            cursor.execute(command)
            cursor.commit()
            print('Remoção realizada com sucesso!')
        except:
            print("Remoção mal sucedida!")
    else:
        print('Remoção não realizada!')


# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()
sucessoNoAcessoAoBD = connect()
if not sucessoNoAcessoAoBD:
    print("Falha ao conectar-se ao SQL Severver")
    exit() # encerra o programa



menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir()
    elif opcao==2:
        procurar()
    elif opcao==3:
        atualizar()
    elif opcao==4:
        listar()
    elif opcao==5:
        excluir()
        
connection.close()
print('OBRIGADO POR USAR ESTE PROGRAMA!')
