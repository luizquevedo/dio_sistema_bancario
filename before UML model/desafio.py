import dio_banco_v2 as Dio
import dio_conta_v1 as Conta
from time import sleep



#----SETTING VARIABLES----

version = "v2"
flag_prerun_check = False

entrada_campo_backup = {'d': 'Depositar', 's': 'Sacar', 'e': 'Extrato', 'q': 'Sair'}
menu_backup = f"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

 """



entrada_campo = dict(Dio.entry_field)
Usuario = Dio.Operations(username="Teste da Silva")
menu = Dio.Menu.make_menu()
if not menu:
    menu = menu_backup



#----PRERUN CHECKS----



conjunto_funcoes_externas = set(
            [elem for elem in dir(Dio.Operations) if not elem.startswith("__")]
            )

if flag_prerun_check and conjunto_funcoes_externas != {
        'extrato', 'deposito', 'precheck_operations_limit', 'sair', 'saque', 'make_timestamp'
        }:

    temp = input(f"AVISO!\n\nFuncionalidade nova detectada. Por favor, verifique:...\n{
          conjunto_funcoes_externas
          }\n\nContinuar programa? [Enter para continuar / qualquer texto para abortar]\n>>> ")
    if not len(temp) < 1:
        quit()




#----INITIALIZING FUNCTIONS----

def sysout_conta_info(target) -> str:
    return target.__repr__()

def interface():
    sleep(0.4)
    print("----INTERFACE----")
    print(sysout_conta_info(conta))


    while True:
        print("Pressione uma das opções (ou Enter para sair).")
        sleep(0.7)
        entrada = input(menu)
        
    
        #--Enter to quit
        if len(entrada) < 1:
            Usuario.sair()
            quit()  ##--HEADS UP! Please keep this here in case the other function changes. Notice 'break' is commented out.
            #break
            
        saida = str(entrada).lower()


        #--Handling weird option
        if saida not in entrada_campo.keys():
            print("Opção inválida. Tente novamente.") 
            sleep(0.7)
            continue
        
        print("Você selecionou:", entrada_campo[saida])
        sleep(0.4)

        return saida


def get_function(opcao=None):   #see note 04
    sleep(0.4)
    try:
        match opcao:

            case "d":
                return Usuario.deposito()
            
            case "s":
                return Usuario.saque()
            
            case "e":
                extrato_string = ""
                #return Usuario.extrato()
                return formatar_extrato()

            case "q":
                return Usuario.sair()
            
            case _:
                print("Funcionalidade não implementada. Favor reportar.")

    except Exception as err:
        print("----AVISO!----\nErro:", err, "\n") 


            
def formatar_extrato():
    formatado = ""
    
    #--Handling missing filehandle
    if Usuario.extrato() is None:
        return None

    for registro in Usuario.extrato():
        # timestamp, tab, value
        formatado += f"{registro[0]}\tR$ {registro[1]:.2f}\n"
    
    formatado += f"Saldo: \tR$ {Usuario.saldo:.2f}"
    return formatado




#----RUNNING----

# Run 'Account' once
conta = Conta.Account()
conta.write_conta_info()


while True:     #quit() instead of break
    opcao = interface()
    
    result = get_function(opcao) 

    print(result if result is not None else "")
    #see note 06

    sleep(0.7)


