"""
Desafio 2: Otimização de Inventário
Objetivo
Criar um sistema de gerenciamento de inventário, usando tabelas hash.
Descrição
Chave da Tabela Hash: Código único do item.
Valores Associados: Quantidade em estoque, localização, informações do fornecedor.
Aplicação: Melhoria da gestão e reposição de estoque."""


class Item:
    def __init__(self, id, quantidade, localizacao, fornecedor):
        self.id = id
        self.quantidade = quantidade
        self.localizacao = localizacao
        self.fornecedor = fornecedor

    def __str__(self):
        return f"Item {self.id}\nQuantidade: {self.quantidade}\nLocalização: {self.localizacao}\nFornecedor: {self.fornecedor}"


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, item):
        key = self.hash(item.id)
        self.tabela[key] = item

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    item = Item(1, 10, "Linha 1", "Fornecedor 1")
    item2 = Item(2, 20, "Linha 2", "Fornecedor 2")
    tabela = TabelaHash(10)
    tabela.inserir(item)
    tabela.inserir(item2)
    result = tabela.buscar(2)
    print(result)
