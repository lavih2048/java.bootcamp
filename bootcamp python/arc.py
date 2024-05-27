idade = 21
nome = "Lavinia"

texto = f"Oi {nome}, voce tem {idade} anos de idade."  #f antes das aspas necessário para concatenar itens

print(texto)

#//

preco1 = 10
total = preco1/2                                       # divisão comum
total1 = preco1//2                                     # divisão também, porém mostra o número inteiro, sem decimal

print(f"{total} \n {total1}")                          # \n serve para continuar na linha debaixo


# contas aritméticas

produto1 = 20
produto2 = 10

print(produto1 + produto2)              # soma
print(produto1 - produto2)              # subtração
print(produto1 / produto2)              # divisão decimal
print(produto1 // produto2)             # divisão inteira
print(produto1 * produto2)              # multiplicação
print(produto1 % produto2)              # porcentagem
print(produto1 ** produto2)             # potenciação

# operador de comparação é: ==
# operador de igualdade é: =

# operador E

saldo = 1000
saque = 200
limite = 100

valor = saldo >= saque and saque <= limite
print(valor)    # false

# operador OU

saldo = 1000
saque = 200
limite = 100

valor = saldo >= saque or saque <= limite
print(valor)     # true


#// 

saldo = 100
limite = 500
                                    #operadores de identidade "is" e "is not"
print(saldo is limite)        # falso, afirma que tem o mesmo espaço
print(saldo is not limite)    # verdadeiro, afirma que não tem o mesmo espaço


# operador IN, serve para verificar se o valor está na lista

frutas = ['limão', 'uva']

print('laranja' in frutas)    # false, não está na lista de frutas        

#estrutura if com identação (python reconhece quando inicia uma função/parâmetro e quando o mesmo finaliza)

def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
        
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
    

def depositar(valor):
    saldo = 500
    saldo += valor
    

sacar(1000)


#exemplo 1

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas ainda não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")
    


# estrutura de repetição com WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
    
    
    
    
#MÉTODOS ÚTEIS DA CLASSE STRING

curso = "pYtHon"

print(curso.upper())      # PYTHON

print(curso.lower())      # python

print(curso.title())      # Python



#ELIMINANDO ESPAÇOS EM BRANCO

curso = "  Python "

print(curso.strip())        # "Python"

print(curso.lstrip())       # "Python "

print(curso.rstrip())       # "  Python"

#JUNÇÕES E CENTRALIZAÇÃO

curso = "Python"

print(curso.center(10, "#"))    # "##Python##"

print(".".join(curso))          # "P.y.t.h.o.n"


# INTERPOLAÇÃO DE VARIÁVEIS, AMBOS OS PRINTS FUNCIONAM DO MESMO JEITO

nome = "Lavínia"
idade = 21
profissao = "Programadora"
linguagem = "Python"

print(f"Olá, me chamo ${nome}, tenho ${idade} anos de idade. Trabalho como ${profissao} com a linguagem ${linguagem}!")

print("Olá, me chamo {nome}, tenho {idade} anos de idade. Trabalho como {profissao} com a linguagem {linguagem}!".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
 
 
 
 
 
#FORMATAR STRINGS COM F-STRING

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")     # "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}")   # "Valor de PI:      3.14"


# FATIAMENTO DE STRINGS

nome = "Lavínia de Souza Freitas"

print(nome[0])
#L
print(nome[:9])
#Lavinia d
print(nome[10:])
#Souza Freitas
print(nome[10:16])
#Souza
print(nome[10:16:2])
#oz
print(nome[:])
#Lavínia de Souza Freitas
print(nome[::-1])
#satierF azuoS ed ainívaL


#STRINGS MÚLTIPLAS

nome = "Lavinia"

mensagem = f'''Olá meu nome é {nome},
    Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos.'''
        
print(mensagem)