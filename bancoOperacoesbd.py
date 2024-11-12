from operacoesbd import *

conn = abrirBancoDados("localhost", "root", "1234", "aluno")

sql = "SELECT * FROM alunos"
resultado = listarBancoDados(conn, sql)

for elemento in resultado:
    print(elemento)

# matricula = int(input('digite a matricula: '))
nome = input('digite o nome: ')
endereço = input('digite o endereço: ')
cidade = input('digite a cidade: ')

sql = "insert into alunos (nome,endereço,cidade) VALUES (%s , %s, %s)"
dados = (nome, endereço, cidade)
insertNoBancoDados(conn, sql, dados)

sql = "SELECT * FROM alunos"
resultado = listarBancoDados(conn, sql)