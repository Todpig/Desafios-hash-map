"""Desafio 1: Rastreamento de Componentes em Tempo Real
Objetivo
Desenvolver um sistema para rastrear componentes individuais na linha de produção, utilizando tabelas hash.
Descrição
Chave da Tabela Hash: ID único do componente.
Valores Associados: Status atual, localização, histórico de processos.
Aplicação: Monitoramento em tempo real dos componentes na linha de produção."""


class Componente:
    def __init__(self, id, status, localizacao, historico):
        self.id = id
        self.status = status
        self.localizacao = localizacao
        self.historico = historico

    def __str__(self):
        return f"Componente {self.id}\nStatus: {self.status}\nLocalização: {self.localizacao}\nHistórico: {self.historico}"

    def set_status(self, status):
        self.status = status

    def set_localizacao(self, localizacao):
        self.localizacao = localizacao

    def add_historico(self, historico):
        self.historico.append(historico)


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, componente):
        key = self.hash(componente.id)
        self.tabela[key] = componente

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    componente = Componente(1, "Em produção", "Linha 1", [
                            "Processo 1", "Processo 2"])
    tabela = TabelaHash(10)
    tabela.inserir(componente)
    result = tabela.buscar(1)
    print(result)
