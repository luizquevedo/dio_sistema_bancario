#---dio_conta_v1.py---

import os

#see note 13
#see note 14: Naming Convention
#see note 15: "Sidequest"



#---VARIÁVEIS COMUNS---

# Vou tentar não pegar uma DB ainda.
filepath = "armazenamento_contas.csv"   # agencia, conta, cpf

#print("---DEBUG MODE---")
#input("\n[Qualquer tecla para continuar]")    #breakpoint
pass    # Heads up! There is more execution at the end!



#---CLASSES PARA INSTANCIAR---



class Account:
    def __init__(self):
        self.agencia = '0001' #see note 09
        pass


    '''conta_num
    cpf
    datanasc
    nome
    endereco
    '''



    @staticmethod
    def prompt_cpf():
        cpf = input('CPF, por favor.'+"\n\n>>> ")
        return cpf

    def get_conta_info(self) -> tuple:
        cpf = self.prompt_cpf()

        # In case it's already registered
        pass
        
        # In case it's NOT registered
        # -get next account number
        with open(filepath, 
                ('r' if os.path.exists(filepath) else 'w')
                ) as file:  # read 
            conta_num = 1 + len(file.readlines())   # 1-based, autoincrement 
        
        return (self.agencia, 
                str(conta_num), 
                cpf)  # Primary Key: cpf



    def write_conta_info(self) -> None:
        with open(filepath, 
                ('a' if os.path.exists(filepath) else 'w')
                ) as file:  # append

            file.write(", ".join(self.get_conta_info()) +"\n")
            print("Dados recebidos com sucesso.")




#---END OF CLASSES PARA INSTANCIAR---


#temp = Account()
#temp.write_conta_info()


