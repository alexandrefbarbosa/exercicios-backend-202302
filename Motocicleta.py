
import Veiculo
class Motocicleta(Veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque, cilindradas):
        super().__init__(marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque)
        self.cilindradas = cilindradas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Cilindradas: {self.cilindradas}")

    def testar(self):
        print("Testando a motocicleta...")
        self.ligar()
        self.acelerar()
        self.frear()
        self.abastecer(10)
        self.exibir_informacoes()
        self.desligar()

""" Aqui comeca o teste """
motocicleta = Motocicleta("Honda", "CBR600RR", 2023, 12000, "Vermelha", "Gasolina", 5000, 20, 600)
print("\nTeste da Motocicleta:")
motocicleta.testar()