"""Desafio 6: Monitoramento de Qualidade de Produtos
Objetivo
Implementar um sistema para monitorar a qualidade dos produtos usando tabelas hash.
Descrição
Chave da Tabela Hash: ID do produto.
Valores Associados: Dados de controle de qualidade, feedbacks.
Aplicação: Assegurar a qualidade e rastrear problemas de fabricação."""


class Feedback:
    def __init__(self, id, nota, comentario):
        self.id = id
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"Feedback {self.id} - Nota: {self.nota} - Comentário: {self.comentario}"


class Produto:
    def __init__(self, id, dados):
        self.id = id
        self.dados = dados
        self.feedbacks = []

    def __str__(self):
        feedback_str = "\n".join(map(str, self.feedbacks))
        return f"Produto {self.id}\nDados: {self.dados}\nFeedbacks: {feedback_str}"

    def add_feedback(self, feedback: Feedback):
        self.feedbacks.append(feedback)


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, produto):
        key = self.hash(produto.id)
        self.tabela[key] = produto

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    produto = Produto(1, "Dados do produto")
    feedback = Feedback(1, 5, "Comentário 1")
    feedback2 = Feedback(2, 3, "Comentário 2")
    produto.add_feedback(feedback)
    produto.add_feedback(feedback2)
    tabela = TabelaHash(10)
    tabela.inserir(produto)
    result = tabela.buscar(1)
    print(result)
