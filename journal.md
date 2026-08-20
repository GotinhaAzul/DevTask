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


Delete tasks - 
* Eu gastei uns 15 minutinhos nisso aqui. Era só reaproveitar a lógica de update tasks, mas me esqueci como funcionam dicionarios e listas, principalmente dicionarios com listas com dicionarios. Eu realmente não gosto de fazer isso com jsons.
* Esse erro meu me incentivou a documentar como tudo se comporta no meu código.


Eu tive um problema de merge... dei git push --force pois as mudanças na origin foram melhoradas no local.

Trabalhando aqui em lidar exceções, eu amo quem criou o .isnumeric :) Cara, que ideia genial.

Setup -
Criei essa função para criar os arquivos faltantes, se faltantes, e configurar o log.

Logging foi bem mais fácil do que fez parecer.


Testes; Parte 1 -
Fazer o teste em si foi até que ok. Eu decidi testar o create(), o check() com o assert e delete().

O complicado foi rodar 'pytest' na root e ir. Não fiz isso funcionar, mas, pytest só do test funcionou.


---

Épico 2 Planejamento

Classe Task 1
Classe TaskManager 2
Classe Storage 3
Classe Logging 4

1 vai ter apenas nome e id
2 recebe as funções
3 acessa e fecha o json
4 objeto intermediario de logs


Épico 3 -

Esse não foi tão difícil, resolvi tudo em umas 3 horas. Storage.py tava bem simples de atualizar, adicionei todo o CRUD nele e implementei com o SQL. 

Removi toda e qualquer noção que o taskmanager tinha sobre o banco de dados, dessa forma, ele vira um gerenciador mesmo.

Atualizar os testes foi o mais chato mesmo.

...

Eu estava prestes a entregar e vi um erro, faltou o close() em cada parada SQL, tá resolvido agora.


Épico 4 -

Trabalhando nas APIs, eu meio que me esqueci de escrever aqui.

Gastei meu token de IA para dar uma estruturada inicial e tô construindo por cima.

Lembrar de fazer uma nova endpoint para busca!
