# Par ou ímpar

numero = int(input("Digite um numero inteiro: "))
if numero % 2 == 0:
    print("O numero é par!")
else:
    print("O numero é impar")

# Aprovação

nota = float(input("Digite a nota do aluno:"))
if nota >= 7:
    print("Aluno aprovado!")
elif nota >= 5:
    print("Aluno de recuperação")
else:
    print("Aluno reprovado")

# Maior, menor ou igual

numero1 = float(input("Digite um numero:"))
numero2 = float(input("Digite outro numero:"))
if numero1 > numero2:
    print(numero1, "é maior que", numero2)
elif numero2 > numero1:
    print(numero2, "é maior que", numero1)
else:
    print("Os numeros sao iguais")

# Banco

conta = 999
senha = 456
saldo = float(1289)
contaUsuario = int(input("Digite o numero da sua conta: "))
senhaUsuario = int(input("Digite o senha da sua conta: "))
if contaUsuario == conta and senhaUsuario == senha:
    print("Usuario logado!")
    valorSaque = float(input("Digite o valor do saque: "))
    if saldo >= valorSaque:
        saldo = saldo - valorSaque
        print(f"Seu saldo agora é R$ {saldo}!")
    else:
        print("Saldo insuficiente!")
else:
    print("Usuario ou senha incorretos!")

