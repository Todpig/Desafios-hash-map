"""Desafio 4: Controle de Acesso e Autenticação
Objetivo
Desenvolver um sistema de controle de acesso usando tabelas hash.
Descrição
Chave da Tabela Hash: ID de usuário.
Valores Associados: Credenciais e níveis de acesso.
Aplicação: Segurança e eficiência na autenticação de usuários."""


class Credenciais:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Email: {self.email} <-> Senha: {self.senha}"


class Usuario:
    def __init__(self, id, credenciais: Credenciais, nivel):
        self.id = id
        self.credenciais = credenciais
        self.nivel = nivel

    def __str__(self):
        return f"Usuário {self.id}\nCredenciais: {self.credenciais}\nNível: {self.nivel}"


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, id):
        return id % self.tamanho

    def inserir(self, usuario):
        key = self.hash(usuario.id)
        self.tabela[key] = usuario

    def remover(self, id):
        key = self.hash(id)
        self.tabela[key] = None

    def buscar(self, id):
        key = self.hash(id)
        return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


if __name__ == "__main__":
    credenciais = Credenciais("vala@cuida.vom", "123456")
    usuario = Usuario(1, credenciais, "admin")
    tabela = TabelaHash(10)
    tabela.inserir(usuario)
    result = tabela.buscar(1)
    print(result)
