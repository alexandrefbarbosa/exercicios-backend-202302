class Veiculo:
    def __init__(self, marca, modelo, ano, preco, cor, motor, quilometragem, capacidade_tanque):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.cor = cor
        self.motor = motor
        self.quilometragem = quilometragem
        self.capacidade_tanque = capacidade_tanque

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Cor: {self.cor}")
        print(f"Motor: {self.motor}")
        print(f"Quilometragem: {self.quilometragem} km")
        print(f"Capacidade do Tanque: {self.capacidade_tanque} litros")

    def ligar(self):
        print("O veículo está ligado.")

    def desligar(self):
        print("O veículo está desligado.")

    def acelerar(self):
        print("O veículo está acelerando.")

    def frear(self):
        print("O veículo está freando.")

    def abastecer(self, litros):
        print(f"Abastecendo o veículo com {litros} litros de combustível.")