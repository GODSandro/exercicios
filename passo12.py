"""
# 1) Crie um método que receba um valor em reais e converta a dólares

def conversao(valor):
    conversao = valor / 5.76
    return conversao

valor1 = float(input('Digite o valor em real: '))
result = conversao(valor1)
print('o valor em convertido é $', round(result, 2))
print('*********************')

# • 2) Crie um método que receba 2 parâmetros: um valor em reais e a moeda que deve ser convertida (dólares, euros ou peso argentino). E
# realize a conversão.

def conversao(valor,moeda):
    conversao = valor / moeda
    return conversao

valor1 = float(input('Digite o valor em real: '))
valor2 = float(input('Digite a cotação do dolar: '))
result = conversao(valor1,valor2)
print('o valor em convertido é $', round(result, 2))
print('*********************')


# • 3) Crie um método que receba 3 parâmetros: um valor, moeda de origem e a moeda que deve ser convertida (dolares, euros ou peso
# argentino). E realize a conversão.

def conversao(valor,moeda,converter):
    conversao = valor / moeda
    return conversao

valor1 = float(input('Digite o valor em real: '))
valor2 = float(input('Digite a cotação da moeda: '))

result = conversao(valor1,valor2)
print('o valor em convertido é $', round(result, 2))
print('*********************')

# • 4) Crie um método que receba o peso e altura e retorne o IMC.

def calculoImc (peso,altura):
    imc = peso / altura**2
    return imc

peso1 = float(input('Digite o peso: '))
altura2 = float(input('Digite a altura: '))
resultado = calculoImc(peso1,altura2)
print('Seu IMC é:', round(resultado, 2))
print('*********************')

"""
# • 5) Crie um método que receba as notas e retorne a maior nota do aluno

def notasMaior(nota1,nota2):
    if nota1 > nota2:
        print('A maior nota é :',nota1)
    else:
        print(print('A maior nota é :',nota2))
    return

nota1 = int(input('Digite sua 1ª nota: '))
nota2 = int(input('Digite sua 2ª nota: '))

# • 6) Crie um método que receba as notas e retorne a média de notas do aluno



# • 7) Crie um método que receba o valor em celsius e converta a farenheit


# • 8) Crie um método que receba o valor em farenheite converta a celsius



# • 9) Crie um método que receba o valor do salario e indique a quantidade de imposto a ser pago (se ganhar até 2000, 12%. Acima de 2000,
# 25%)

# • 10) Desafio:
# • Crie uma classe Conta com as variaveisagencia, conta, titular e saldo
# • Crie uma classe chamada Agencia, que tenha uma lista chamada contas
# • A classe Agencia, deve ter um metodochamado adicionarConta, que adiciona uma nova conta à agencia
# • A classe Agencia, deve ter um metodochamado quantidadeContas, que retorna a quantidade de contas da agencia

