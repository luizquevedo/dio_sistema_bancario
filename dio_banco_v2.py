#----dio_banco_v2.py----
#see note 07


from collections import OrderedDict
from datetime import datetime   #see note 08



#----VARIAVEIS COMUNS----



entry_field = [('d', 'Depositar'),
('s', 'Sacar'),
('e', 'Extrato'),
('q', 'Sair')]



#----FUNCOES COMUNS----

@staticmethod
def make_timestamp():
    return datetime.strftime(datetime.now(), "%c")

def precheck_operations_limit(self):
    if self.numero_de_operacoes < 1:
        raise Exception("Máximo de operações do dia atingido.")
    print(f"Operações restantes: {self.numero_de_operacoes}")

def precheck_withdrawals_limit(self):
    if self.numero_de_saques < 1:
        raise Exception("Máximo de operações de saque por dia atingido.")
    print(f"Operações de saque restantes: {self.numero_de_saques}")



#----CLASSES PARA INSTANCIAR----



class Menu:
    def __init__(self, name):
        self.name = name
        self.make_menu()

    @staticmethod
    #--also void, but i cant get it right, this is not ironically my first time decorating a function
    def make_menu():
        ECL = entry_field.copy()

        menu = ("\n"
                .join(f"[{elem[0]}]: {elem[1]}" for elem in ECL) 
                + ("\n\n=> ")
                ) #see note 02
        return menu




class User:

    def __init__(self, username):
        self.username = username
        self.historico = self.get_historico() #(timestamp, valor_operacao, operacao, saldo)
        self.saldo = 0  #see note 01

        self.numero_de_saques = 3
        self.numero_de_operacoes = 10
        self.limite_do_saque = 500
    


    def get_historico(self):
        #see note 03    
        return []



    #----DIO.USER FUNCTIONS----

    def extrato(self):

        if len(self.historico) < 1:
            print("Não foram realizadas movimentações.")
            return None

        return self.historico




    def deposito(self):
        precheck_operations_limit(self)



        v_deposito = input("Deseja depositar quanto?\n\n=> ")
        try:
            v_operacao = float(v_deposito)
        except:
            raise Exception("Erro. Digite um número no formato XXXX.XX, outros formatos ainda não são aceitos.")
        


        if v_operacao < 0:
            raise Exception("Erro. Digite um número no formato XXXX.XX maior que zero.")



        self.saldo += v_operacao    #função para mexer no saldo
        self.numero_de_operacoes -= 1
        print("Operação bem sucedida.")

        operacao = (make_timestamp(), v_operacao, "deposito", self.saldo)
        self.historico.append(operacao)

        return operacao       #parcial, é o item do extrato




    def saque(self):
        precheck_operations_limit(self) 
        precheck_withdrawals_limit(self)



        def update_saques():
            #--Iterando self.numero_de_saques com base nos valores numéricos de self.historico
            if len(self.historico) < self.numero_de_saques:
                ##--Heads up! Possivel erro Off-By-One. Verificar. Alternativamente, menor que 1.
                return None
            for registro in self.historico:
                if registro[0] < 0:  #valor negativo
                    self.numero_de_saques -= 1
                if self.numero_de_saques < 1: 
                    raise Exception("Máximo de operações de saque por dia atingido.") 
                    break
            return self.numero_de_saques



        v_saque = input("Deseja sacar quanto?\n\n=> ")
        try:
            v_operacao = float(v_saque)
            v_operacao *= -1
        except:
            raise Exception("Erro. Digite um número no formato XXXX.XX maior que zero.")
        
        if v_operacao > 0:    #valor negativo
            raise Exception("Erro. Digite um número no formato XXXX.XX maior que zero.")
        if v_operacao < -self.limite_do_saque: #valor negativo
            raise Exception(f"Valor do saque muito alto. Seu limite de valor do saque atual é de R${self.limite_do_saque}. Caso necessário, faça mais de uma operação, lembrando do número de saques diários.")        
        if (self.saldo + v_operacao) < 0:
            raise Exception("Erro. Saldo insuficiente. Abortando operação.")




        self.saldo += v_operacao    #função para mexer no saldo
        self.numero_de_operacoes -= 1
        self.numero_de_saques -= 1
        print("Operação bem sucedida.")
        
        operacao = (make_timestamp(), v_operacao, "saque", self.saldo)
        self.historico.append(operacao)

        return operacao       #parcial, é o item do extrato






    @staticmethod
    def sair():
        flag_mostrar_historico = False
        flag_fazer_resumo = False

        msg_despedida = "O Banco agradece a preferência. Até a próxima!"
        
        print(msg_despedida)
        quit()
        
