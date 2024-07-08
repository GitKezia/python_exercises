print('1.Imprima a frase: Python na Escola de Programação da Alura.')

print('Python na Escola de Programação da Alura\n')

print('2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.')

# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))
# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

print('3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir: \n')

print('A')
print('L')
print('U')
print('R')
print('A\n')
print('A','L','U','R','A\n',sep='\n')

print('4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:')

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

# Exercícios aula 02

print('1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.')
numero  = int(input('Insira um número: '))
if numero % 2 == 0: 
    print('O número é par\n')
else: 
    print('O número é ímpar\n')
    
    
print('2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:')

idade = int(input('Quantos anos você tem? '))
if 0 < idade <= 12: 
    print('Criança')
elif 12 <  idade < 18:
    print('Adolescente')
elif idade >= 18: 
    print('Adulto')
else: 
    print('Valor inválido!\n') 


# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print('3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.')
usuario = 'kezia21'
senha = 'kezia123'

digitando_usuario = input('Digite seu usuario: \n')
digitando_senha = input('Digite sua senha: \n')

if digitando_usuario == usuario and digitando_senha == senha:
    print('Bem-vindo a sua conta')
else: 
    print('Usuário ou senha inválidos. Tente novamente.\n')




print('4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:') 

print('Primeiro Quadrante: os valores de x e y devem ser maiores que zero;')
print('Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;')
print('Terceiro Quadrante: os valores de x e y devem ser menores que zero;')
print('Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;')
print('Caso contrário: o ponto está localizado no eixo ou origem.\n')

x = float(input('Digite a coordenada de x: '))
y = float(input('Digite a coordenada de y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0: 
    print('Segundo Quadrante')
elif x < 0 and y < 0: 
    print('Terceiro Quadrante')
elif x > 0 and y < 0: 
    print('Quarto Quadrante')
else: 
    print('O ponto está localizado no eixo ou origem\n')

print('Número válido')
numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)

# Exercicios Aula 03

print('1 - Crie uma lista para cada informação a seguir:')

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista02 = ['Kezia', 'Rebeca', 'Keila']
lista03 = [2000, 2024]

print('2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.')

lista_comidas_favoritas = ['Salada', 'Strogonoff', 'Fricassê']
for lista in lista_comidas_favoritas:
    print(f'{lista}')

print('3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.')
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
    print(soma_impares)

print('4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.')
for i in range(10, 0, -1):
    print(i)

print('5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.')
numero_tabuada = int(input('Digite um número para a tabuada:'))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = resultado')

print('6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.')

lista_numeros = [24, 5, 8, 19, 89, 22]
soma = 0

try: 
    for numero in lista_numeros:
        soma += numero
        print(f'Soma dos elementos: {soma}')
except Exception as e: 
    print(f'Ocorreu um erro: {e}')

print('7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.')
lista_valores = [35, 1, 7, 33, 40]
soma_valores = 0

try: 
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f'Média dos valores {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# Exercicios Aula 04

print('1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.')

pessoa = [{'nome': 'Aline', 'idade': 26, 'cidade': 'Arkansas'}, 
          {'nome': 'Gustavo', 'idade': 19, 'cidade': 'Goiânia'}]

print('2 - Utilizando o dicionário criado no item 1:')

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.'

pessoa['idade'] = 31

pessoa['profissao'] = 'Programador'

del pessoa['cidade']

print('3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.')

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

print('3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.')
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

print('5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.')

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

