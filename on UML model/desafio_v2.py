# ---desafio_v2.py---
# see note 01



from abc import ABC, abstractmethod

class Transacao(ABC): 
    @abstractmethod
    def registrar(self):
        pass

# TODO: Tudo precisa de uma conta para existir. Faz uma aí, mano.

#------

class Deposito(Transacao):
    # PREMISSA: Valores de depósito são sempre positivos.
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        # from github repo, pruned
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.adicionar_transacao(self)


class Saque():
    # PREMISSA: Valores de saque são sempre *POSITIVOS*!
    def __init__(self, valor):
        self.valor = valor

    def sacar(self, saldo, valor):
        if valor > saldo:
            return 'Saque não permitido'
        else:
            self.saldo -= valor
            return valor



        

class Historico():
    # Toda conta tem o seu historico.
    def __init__(self, historico:dict={}):
        self.historico = historico

    def adicionar_transacao(self, datetime, operacao, valor):
        # Talvez no futuro registrar() conecte uma DB?
        transacao = {datetime: (operacao, valor)}  # dict with tuples
        self.historico.update(transacao)

    def __str__(self):
        if len(self.historico) < 1:
            return '(nenhum historico)'
        else:
            return "->\n".join([f'{k}: v' for k,v in self.historico.items()])



class Cliente():

    def __init__(self, 
                 responsavel:object, 
                 endereco:str, 
                 contas:list=None):
        # 'responsavel' recebe um objeto PessoaFisica
        # 'contas' fica com uma lista de ints (ex: [0001,0002,2238])
        self.responsavel = responsavel
        self.endereco = endereco
        self.contas = [] if contas is None else contas 
        # success msg
        print('Cliente criado com sucesso!', self.__str__())

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        pass

    def __str__(self):
        return "\n---CLIENTE---\n" + "\n".join([f"> {k.upper()}: {v}" for k,v in self.__dict__.items()]) + "\n------\n"



class PessoaFisica():
    def __init__(self, cpf: str, nome: str, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        # success msg
        print('Sucesso!', self.__str__())

    def __str__(self):
        return "(Pessoa Fisica)\n" + "\n".join([f"> {k.upper()}: {v}" for k,v in self.__dict__.items()]) + "\n"   



class Conta():
    def __init__(self, 
                 cliente:object=None,
                 saldo:float=0, 
                 numero:int=None, 
                 agencia:str='0001', 
                 historico:object=None):
        self.saldo = saldo
        self.numero = numero 
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

        #--por padrao, todas as contas sao conta corrente--
        ContaCorrente.__init__(self, limite=0, limite_saques=3)

        #--fazendo raise em caso de falta de cliente --
        if self.cliente is None:
            raise Exception('Erro. Conta sem cliente.')
        
        #--success msg--
        print('Conta obtida com sucesso!\n' + self.__str__())


    #----
    def saldo(self) -> float:
        return self.saldo

    def nova_conta(self, cliente, numero:int):
        pass

    def sacar(self, valor:float) -> bool:
        pass

    def depositar(self, valor:float) -> bool:
        pass
    
    def __str__(self):
        return "\n".join([f"{k.title()}: {v}" for k,v in self.__dict__.items()])



class ContaCorrente():
    def __init__(self, limite: float, limite_saques: int):
        self.limite = limite
        self.limite_saques = limite_saques



#---Rodando---

## Primeiro uma pessoa entra no banco e solicita... ser cliente.
## Dai sendo cliente, pode solicitar abrir uma conta.


# setting a person
luiz = PessoaFisica(12345678901, 'luizinho delas', 20010101)


# making a person into a client
cliente = Cliente(luiz, 'Rua dos Bobos, 0')


# opening an account when there is none under their name
cuenta = Conta(cliente, 0, 0, 0) 

