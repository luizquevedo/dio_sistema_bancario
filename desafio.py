import dio_banco_v1 as Dio
from time import sleep

#----SETTING VARIABLES----

version = "v1"

current_version_functions = ['Menu', 'OrderedDict', 'User', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'asctime', 'entrada_campo_listuple', 'entry_field', 'localtime']



entrada_campo = {'d': 'Depositar', 's': 'Sacar', 'e': 'Extrato', 'q': 'Sair'}

menu = f"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

menu = Dio.Menu.make_menu()
entrada_campo = dict(Dio.entry_field)
Usuario = Dio.User(username="Teste da Silva")


#----PRERUN CHECKS----



if list(dir(Dio)) != current_version_functions:
    print("Seu sistema está desatualizado. \nAbortando operação")
    quit()

conjunto_funcoes_externas = set(
            [elem for elem in dir(Dio.User) if not elem.startswith("__")]
            )

if conjunto_funcoes_externas == {'sair', 'saque', 'deposito', 'extrato'}:
    flag_funcoes_esperadas = True
else:
    print("Funcionalidade estranha detectada. Por favor, verifique.")
    quit()




#----INITIALIZING FUNCTIONS----



def debug_by_print():
    print("----DEBUG")
    print(entrada_campo)
    print(menu)


def interface():
    sleep(0.4)
    print("----INTERFACE")

    while True:
        print("Pressione uma das opções (ou Enter para sair).")
        sleep(0.7)
        entrada = input(menu)
        
    
        #--Enter para sair
        if len(entrada) < 1:
            #break
            quit()
            
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
        print(err, "\n") 


            
def formatar_extrato():
    formatado = ""
    
    if Usuario.extrato() is None:
        return None

    for registro in Usuario.extrato():
        formatado += f"R$ {registro[0]:.2f}"
        formatado += "\n"
    
    formatado += f"R$ {Usuario.saldo:.2f}"
    return formatado




#----RUNNING----



#debug_by_print()


while True:     #quit() instead of break
    opcao = interface()
    
    result = get_function(opcao) 

    print(result if result is not None else "")
    #see note 06

    sleep(0.7)


