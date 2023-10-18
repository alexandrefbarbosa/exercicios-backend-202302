import Veiculo
class Onibus(Veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque, capacidade_passageiros):
        super().__init__(marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque)
        self.capacidade_passageiros = capacidade_passageiros

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Capacidade de Passageiros: {self.capacidade_passageiros}")

    def testar(self):
        print("Testando o ônibus...")
        self.ligar()
        self.acelerar()
        self.frear()
        self.abastecer(100)
        self.exibir_informacoes()
        self.desligar()

""" Aqui comeca o teste """
onibus = Onibus("Mercedes-Benz", "Citaro", 2020, 300000, "Branco", "Diesel", 10000, 300, 50)
print("\nTeste do Ônibus:")
onibus.testar()