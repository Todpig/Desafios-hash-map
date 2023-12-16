"""Desafio 3: Análise de Dados de Sensores
Objetivo
Implementar um sistema para analisar dados de sensores em tempo real, com tabelas hash.
Descrição
Chave da Tabela Hash: ID único do sensor.

Valores Associados: Leituras recentes do sensor.
Aplicação: Análise para manutenção preditiva e otimização de processos."""


class Sensor:
    def __init__(self, id, leituras):
        self.id = id
        self.leituras = leituras

    def __str__(self):
        return f"Sensor {self.id}\nLeituras {self.leituras}"

    def add_leitura(self, leitura):
        self.leituras.append(leitura)


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, sensor):
        key = self.hash(sensor.id)
        self.tabela[key] = sensor

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    sensor = Sensor(1, [10, 20, 30])
    tabela = TabelaHash(10)
    tabela.inserir(sensor)
    result = tabela.buscar(1)
    print(result)
