import sys
import time


menu = """
===== Escolha uma opção =====

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    
  => """ 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



def processando(duracao):
    fim_processando = time.time() + duracao
    while time.time() < fim_processando:
        for pontinhos in range(4):
            sys.stdout.write("\r\033[1mProcessando" + "." * pontinhos + "   \033[m")
            sys.stdout.flush()
            time.sleep(0.7)
            
    sys.stdout.write(" ")
    

while True:
     
    opcao = input(menu)
     
    if opcao == "1":
        processando(4)
        valor = float(input("\nPor favor, informe o valor do \033[1;32mDepósito: R$ \033[m"))
        processando(2)
        

        if valor > 0:
            print("\n\033[1;32mSucesso!\033[m")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("\n\033[1mA operação falhou! O valor informado é\033[m \033[1;31mINVALIDO!\033[m")
            

    elif opcao == "2":
        processando(4)
        valor = float(input("\nPor favor, informe o valor do \033[1;32mSaque: R$ \033[m"))
        processando(2)
        
        execeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite
        
        exedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if execeu_saldo:
            print("\n\033[1mA operação falhou!\033[m Você não tem \033[1;31mSALDO\033[m suficiente.")
            
        elif exedeu_limite:
            print("\n\033[1mA operação falhou!\033[m O valor do saque \033[1;31mEXEDE\033[m o seu limite atual.")
        
        elif exedeu_saques:
            print("\n\033[1mA operação falhou!\033[m O número de saques diarios já foi \033[1;31mEXEDIDO.\033[m")
            
        elif valor > 0:
            print("\n\033[1;32mSucesso!\033[m")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("\n\033[1mA operação falhou! O valor informado é\033[m \033[1;31mINVÁLIDO!\033[m")
            
    elif opcao == "3":
        processando(4)
        print("\n=================== \033[1mEXTRATO\033[m ===================")        
        print("Não foram realizadas movimentaçoes." if not extrato else extrato)        
        print(f"\nSaldo: R$ {saldo:.2f}")        
        print("=================================================")        
     
    elif opcao == "0":
        processando(2)
        print("\n\033[1mAgradecemos por escolher nossos serviços. Volte sempre!\033[m")
        break
    
    else:
        print("\033[1;31mOperação INVÁLIDA!\033[m \033[1mPor favor selecione novamente uma alternativa valida.\033[m") 