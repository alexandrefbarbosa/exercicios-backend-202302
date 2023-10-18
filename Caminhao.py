import Veiculo

class Caminhao(Veiculo.Veiculo):
    def __init__(self, marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque, capacidade_carga):
        super().__init__(marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque)
        self.capacidade_carga = capacidade_carga

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Capacidade de Carga: {self.capacidade_carga} toneladas")

    def testar(self):
        print("Testando o caminhão...")
        self.ligar()
        self.acelerar()
        self.frear()
        self.abastecer(50)
        self.exibir_informacoes()
        self.desligar()

""" Aqui comeca o teste """

caminhao = Caminhao("Volvo", "FH16", 2021, 180000, "Azul", "Diesel", 50000, 500, 25)
print("\nTeste do Caminhão:")
caminhao.testar()
