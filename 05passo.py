'''
#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("Olá mundo!!")

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = int(input("Digite um numero: "))
print("O número informado foi:",numero)

#Faça um Programa que peça dois números e imprima a soma.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

soma = numero1 + numero2
print("A soma é:",soma)


# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a primeira media: "))
nota2 = float(input("Digite a segunda media: "))
nota3 = float(input("Digite a terceira media: "))
nota4 = float(input("Digite a quarta media: "))

media = (nota1+nota2+nota3+nota4) / 4

print(media)

#• Faça um Programa que converta metros para centímetros.

metro = int(input("Digite um numero: "))

centimetro = metro * 100
print(centimetro)

#• Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite um numero: "))

#A=π×r2
pi = 3.14
raio = raio**2

area = pi * raio
print(area)

#• Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = float(input("Digite um numero: "))
area = quadrado**2

print(area*2)

#• Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#• Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Digite quanto você ganha por hora: "))
horasMes = float(input("Digite quantas horas você trabalhou no mês: "))

remuneração = salarioHora *horasMes
print("Seu salario no mês foi: ","R$",remuneração)

• Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
• C = 5 * ((F-32) / 9).

Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
conversao = 5 * ((Fahrenheit-32) / 9)
print("A temperatura em Cº é: ",conversao)


# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F=( C × 5/9 )+32

Celsius = float(input("Digite a temperatura em Celsius: "))
conversaoFahrenheit = (Celsius * 1.8) + 32
print("A temperatura em Fº é: ", conversaoFahrenheit)

• Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
• o produto do dobro do primeiro com metade do segundo .
• a soma do triplo do primeiro com o terceiro.
• o terceiro elevado ao cubo.

numero3 = int(input("Digite o 1º numero: "))
numero4 = int(input("Digite o 2º numero: "))
numero5 = int(input("Digite o 3º numero: "))

produtoDobro = (numero3 * 2) * (numero4 / 2)
somaTriplo = (numero3 * 3) + numero4
terceiroCubo = numero5 ** 3

print("o produto do dobro do primeiro com metade do segundo é: ",produtoDobro)
print("a soma do triplo do primeiro com o terceiro. é: ",somaTriplo)
print("o terceiro elevado ao cubo é: ",terceiroCubo)


• Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
(72.7*altura) –58

altura = float(input("digite sua altura: "))
pesoIdeal = (72.7 * altura)-58

print("seu peso ideal é: ",pesoIdeal)


Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
homens: (72.7*h) –58
mulheres: (62.1*h) -44.7


altura = float(input("digite sua altura: "))
sexo = int(input("Digite 1 para Homem e 2 para Mulher "))

if sexo == 1:
    homem =  (72.7 * altura) - 58
    print("seu peso ideal é: ", homem)
elif sexo == 2:
    mulher = (62.1 * altura) - 44.7
    print("seu peso ideal é: ", mulher)
else:
    print("Opção inválida!!")

• João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que
ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os
dados do programa com as mensagens adequadas.


pesoPeixes = float(input("Digite o peso: "))

excesso = pesoPeixes - 50
print(excesso)
multa = excesso * 4
print(multa)

print("O total a pagar é: ",multa)

• Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
programa que nos dê:
• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.
• calcule os descontos e o salário líquido, conforme a tabela à direita.
'''
