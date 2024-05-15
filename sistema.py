menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """
Saldo = 0
Saque = 500
Extrato = ""
numeros_de_saque = 0
limite_de_saque = 3

while True:
    opc = int(input(menu))

    if opc == 1:
      valor = float(input('Deposite sua dinheiro:R$'))

      if valor > 0:
        Saldo += valor
        Extrato += f"Depósito: R$ {valor:.2f}\n"

      else:
        print("Operação falhou! O valor informado é inválido.")


    if opc == 2:
        valor =  float(input("Infome o valor de saque:R$"))

        if valor > Saldo:
            print('Você não possui saldo sufuciente')

        if valor > 500:
            print('Impossível realizar o saque,limite de R$ 500 reais ultrapassado')

        elif  numeros_de_saque >= limite_de_saque:
         print('Número máximo de saques excedido.')
        if valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_de_saque += 1
        else:
            print("Operação falhou! O valor informado é inválido.")


    if opc == 3:

        print("============EXTRATO============  ")
        print(" Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nSaldo: R${Saldo:.2f}")
        print("=============================== ")

    if opc == 4:
        break

