# ---desafio_v2_feature_historico.py---
# see note 01



from abc import ABC, abstractmethod
from datetime import datetime
from json import loads, dumps  # alt: load, dump


class Transacao(ABC): 
    @abstractmethod
    def registrar(self):
        pass

#---!!! A T E N C A O !!!---
# Voce esta na branch feature_historico
#
# todo: branch 1 (né aqui não!!!)
# TODO: branch 2 -> conta -> historico (registrar qqr coisa ae mano, não precisa ser operações não.)
#
# OBJETIVO: registrar qualquer coisa via Historico()
# Feito
# PROBLEMA de programação: impl. funcionalid. Create, Read, Update
# Funcionalidades CRU feitas via Historico.adicionar_transacao()
#------

class Deposito(Transacao):
    # PREMISSA: Valores de depósito são sempre positivos.
    
    def depositar(self, valor:float) -> bool:
        # TODO: sanitize your inputs!        
        if valor < 0:
            print('\n\nErro ao depositar.\n\nFavor verificar.\n\n')
            return False
        self.saldo += valor
        return True

    def registrar(self):
        # pegar o ponteiro self.historico:Historico.
        #self.historico:object
        # extrair as transações ou a estrutura de dados
        #Feito via chamado de self.historico.transacoes
        # append ou update
        #Feito via Historico.adicionar_transacao
        # fazer o set da estrutura de dados no objeto historico
        Historico.adicionar_transacao(
                self,
                self.__class__.__name__,
                'valor',
                )
        pass


class Saque():
    # PREMISSA: Valores de saque são sempre *POSITIVOS*!

    def sacar(self, valor):
        print('\nAtenção: se você está vendo isso, você não tem uma conta corrente.\nFavor verficar.\n\n')
        if valor > self.saldo:
            print('Saque não permitido')
            return False
        else:
            self.saldo -= valor
            return True

    def registrar(self):
        # vide Deposito.registrar()
        pass

        

class Historico():
    # Toda conta tem o seu historico. 'self.historico = Historico()

    def __init__(self, numero_da_conta:str): 
        # Talvez no futuro conecte uma DB?
        # see note 005

        self.filename = 'historico'+str(numero_da_conta)+'.json'
        try:
            # try opening 'historico000000001-9.txt'
            with open(self.filename, 'r') as filehandle:
                self._transacoes = loads(filehandle.read())
        except FileNotFoundError: 
            self._transacoes = {}


    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, operacao:str, valor):
        #---Adicionar transacao---

        dataihora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        transacao = {dataihora: {
            'tipo': operacao, 
            'valor': valor,
            }}  # dict with dicts
        
        # fazer Update de self.transacoes:dict
        # E se duas operacoes ocorrerem ao mesmo tempo??? see note 004
        self.transacoes.update(transacao)

        # escrever no arquivo. abrir em modo write/append nunca grita erro pois abre um arquivo se não tiver.
        with open(self.filename, 'w') as filehandle:
            filehandle.write(dumps(self.transacoes).strip('\n'))
            # uma linha alternativa com "open(self.filename, 'a'(...)dumps(transacao)" faz raise do erro 'json.decoder.JSONDecodeError: Extra data'
            # esta linha com modo write, ela tem O(triangular) uma vez que reescreve tudo de novo, mas deve evitar erros por enquanto!


        
        #------


    def __str__(self):
        if len(self.transacoes) < 1:
            return '(nenhum historico)'
        else:
            return "->\n".join([f'{k}: v' for k,v in self.transacoes.items()])



class Cliente():

    def __init__(self, 
                 responsavel:object, 
                 endereco:str, 
                 contas=None):
        # 'responsavel' recebe um objeto PessoaFisica
        # 'contas' fica com uma lista de ints (ex: [0001,0002,2238])
        self.responsavel = responsavel
        self.endereco = endereco

        #self.contas = [] if contas is None else contas 
        # Quem verifica se 'cliente.contas is None' é na verdade Conta.nova_conta()
        self.contas = contas

        # success msg
        print('Cliente criado com sucesso!', self.__str__())

    def realizar_transacao(self, conta, transacao):
        # ...pegar a conta certa
        # ...realizar a transacao nela daí
        pass

    def adicionar_conta(self, conta):
        # ...pegar a conta atual (eu acho) 
        # ...recolher seu ID e juntar em cliente.contas
        pass

    def __str__(self):
        return "\n---CLIENTE---\n" + "\n".join([f"> {k.upper()}: {v}" for k,v in self.__dict__.items()]) + "\n------\n"



