# Notes
--- 
### note 01
Esta é uma continuação do Desafio Bancário, do bootcamp de Python da Digital Innovation One. Nesta parte, sugere-se instanciar objetos e classes, de acordo com um diagrama UML - sem criar novos módulos (talvez arquivos me ajudem).

### note 003
Quem vai subir pro historico na verdade é Deposito.registrar() com base no ponteiro self.historico:Historico. 
Repare! self.historico não é uma estrutura de dados, é um ponteiro pra um objeto que a contém.

### note 004
Duas operações vão acontecer no mesmo segundo??? E se? Meu filho, este programa roda na CLI. Se acontecer eu vou estar DJ Khalid: Suffering From Success. Caso no qual a gente vem e melhora a implementação. Em todo caso, *otimização prematura é a raiz de todo mal.*

### note 005
Como criar arquivos de histórico?

Por ora, vai se fazer um struct de nome de arquivo, para padronizar.
'historico'+self.conta
