nota 01:
Saldo começa como zero. Precisa começar como zero, do contrário uma conta tira grana do nada.

nota 02:
# Heads Up! doing .join(f"{comprehension}".join() 
# evaluates that comprehension twice!
# In order to see what happens, do replace + with .join()

nota 03: Snippet
```
        #--Get previous history from file, GET ONLY
        try:
            with open("historico.txt", "r") as file:
                historico = OrderedDict(f.read())
        except:
            self.historico = OrderedDict()  # {datetime: (balance_delta, _)}
```

nota 04:
#--Mapeando opcao escolhida a sua correspondente funcao externa
#, assumindo que as funções são aquelas quatro e somente aquelas quatro
#, e assumindo que opcao já foi filtrada por interface().
#
# Ademais, a estratégia adotada foi match-case, no lugar de construtor.


nota 06:
As funções retornam valores ou jogam erros.
Quem fica responsável por mostrar no sysout é o run.py e apenas o run.py (Princípio da Responsabilidade Única).


Changelog
1. dio_banco_v2.py criado (talvez seja desnecessário? o .git serve pra isso!)
2. uso do módulo datetime em vez do time
3. self.numero_de_operacoes
4. uma variedade de util functions
5. retirado current_working_functions


nota 07:
Novo desafio  
_ Estabelecer limite de 10 transações diárias para a conta
__ Em caso de tentativa após o limite, informar que excedeu 
_ Mostrar no extrato data e hora de todas as transações
? Salvar transações ou em .csv ou em banco de dados


nota 08:

Eu tinha colocado o seguinte `#TODO:format using time.asctime() instead of datetime.strftime()`, contudo Exu matou um pássaro hoje com uma pedra que jogou ontem; acontece que o formato `%c` é praticamente idêntico.

nota 09:

Novo desafio
_ (novo) Criar funções: 
__ cadastrar usuário*
__ cadastrar conta bancária** & vincular a algum usuário
_ (feito) ~~Criar funções para as op. existentes (s, d, e)~~
? Menu inicial de acesso a usuario e a conta
? Armazenamento persistente****

_* Um usuário é composto por: (nome, data de nascimento, CPF, endereço). Já o endereço é composto por: (logradouro,"-", número, "-",bairro ,"-", cidade + "/" + sigla estado). Ainda, o CPF é só números, sem havendo dois CPF iguais. O programa deve armazenar os usuários em uma lista. [alist? o instrutor sugere list\_of\_dicts.]

_** Uma conta é composta por: (agencia, numero da conta, usuario).
A agencia é única: "0001". Já o numero da conta é sequencial iniciando em 1. Por fim um usuário pode ter várias contas, mas uma conta pertence a um [e somente um] usuário [many-to-one].

_*** Dica: criar uma conta já vinculando a um usuário. Caso não exista o usuário fornecido, não criar conta.

_**** [SQLite??? arquivo.txt com stdlib.os.remove()?]


nota 10:
Por enquanto, eu vou separar, ter o cadastro separado do loop da interface. Vai ser antes.

nota 11:
eu PRECISO aprender a fazer Factory. E ainda, ATENÇÃO! Global variables podem ser acessadas a qualquer momento durante a execução do programa, expondo dados sensíveis.

nota 12:
Agora a função get_historico pode obter a partir de um registro de cpf, que é único, e no futuro será uma conta. Inclusive, pode obter de cpf nenhum, o que não altera seu funcionamento da v1 pra -> v2. Mas se tiver, se um cpf for passado, aí ele pega - não, ele instancia as operações só naquele cpf ou naquela conta.


Changelog
1. adicionada `class Account` 
2. agora Dio.User é instanciada, tendo como base o prompt de Account.get_cpf()
2.1. get_cpf() aceita _qualquer_ texto, por enquanto.
# em 1. eu pensei em escrever "adicionado Monad (cpf -> Dio.User)"

nota 13:
Não é muito mais fácil fazer um código modular? Não é muito mais fácil fazer um _módulo_ que acesse uma conta? Assim o código funciona sozinho, com menu e writes, como está. Nada se quebra.
AVISO! ...só que agora eu trabalho na pasta GitHub.

nota 14: Naming Convention
class name(EN)
def name < (action(EN) + short_desc(PTBR)
variable name(PTBR)
#"code commented-out"
# "notes or in-line docs"
#---"TITLE"--- < "big sections of code"
#see note [0-9][0-9] > notas.md

nota 15: "Sidequest"
---
# get file to append to; otherwise, make file
# TODO: time this against "'a' if os.path.exists... else 'w'"

if os.path.exists("armazenamento_contas.csv"):
    filehandle = open("armazenamento_contas.csv", "a")  #append  
else:
    filehandle = open("armazenamento_contas.csv", "w")  #touch + open in write mode
---

Changelog
1. criado dio\_conta\_v1.py, que gerencia registro & leitura de contas
2. adicionado armazenamento_contas.csv via dio\_conta\_v1.py



