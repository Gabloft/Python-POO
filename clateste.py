pessoas = []

while True:
    nome = input("Digite o nome (ou 'null' para sair): ").strip()
    if nome.lower() == "null":
        break

    idade = input("Digite a idade (ou 'null' para sair): ").strip()
    if idade.lower() == "null":
        break

    while not idade.isdigit():
        idade = input("Idade inválida. Digite um número: ").strip()

    pessoas.append({"nome": nome, "idade": int(idade)})

print("\nPessoas cadastradas:")
for pessoa in pessoas:
    print(f"Meu nome é {pessoa['nome']}, e eu tenho {pessoa['idade']} anos")
