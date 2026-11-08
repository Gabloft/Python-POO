import math


class Calculadora:
    """Calculadora básica com as quatro operações e histórico."""

    def __init__(self):
        self._historico = []  # protegido: acesse pelos métodos

    def somar(self, a, b):
        return self._registrar(f"{a} + {b}", a + b)

    def subtrair(self, a, b):
        return self._registrar(f"{a} - {b}", a - b)

    def multiplicar(self, a, b):
        return self._registrar(f"{a} x {b}", a * b)

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return self._registrar(f"{a} / {b}", a / b)

    def _registrar(self, expressao, resultado):
        self._historico.append(f"{expressao} = {resultado}")
        return resultado

    def get_historico(self):
        return list(self._historico)

    def limpar_historico(self):
        self._historico.clear()


class CalculadoraCientifica(Calculadora):
    """Herda da Calculadora e adiciona operações extras."""

    def potencia(self, a, b):
        return self._registrar(f"{a} ^ {b}", a ** b)

    def raiz(self, a):
        if a < 0:
            raise ValueError("Não existe raiz real de número negativo.")
        return self._registrar(f"√{a}", math.sqrt(a))

    def porcentagem(self, a, b):
        return self._registrar(f"{b}% de {a}", a * b / 100)

    def dividir(self, a, b):
        # Usa a divisão da classe mãe e arredonda o resultado
        resultado = super().dividir(a, b)
        return round(resultado, 10)


def converter_numero(texto):
    numero = float(texto.replace(",", "."))
    return int(numero) if numero.is_integer() else numero


def ler_numeros(mensagem, qtd):
    """Lê `qtd` números digitados na mesma linha, separados por espaço."""
    while True:
        partes = input(mensagem).split()
        if len(partes) != qtd:
            print(f"Digite exatamente {qtd} número(s), separados por espaço.")
            continue
        try:
            return [converter_numero(p) for p in partes]
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def main():
    calc = CalculadoraCientifica()

    # opção: (nome, método, quantidade de números)
    opcoes = {
        "1": ("Somar", calc.somar, 2),
        "2": ("Subtrair", calc.subtrair, 2),
        "3": ("Multiplicar", calc.multiplicar, 2),
        "4": ("Dividir", calc.dividir, 2),
        "5": ("Potência", calc.potencia, 2),
        "6": ("Raiz quadrada", calc.raiz, 1),
        "7": ("Porcentagem", calc.porcentagem, 2),
    }

    while True:
        print("\n===== CALCULADORA =====")
        for chave, (nome, _, _) in opcoes.items():
            print(f"{chave} - {nome}")
        print("8 - Ver histórico")
        print("9 - Limpar histórico")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Até mais!")
            break
        elif escolha == "8":
            historico = calc.get_historico()
            if not historico:
                print("Histórico vazio.")
            for linha in historico:
                print(linha)
        elif escolha == "9":
            calc.limpar_historico()
            print("Histórico limpo.")
        elif escolha in opcoes:
            nome, metodo, qtd = opcoes[escolha]
            if qtd == 1:
                numeros = ler_numeros("Digite o número: ", 1)
            elif escolha == "7":
                numeros = ler_numeros(
                    "Digite o valor e a porcentagem (ex: 200 15): ", 2)
            else:
                numeros = ler_numeros(
                    "Digite os dois números (ex: 10 5): ", 2)
            try:
                print(f"Resultado: {metodo(*numeros)}")
            except ValueError as erro:
                print(f"Erro: {erro}")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
