from collections import OrderedDict
from time import localtime, asctime



#----VARIAVEIS COMUNS----



entrada_campo_listuple = [('d', 'Depositar'),
('s', 'Sacar'),
('e', 'Extrato'),
('q', 'Sair')] #aka entrada_campo ou entry_field ou input_field

entry_field = entrada_campo_listuple



#----CLASSES PARA INSTANCIAR----



class Menu:
    def __init__(self, name):
        self.name = name
        self.make_menu()

    @staticmethod
    #--also void, but i cant get it right,
    #--this is not ironically my first time decorating a function
    def make_menu():
        ECL = entrada_campo_listuple.copy()

        entrada_campo = {'d': 'Depositar',
                         's': 'Sacar',
                         'e': 'Extrato',
                         'q': 'Sair'}
         
        menu = ("\n"
                .join(f"[{elem[0]}]: {elem[1]}" for elem in ECL) 
                + ("\n\n=> ")
                ) #see note 02
        #print(menu)
        return menu




class User:

    def __init__(self, username):
        self.username = username
        self.saldo = 0 #see note 01 
        self.historico = [] #(valor_operacao, operacao, saldo)
        #see note 03
        self.numero_de_saques = 3
        self.limite_do_saque = 500



    def extrato(self):
        #print("É um extrato.")

        if len(self.historico) < 1:
            print("Não foram realizadas movimentações.")
            return None

        return self.historico


    def deposito(self):
        #print("É um deposito.")

        v_deposito = input("Deseja depositar quanto?\n\n=> ")

        try:
            v_operacao = float(v_deposito)
        except:
            raise Exception("Erro. Digite um número no formato XXXX.XX, outros formatos ainda não são aceitos.")
        
        if v_operacao < 0:
            raise Exception("Erro. Digite um número no formato XXXX.XX maior que zero.")



        self.saldo += v_operacao    #função para mexer no saldo
        print("Operação bem sucedida.")

        operacao = (v_operacao, "deposito", self.saldo)
        self.historico.append(operacao)

        return operacao       #parcial, é o item do extrato




    def saque(self):
        print("É um saque.")
        
        if self.numero_de_saques < 1:
            raise Exception("Máximo de operações de saque por dia atingido.")
        print(f"Operações de saque restantes: {self.numero_de_saques}")

        def ler_saques_do_historico():
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
        self.numero_de_saques -= 1
        print("Operação bem sucedida.")
        
        operacao = (v_operacao, "saque", self.saldo)
        self.historico.append(operacao)

        return operacao       #parcial, é o item do extrato






    @staticmethod
    def sair():
        flag_mostrar_historico = False
        flag_fazer_resumo = False

        msg_despedida = "O Banco agradece a preferência. Até a próxima!"
        
        print(msg_despedida)
        quit()
        
