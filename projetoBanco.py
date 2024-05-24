import sys


#depositar = 500
#sacar = 200
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu ='''
    Digite a opção:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] sair
'''


while True:
    
    opcao = input(menu)
    
    if opcao == 1:
        valor = float(input("Digite o valor do deposito: "))
        if valor >0:
          saldo+=valor
          extrato += f"Deposito de R$ {valor:.2f}\n"
        else:
            print("Valor inválido para deposito")
        
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor >limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação fallhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -=valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
        else:
            print("Operação falohu! o valor informado é invalido")
            
    elif opcao == 3:
        print("\n==============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")  
    elif opcao == 4:
        break
    else:
        print("opção invalida, favor escolher uma opção certa!!!")
