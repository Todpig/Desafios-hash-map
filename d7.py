"""Desafio 7: Logística e Rastreamento de Remessas
Objetivo
Desenvolver um sistema para rastrear remessas usando tabelas hash.
Descrição
Chave da Tabela Hash: Número de rastreamento da remessa.
Valores Associados: Localização atual, status da entrega, detalhes do destinatário.
Aplicação: Eficiência no rastreamento e entrega de remessas."""


class Destinatario:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"Destinatário: {self.nome}\nEndereço: {self.endereco}"


class Remessa:
    def __init__(self, id, destinatario: Destinatario, localizacao, status):
        self.id = id
        self.destinatario = destinatario
        self.localizacao = localizacao
        self.status = status

    def __str__(self):
        return f"Remessa {self.id}\n{self.destinatario}\nLocalização: {self.localizacao}\nStatus: {self.status}"


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, remessa):
        key = self.hash(remessa.id)
        self.tabela[key] = remessa

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    destinatario = Destinatario("João", "Rua A, 123")
    remessa = Remessa(1, destinatario, "Localização 1", "Status 1")
    tabela = TabelaHash(10)
    tabela.inserir(remessa)
    result = tabela.buscar(1)
    print(result)
