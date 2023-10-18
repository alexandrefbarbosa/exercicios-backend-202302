import Veiculo
class Carro(Veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque, num_portas):
        super().__init__(marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque)
        self.num_portas = num_portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Número de Portas: {self.num_portas}")

    def testar(self):
        print("Testando o carro...")
        self.ligar()
        self.acelerar()
        self.frear()
        self.abastecer(20)
        self.exibir_informacoes()
        self.desligar()

""" Aqui comeca o teste """

carro = Carro("Toyota", "Corolla", 2022, 80000, "Prata", "Gasolina", 20000, 50, 4)
print("\nTeste do Carro:")
carro.testar()