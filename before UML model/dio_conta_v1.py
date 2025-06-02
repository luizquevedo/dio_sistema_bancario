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
        self.agencia = '0001'   #see note 09
        self.conta_num = None   #flag
        self.CPF = None         #LGPD
        pass


    '''conta_num
    cpf
    datanasc
    nome
    endereco
    '''
    
    def __repr__(self):
        #return f"\n{[f'{k}: {v}' for k,v in self.__dict__.items()]}\n"
        return f"\nAG: {self.agencia}\nC/C: {self.conta_num}\n"


    @staticmethod
    def prompt_cpf():
        cpf = input('CPF, por favor.'+"\n\n>>> ")
        return cpf

    def get_conta_info(self) -> tuple:
        cpf = self.prompt_cpf()
    
        if not os.path.exists(filepath):
            print('hey!')
            self.conta_num = 1
            print(self.conta_num)
        else:

            with open(filepath, 'r') as file:  # read

                for elem in file.readlines():

                    conta = elem.strip('\n').split(', ')
                    conta_corrente_da_vez = int(conta[-2])

                    # f. In case it's NOT, get:
                    #--max account number--
                    if self.conta_num is None:
                        self.conta_num = conta_corrente_da_vez
                    if conta_corrente_da_vez > self.conta_num:
                        self.conta_num = conta_corrente_da_vez

                    # t. In case it's registered
                    if cpf == conta[-1]:
                        break
                
                # f. set to max account number + 1 
                else:   # for/else
                    #TODO: flag de novo Usuario ou novo cliente, etc.
                    #TODO: Procedimento registrar novo Usuario, endereco, etc.
                    self.conta_num += 1
        


        return (self.agencia, 
                str(self.conta_num), 
                cpf)  # Primary Key: cpf



    def write_conta_info(self) -> None:
        conta_cached = self.get_conta_info()

        with open(filepath, 
                ('a' if os.path.exists(filepath) else 'w')
                ) as file:  # append

            file.write(", ".join(conta_cached) +'\n')
            

            print("Dados recebidos com sucesso.")




#---END OF CLASSES PARA INSTANCIAR---


#temp = Account()
#temp.write_conta_info()



#---I use Vim, btw.---
