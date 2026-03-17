clientes = {}
pets = []
servicos_realizados = []


servicos_disponiveis = {
1: {'nome': 'Banho', 'preco': 80},
2: {'nome': 'Tosa', 'preco': 100},
3: {'nome': 'Consulta', 'preco': 120},
4: {'nome': 'Hospedagem', 'preco': 150}
}

def cadastrar_cliente():
    cpf = input("CPF: ")

    if cpf in clientes:
        print("CPF já cadastrado")
        return

    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    endereco = {
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado
    }

    clientes[cpf] = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
        "gasto": 0
    }

    print("Cliente cadastrado")

def cadastrar_pet():
    cpf = input("CPF do dono: ")

    if cpf not in clientes:
        print("Cliente não encontrado")
        return

    nome = input("Nome do pet: ")
    especie = input("Espécie: ")

    pet = {
        "nome": nome,
        "especie": especie,
        "cpf_dono": cpf,
        "total_servicos": 0
    }

    pets.append(pet)

    print("Pet cadastrado")

def registrar_servico():
    nome_pet = input("Nome do pet: ")

    pet_encontrado = None

    for pet in pets:
        if pet["nome"] == nome_pet:
            pet_encontrado = pet

    if pet_encontrado is None:
        print("Pet não encontrado")
        return

    print("Serviços disponíveis")

    for chave, valor in servicos_disponiveis.items():
        print(chave, "-", valor["nome"], "-", valor["preco"])

    escolha = int(input("Escolha o serviço: "))

    if escolha not in servicos_disponiveis:
        print("Serviço inválido")
        return

    servico = servicos_disponiveis[escolha]

    registro = {
        "pet": nome_pet,
        "servico": servico["nome"],
        "preco": servico["preco"]
    }

    servicos_realizados.append(registro)

    pet_encontrado["total_servicos"] += 1

    cpf = pet_encontrado["cpf_dono"]
    clientes[cpf]["gasto"] += servico["preco"]

    print("Serviço registrado")

def relatorios():
    total_clientes = len(clientes)
    total_pets = len(pets)
    total_servicos = len(servicos_realizados)

    faturamento = 0

    for servico in servicos_realizados:
        faturamento += servico["preco"]

    print("Total de clientes:", total_clientes)
    print("Total de pets:", total_pets)
    print("Total de serviços:", total_servicos)
    print("Faturamento total:", faturamento)

def listar_pets_por_cpf():
    cpf = input("CPF do dono: ")

    for pet in pets:
        if pet["cpf_dono"] == cpf:
            print(pet["nome"], "-", pet["especie"])

def cliente_que_mais_gastou():
    maior = 0
    nome = ""

    for cpf, cliente in clientes.items():
        if cliente["gasto"] > maior:
            maior = cliente["gasto"]
            nome = cliente["nome"]

    if nome == "":
        print("Nenhum gasto registrado")
    else:
        print("Cliente que mais gastou:", nome, "-", maior)

def ticket_medio():
    if len(servicos_realizados) == 0:
        print("Ticket médio: 0")
        return

    total = 0

    for s in servicos_realizados:
        total += s["preco"]

    media = total / len(servicos_realizados)

    print("Ticket médio:", media)

def menu():
    while True:

        print()
        print("1 Cadastrar cliente")
        print("2 Cadastrar pet")
        print("3 Registrar serviço")
        print("4 Relatórios")
        print("5 Listar pets por CPF")
        print("6 Cliente que mais gastou")
        print("7 Ticket médio")
        print("0 Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            cadastrar_pet()

        elif opcao == "3":
            registrar_servico()

        elif opcao == "4":
            relatorios()

        elif opcao == "5":
            listar_pets_por_cpf()

        elif opcao == "6":
            cliente_que_mais_gastou()

        elif opcao == "7":
            ticket_medio()

        elif opcao == "0":
            break

        else:
            print("Opção inválida")

menu()

