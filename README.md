Prólogo -
* Eu acabei de inicializar o projeto usando 'uv init'. 
  - Eu usei uv por ele ser extremamente mais rápido do que pip e eu já o tinha instalado na minha máquina.
* Também comecei o git com 'git init' e dei push pro repo criado no Github.


Planejamento Épico 1 - 
* Certo.. primeiro eu vou estudar em como editar JSONs com python, ai fazer o CRUD com eles. Dar um print em todas as opções primeiro, depois vejo se devo melhorar isso.

Create Tasks -
* Foi mais chato do que pensava. Ler e editar Jsons, principalmente para dar append, é muito chato. No fim, fiz o seguinte: Abre o dados.json e le o que tem lá, então, coloca em uma lista. Vê o novo dado a adicionar, adiciona na lista e então dá overwrite no dados.py
* Eu resolvi fazer isso ao invés de usar o append do open() por que vai facilitar meu trabalho futuramente na hora de ler as tasks e edita-las.

Read Tasks - 
* Foi melhor do que pensava. Enquanto programava essa, percebi que eu teria de fazer alguma forma de o usuário marcar uma task como Done, então... vou ver isso aí agora. Eu praticamente repliquei o que fiz em Create Tasks e fiz uma busca em dicionário que já havia feito em exercícios antes.


Markasdone Tasks -
* Isso aqui foi bem complicado. Tentei muita coisa, pesquisei- mesmo sem resultados, e finalmente pensei em algo. Eu abri o dados.json para ver como era os dados, né? Ai eu vi que era um dicionário 'tasks' com uma lista de outros dicionários, ai ficou fácil.


Update tasks -
* Markasdone só que para nomes, já que, por hora, é a única coisa alterável.
* Eu adicionei uma nova função chamada check(), ela serve para garantir que o ID exista.
