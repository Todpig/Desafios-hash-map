"""Desafio 8: Análise de Tendências de Mercado
Objetivo
Criar um sistema para analisar tendências de mercado com tabelas hash.
Descrição
Chave da Tabela Hash: Identificador do produto ou categoria.
Valores Associados: Dados de vendas, demanda, avaliações de clientes.
Aplicação: Compreensão das tendências de mercado e ajuste de estratégias de produção."""


class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Categoria {self.id} - {self.nome}"


class Produto:
    def __init__(self, id, dados, categoria: Categoria):
        self.id = id
        self.dados = dados
        self.categoria = categoria

    def __str__(self):
        return f"Produto {self.id}\nDados: {self.dados}\nCategoria: {self.categoria}"


class Dados:
    def __init__(self, id, vendas, demanda, avaliacoes):
        self.id = id
        self.vendas = vendas
        self.demanda = demanda
        self.avaliacoes = avaliacoes

    def __str__(self):
        return f"Vendas: {self.vendas}\nDemanda: {self.demanda}\nAvaliações: {self.avaliacoes}"


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, dados):
        key = self.hash(dados.id)
        self.tabela[key] = dados

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    categoria = Categoria(1, "Perfumes")
    dados = Dados(1, 100, 10, 5)
    produto = Produto(1, dados, categoria)
    tabela = TabelaHash(10)
    tabela.inserir(produto)
    result = tabela.buscar(1)
    print(result)
