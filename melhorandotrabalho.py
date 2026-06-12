#Funções
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite apenas números inteiros.")

def ler_opcao(mensagem, opcoes_validas):
    while True:
        entrada = input(mensagem).strip().upper()
        if entrada in opcoes_validas:
            return entrada
        print(f"Valor inválido! Digite uma das opções: {', '.join(opcoes_validas)}.")

# Valores iniciais
valor_aluguel = 0
valor_contrato = 2000.00

#Menu de Seleção
print("=== GERADOR DE ORÇAMENTO - IMOBILIÁRIA R.M ===")
print("1 - Apartamento")
print("2 - Casa")
print("3 - Estúdio")

#Entrada do Usuário

opcao = ler_inteiro("Escolha o tipo de imóvel (1-3): ", 1, 3)

tipo_imovel = ""

#Condições

if opcao == 1:
    tipo_imovel = "Apartamento"
    valor_aluguel = 700.00

    quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)
    if quartos == 2:
        valor_aluguel += 200.00

    garagem = input("Deseja vaga de garagem? (S/N): ").upper()
    if garagem == "S":
        valor_aluguel += 300.00

    criancas = input("Possui crianças? (S/N): ").upper()
    if criancas == "N":
        valor_aluguel *= 0.95  # desconto de 5%

elif opcao == 2:
    tipo_imovel = "Casa"
    valor_aluguel = 900.00

    quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)
    if quartos == 2:
        valor_aluguel += 250.00

    garagem = ler_opcao("Deseja vaga de garagem? (S/N): ", ["S", "N"])
    if garagem == "S":
        valor_aluguel += 300.00

elif opcao == 3:
    tipo_imovel = "Estúdio"
    valor_aluguel = 1200.00

        estacionamento = ler_opcao("Deseja vagas de estacionamento? (S/N): " ,["S", "N"])
    if estacionamento == "S":
        valor_aluguel += 250.00
        adicionais = int(input("Quantas vagas adicionais deseja? "))
        valor_aluguel += adicionais * 60.00


# Parcelamento do contrato
parcelas = ler_inteiro("Número de parcelas do contrato (1 a 5): ", 1, 5)


valor_parcela = valor_contrato / parcelas

# Exibição do orçamento
print("\n===== ORÇAMENTO =====")
print(f"Tipo do imóvel: {tipo_imovel}")
print(f"Valor do aluguel mensal: R$ {valor_aluguel:.2f}")
print(f"Valor do contrato: R$ {valor_contrato:.2f}")
print(f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f}")