class PessoaFisica():
    def __init__(self, cpf: str, nome: str, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        # success msg
        print('\n\nSucesso!\n' + self.__str__())

    def __str__(self):
        return "(Pessoa Fisica)\n" + "\n".join([f"> {k.upper()}: {v}" for k,v in self.__dict__.items()]) + "\n"   



class Conta(Deposito, Saque):
    # Por que não simplesmente herdar as operações?

    def __init__(self, 
                 cliente:object=None,
                 saldo:float=0, 
                 numero:int=None, 
                 agencia:str='0001', 
                 historico:object=None):  # possivel ataque: injetar um historico fake
        self.saldo = saldo
        self.numero = numero 
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico(self.numero)

        #--por padrao, começa tipo 'conta', podendo virar corrente--
        pass

        #--fazendo raise em caso de falta de cliente --
        if self.cliente is None:
            raise Exception('Erro. Conta sem cliente.')
        
        #--success msg--
        print('Conta obtida com sucesso!\n' + self.__str__())


    #----
    def saldo(self) -> float:
        return self.saldo

    def nova_conta(self, cliente, numero:int):
        # checar se o cliente.contas ja possui alguma conta
        # caso negativo: acessar DB, puxar o proximo numero, instanciar uma nova Conta, e aí se der certo adicionar ID em cliente.contas
        # Quem adiciona em cliente.contas na verdade é Cliente.adicionar_conta()
        pass

    def sacar(self, valor:float) -> bool:
        pass

    def depositar(self, valor:float) -> bool:
        # checar se valor < 0
        # caso negativo chamar Deposito.depositar()
        # see note 003. Quem vai subir pro historico na verdade é Deposito.registrar() com base no ponteiro self.historico:Historico. Repare! self.historico não é uma estrutura de dados, é um ponteiro pra um objeto que a contém.
        pass
    
    def __str__(self):
        return "\n".join([f"{k.title()}: {v}" for k,v in self.__dict__.items()])



class ContaCorrente(Conta):
    def __init__(self, limite: float, limite_saques: int):
        super().__init__(self, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    



#---Rodando---
##--Exploração inicial
## Primeiro uma pessoa entra no banco e solicita... ser cliente. Daí, sendo cliente, pode solicitar abrir uma conta.

    
def conta_demo():    
    global luiz, cliente, conta

    # instanciando uma pessoa
    luiz = PessoaFisica(12345678901, 'luizinho delas', 20010101)
    
    # 'clientizando' uma pessoa 
    cliente = Cliente(luiz, 'Rua dos Bobos, 0')
    
    # abrindo a primeira conta do cliente
    conta = Conta(cliente, 0, 0, 0) 
    
    print("Conta demo instanciada.\n(explore 'luiz', 'cliente' e 'conta' na CLI\n")



##--Simulação de autoatendimento--
## Abertura de conta: 1.dados da pessoa fisica; 2.clientizar; 3.abrir a primeira conta; 4. mostrar

# loopando interface com usuario 
while resp := input('Abrir uma conta? [y/n]\n(aperte n e Enter para cancelar)\n>>> ').lower() != 'n':
    # 1.
    print('Certo, vamos cadastrar uma pessoa física.\nPreciso das seguintes informações:')

    # PREMISSA: é *inseguro* o acesso público para acessar PessoaFisica.__dict__.keys()... proibido!
    '''
    if len(PessoaFisica.__dict__.keys()) != 3:
        raise NotImplementedError('Erro. Robô responsável pelas pessoas físicas: em manutenção. Por favor, falar com um atendente.')'''
    
    # 'campos' é um iterável cujas chaves são, sem tirar nem por, os argumentos da função que instancia, nem mais nem menos.
    campos = dict.fromkeys(
            ('CPF', 'Nome completo', 'Data de nascimento'), 
            None
            )
    # 'campos' recebe strings do usuário.
    for k in campos.keys():
        campos[k] = input(f'{k}:\n>>> ')
    # 'campos' é expandido no ato de instanciar.
    try:
        pessoa = PessoaFisica(*campos.values())
    except:
        raise NotImplementedError('Erro. Robô não conseguiu criar uma instância de pessoa física.')
    

    # 2. clientizando
    endereco = input('Endereço:\n>>> ')
    cliente = Cliente(pessoa, endereco)

    # 3. abrindo conta
    conta = Conta(cliente, numero='00000001-9')

    # 4. mostrando
    # Feito via *.__str__
    break


    
if not resp:
    conta_demo()
else:
    print('O Banco agradece sua visita. Até a próxima!')
