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
