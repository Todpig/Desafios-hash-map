"""Desafio 5: Gerenciamento de Ordens de Produção
Objetivo
Criar um sistema para gerenciar ordens de produção usando tabelas hash.
Descrição
Chave da Tabela Hash: Número da ordem de produção.
Valores Associados: Status da ordem, detalhes do produto, prazos.
Aplicação: Otimização do fluxo de produção e acompanhamento de ordens."""


class Produto:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"Nome: {self.nome} - Descrição: {self.descricao}"


class Ordem:
    def __init__(self, id, status, produto: Produto, prazo):
        self.id = id
        self.status = status
        self.produto = produto
        self.prazo = prazo

    def __str__(self):
        return f"Ordem {self.id}\nStatus: {self.status}\nProduto: {self.produto}\nPrazo: {self.prazo}"


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, ordem):
        key = self.hash(ordem.id)
        self.tabela[key] = ordem

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    produto1 = Produto(1, "Produto 1", "Descrição 1")
    ordem = Ordem(1, "Em produção", produto1, "10 dias")
    tabela = TabelaHash(10)
    tabela.inserir(ordem)
    result = tabela.buscar(1)
    print(result)
