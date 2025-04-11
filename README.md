# ----Sobre----

Este miniprojeto é a minha resolução do desafio [Criando um Sistema Bancário com Python](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py), versão 1, do bootcamp [Suzano - Python Developer](https://web.dio.me/track/suzano-python-developer) da DIO.me

Em vez de me inspirar no código providenciado [aqui](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py), eu resolvi fazer do zero para poder eu mesmo trabalhar no Vim, e para me adiantar a outros usuários, instanciando umas poucas classes desde o começo.

Ainda, este repositório faz parte de uma restrição autoimposta: No-Google Challenge, em que eu experimento trabalhar com uma stack sem quaisquer ferramentas do Google. Para tanto, foi utilizado Conda, Vim, Git, GitHub, e só.

----

[![LinkedIn Luiz Quevedo](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luiz-quevedo/)

[![Discord Luiz Quevedo](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/channels/@qvedo/)

[![GitHub Luiz Quevedo (você está aqui!)](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/luizquevedo)

## ----Como Rodar----

Este repo tem dois arquivos `.py`. O primeiro "dio_banco_v1.py" possui umas strings padrão e umas classes, e mais nada. Já o segundo possui apenas funções para usuários interagirem - ela puxa informações do primeiro arquivo como módulo. Além disso, separei anotações e explicações pontuais no arquivo "notas.md".
Como sempre, verifique o arquivo antes de rodar.

### ----Agradecimentos----

Deus salve o StackOverflow. Eu não teria conseguido sem.

### ----Anotações Soltas----

Três operações: depósito, saque, extrato

v1: Não precisa ainda lembrar de usuários diferentes!

Depósito
- deve ser armazenado

Saque
- out of bounds é erro, precisa ser handled
- limite diário de 500tão

Extrato
- listar todos os saques e depósitos
- formatação
