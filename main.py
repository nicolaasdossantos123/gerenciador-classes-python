class GerenciadorNumeros:
    def __init__(self):
        self.numeros = []

    def adicionar_numero(self):
        try:
            numero = int(input("Adicione um número à lista: "))
            self.numeros.append(numero)
            print("Número adicionado!")
        except ValueError:
            print("Digite apenas números.")

    def contar_positivos(self):
        contador = 0
        for numero in self.numeros:
            if numero > 0:
                contador += 1
        print("Positivos:", contador)

    def contar_pares(self):
        contador = 0
        for numero in self.numeros:
            if numero % 2 == 0:
                contador += 1
        print("Pares:", contador)

    def contar_impares(self):
        contador = 0
        for numero in self.numeros:
            if numero % 2 != 0:
                contador += 1
        print("Ímpares:", contador)

    def mostrar_lista(self):
        print(self.numeros)


def menu():
    ger = GerenciadorNumeros()

    while True:
        print("\n1 - Adicionar número")
        print("2 - Contar pares")
        print("3 - Contar ímpares")
        print("4 - Contar positivos")
        print("5 - Mostrar lista")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido")
            continue

        if opcao == 1:
            ger.adicionar_numero()

        elif opcao == 2:
            ger.contar_pares()

        elif opcao == 3:
            ger.contar_impares()

        elif opcao == 4:
            ger.contar_positivos()

        elif opcao == 5:
            ger.mostrar_lista()

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida")


menu()