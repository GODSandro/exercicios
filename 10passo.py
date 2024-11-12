"""Isabela Vitoriano foi contratada para desenvolver um sistema para gestão da Universidade ABC. Abaixo temos uma relação de 3 tabelas que são
necessárias para o sistema.
• Alunos (MAT, nome, endereço, cidade)
    • Disciplinas (COD_DISC, nome_disc, carga_hor)
• Professores (COD_PROF, nome, endereco, cidade)
Consultas a serem criadas:
• Crie cada uma das 3 tabelas (o sublinhado significa chave primária)
• Faça ao menos 3 inserções em cada uma das tabelas
• Listar todos os alunos
• Listar todas as disciplinas
• Listar todos os professores
• Listar todos os alunos que residem em Campina Grande
• Listar todos os alunos que possuem algum sobrenome Abella
• Listar os dados do aluno que possui matrícula 1
• Listar o nome do aluno que possui matrícula 1
• Listar as disciplinas que possuem carga horária maior ou igual a 60
• Listar as disciplinas que possuem no seu nome a palavra PYTHON
• Listar todos os professores que residem em Campina Grande
• Excluir o aluno que possui matrícula 2
• Excluir os alunos que possuem algum sobrenome Abella
• Alterar a carga horária das disciplinas com 60 horas para 80 horas

/*
create table alunos(

	matricula int auto_increment,
	nome varchar(30),
	endereço varchar(100),
	cidade varchar(20),
	primary key (matricula)

)

/*
insert into disciplinas
(codigoDisciplina, nome_disc, cargaHoraria) 
values (1, "sistemas", 80); 

insert into disciplinas
(codigoDisciplina, nome_disc, cargaHoraria) 
values (2, "informação", 160); 

insert into disciplinas
(codigoDisciplina, nome_disc, cargaHoraria) 
values (3, "merdicina", 20); 


insert into professores
(COD_PROF, nome, endereco, cidade) 
values (100, "fabricio", "ruda da avenue", "texas"); 

insert into professores
(COD_PROF, nome, endereco, cidade) 
values (10, "samara", "ruda do fogo", "barbacena"); 

insert into professores
(COD_PROF, nome, endereco, cidade) 
values (1000, "abella", "ruda da facisa", "new york"); 


select * from alunos
select * from dsiciplinas
select * from professores


select * from professores where cidade = 'campina grande';

select * from  alunos where cidade = 'Campina Grande'

select * from alunos where nome like '%abella%';	

select * from alunos where matricula = 1;

select nome from alunos where matricula = 1;

select * from dsiciplinas where carga_horaria >= 60;

select * from disciplinas where nome like '%python%';

delete from alunos
*/
"""
calculoImc(imc)