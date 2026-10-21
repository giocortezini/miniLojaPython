cadastroCliente = []

print("\nSISTEMA DE CADASTRO DE CLIENTE")

while True:
    print(f"\nCadastrando o {len(cadastroCliente) + 1}º cliente:")

    codigo = int(input("Digite o código do cliente: "))
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF com ponto e traço: ")

    cliente = {
        "código": codigo,
        "nome": nome,
        "cpf": cpf
    }

    cadastroCliente.append(cliente)
    print("Cliente cadastrado com sucesso!")

    if len(cadastroCliente) >= 3:
        resp = input("Deseja finalizar os cadastros (S/N)? ").upper()
        if resp == "S":
            break

cadastroFunc = []

print("\nSISTEMA DE CADASTRO DE FUNCIONÁRIO")

while True:
    print(f"\nCadastrando o {len(cadastroFunc) + 1}º funcionário:")

    codigo = int(input("Digite o código do funcionário(a): "))
    nome = input("Digite o nome do funcionário(a): ")
    cargo = input("Digite o cargo do funcionário(a): ")

    funcionario = {
        "código": codigo,
        "nome": nome,
        "cargo": cargo
    }

    cadastroFunc.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

    if len(cadastroFunc) >= 3:
        resp = input("Deseja finalizar os cadastros (S/N)? ").upper()
        if resp == "S":
            break

cadastroProd = []

print("\nSISTEMA DE CADASTRO DE PRODUTO")

while True:
    print(f"\nCadastrando o {len(cadastroProd) + 1}º produto:")

    codigo = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantEstoq = int(input("Digite a quantidade de produtos em estoque: "))

    produto = {
        "código": codigo,
        "nome": nome,
        "preco": preco,
        "quantEstoq": quantEstoq
    }

    cadastroProd.append(produto)
    print("Produto cadastrado com sucesso!")

    if len(cadastroProd) >= 5:
        resp = input("Deseja finalizar os cadastros (S/N)? ").upper()
        if resp == "S":
            break

print("\n====MENU DE CONSULTAS E VENDAS====")
print("\n1 - Consultar clientes")
print("\n2 - Consultar funcionários")
print("\n3 - Consultar produtos")
print("\n4 - Consultar formas de pagamento")
print("\n5 - Realizar uma venda")
print("\n0 - Encerrar o sistema")
opcao = int(input("\nEscolha uma opção: "))

if opcao == 1:
    print("\nSegue a lista de clientes:\n")
    for cliente in cadastroCliente:
        print(f"Código: {cliente['código']} | Nome: {cliente['nome']} | CPF: {cliente['cpf']}")
elif opcao == 2:
    print("\nSegue a lista de funcionários:\n")
    for funcionario in cadastroFunc:
        print(f"Código: {funcionario['código']} | Nome: {funcionario['nome']} | Cargo: {funcionario['cargo']}")
elif opcao == 3:
    print("\nSegue a lista de produtos:\n")
    for produto in cadastroProd:
        print(f"Produto: {produto['código']} | Nome: {produto['nome']} | Preço: {produto['preco']} | Quantidade em estoque: {produto['quantEstoq']}")
elif opcao == 4:
    print("\nSegue as opções de pagamento:\n")
    opcaoPag = ("Dinheiro", "PIX", "Débito", "Crédito")
    for i, forma in enumerate(opcaoPag, start=1):
        print(f"Opção {i}: {forma}")