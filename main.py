# Desenvolvimento de um sistema com menu

# O sistema deve armazenar os dados em uma lista, e deve possuir um menu com as opções mínimas:
# Visualizar dados
# Adicionar item
# Remover item
# Salvar dados em um arquivo
# Carregar dados de um arquivo
# Sair/Encerrar

# O programa deve rodar em um loop infinito, que encerra quando o usuário escolher a opção de Sair.
#Sistema de cadastro de clientes
lista=[]
print("Cadrastro de Clientes")
while True:
    print("1-Visualizar dados")
    print("2-Adicionar item")
    print("3-Remover item")
    print("4- Modo edição de usuario")
    print("5-Salvar dados em um arquivo")
    print("6-Carregar dados de um arquivo")
    print("7-Sair/Encerrar")
    try:
        escolha=int(input("Digite a Opcão:"))
    except ValueError:
        print("Escolha errada, Escolha novamente")
        continue
    if escolha ==1:
        if len(lista)==0:
            print("Não existe nenhum conteudo para visualizar")
        else:
            for i,clientes in enumerate(lista):
                print(f"Dados do Clinte: {i+1}")
                print("Nome:",clientes[0])
                print("Idade:",clientes[1])
                print("Email:",clientes[2])
                print("Cpf:",clientes[3])
    elif escolha==2:
        usuario=[]
        nome=input("Digite seu Nome:")
        idade=input("Digite sua Idade:")
        email=input("Digite seu Email: ")
        Cpf=input("Digite seu Cpf:")
        usuario.append(nome)
        usuario.append(idade)
        usuario.append(email)
        usuario.append(Cpf)
        lista.append(usuario)
        print("Dados adicionados com sucesso")
    elif escolha==3:
        print(" Deseja remover algum dado?")
        removido=False
        Cpf_excluir=(input("Digite o CPF que deseja remover: "))
        for usuario in lista:
            if usuario[3]==Cpf_excluir:
                lista.remove(usuario)
                removido=True
        if removido==False:
            print("CPF não encontrado")
    elif escolha==4:
        print("Modo de Edição")
        for i in range(len(lista)):
            print(f"lista de usuarios:{lista[i]}")
        editar_dado=int(input("Digite dado do cliente q quer editar, 1- Nome, 2- Idade, 3- Email, 4- Cpf "))
        indice_usuario=int(input("Digite o indice do usuario q quer editar: "))
        print(f"dado antigo:{lista[indice_usuario][editar_dado]}")
        dado_novo=input("Digite o dado novo: ")
        lista[indice_usuario][editar_dado]=dado_novo
    elif escolha==5:
        with open("arquivo/arquivo_clientes","w") as f:
            f.write("")
            for cliente in lista:
                f.write(f"{cliente[0]},{cliente[1]},{cliente[2]},{cliente[3]}\n")
    elif escolha==6:
        lista.clear()
        with open("arquivo/arquivo_clientes", "r") as f:
            for linha in f.read().splitlines():
                lista.append(linha.split(","))
                print(linha)
    elif escolha==7:
        print("Obrigado por se Cadastrar, Volte Sempre!")
        break
