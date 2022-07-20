# Documento de Arquitetura

## Histórico de Revisão

| Data       | Versão | Modificação | Autor |
| :--------- | :----- | :---------- | :---- |
| 10/07/2022 | 0.1    | Criação do documento e adição da introdução | Eduardo    |
| 17/07/2022 | 0.2    | Acrescentando tópicos                       | Breno Yuri | 
| 20/07/2022 | 0.3    | Adiciona Representação de Dados             | Breno Yuri, Eduardo, Giovanna, Felipe, Cainã | 

### Introdução  

<p  align="justify">    Este documento tem como função explicar e exemplificar a arquitetura de software utilizada no desenvolvimento do projeto PUMA, afim de garantir uma maior facilidade na visualização dos requisitos e da estrutura para os desenvolvedores.</p>

#### Finalidade  

<p  align="justify">    Fazendo um projeto da arquitetura do projeto PUMA, possibilitará uma visão ampla da arquitetura do projeto. Portanto esse documento tem como finalidade mostrar as decisões tomadas pela equipe no desenvolvimento PUMA.</p>

#### Escopo

<p  align="justify">    O PUMA tem como principal função dar suporte para a Engenharia de Produção, sendo no auxilio na seleção de times, propostas, projetos e feedbacks aos agentes externos. Neste documento será exposto os padrões arquiteturais utilizados no desenvolvimento do projeto. Será apresentado neste documento a lógica de construção do sistema, tecnologias utilizadas, implementação e frameworks.</p>

#### Visão Geral

Estrutura do documento:  

* Introdução;
* Representação da Arquitetura; 
* Metas e Restrições de Arquitetura;
* Visão lógica;


#### Definições, Acrônimos e Abreviações

| Sigla | Significado                                                                |
| :---  | :------------------------------------------------------------------------  | 
| HTML	| Hypertext Markup Language (Linguagem de Marcação de Hipertexto)            |
| HTTP  | Hypertext Transfer Protocol (Protocolo de Transferência de Hipertexto)     |
| SQL   | Structured Query Language (Linguagem de Consulta Estruturada)              |
| API   | Application Programming Interface (Interface de Programação de Aplicações) |


### Representação de relações

[]()

### Representação dos Serviços

#### Front End

O front end é a interface onde o usuário irá se comunicar com o sistema. É composto por uma tela de cadastro e outra de registro, o que leva à página inicial do PUMA, a página de perfil de usuário. Nesse ponto, há a possibilidade de seguir diversos caminhos dentro do sistema, como as páginas de cadastro de proposta, avaliação de proposta e repositório de projetos [[2]](#ref2).


#### API Gateway

O API Gateway é utilizado como um mutex para a comunicação entre a interface de usuário e os outros micro-serviços. Dessa forma, ao receber uma requisição o gateway atua como uma ponte entre o front end e o serviço desejado [[2]](#ref2).

#### Project-Service

O serviço "Project-Service" foi planejado para lidar com todas as tarefas envolvendo projetos do sistema. Assim, o envio de propostas, o encaminhamento para o professor / disciplina adequada e as possíveis alterações nos projetos seriam todas tarefas para o Project-Service resolver [[2]](#ref2).

#### User-Service

Desenvolvido para manter o controle de usuários, desde sua criação até o controle das rotas de acesso permitidas, criação de times dentre outros [[2]](#ref2). 

### Tecnologias

#### Vue.js 

Vue.js é um framework JavaScript de código-aberto, focado no desenvolvimento de interfaces de usuário e aplicativos de página única [[6]](#ref6). 

#### Node.js

Node.js é um software de código aberto, multiplataforma, baseado no interpretador V8 do Google e que permite a execução de códigos JavaScript fora de um navegador web [[4]](#ref4). 

#### PostgreSQL 

PostgreSQL é um sistema gerenciador de banco de dados objeto relacional, desenvolvido como projeto de código aberto [[5]](#ref5).

#### Docker

Docker é um conjunto de produtos de plataforma como serviço que usam virtualização de nível de sistema operacional para entregar software em pacotes chamados contêineres. Os contêineres são isolados uns dos outros e agrupam seus próprios softwares, bibliotecas e arquivos de configuração [[3]](#ref3).

#### Docker Compose

O Compose é uma ferramenta para definir e executar aplicativos Docker de vários contêineres. Com o Compose, você usa um arquivo YAML para configurar os serviços do seu aplicativo [[1]](#ref1).

### Representação de Dados

#### Modelo Entidade-Relacionamento

##### Entidades

&emsp;&emsp;COMMON_USER <br>
&emsp;&emsp;&emsp;&emsp;STUDENT <br>
&emsp;&emsp;&emsp;&emsp;PROFESSOR <br>
&emsp;&emsp;&emsp;&emsp;JURIDICAL_AGENT <br>
&emsp;&emsp;&emsp;&emsp;PHYSICAL_AGENT <br>
&emsp;&emsp;PROJECT <br>
&emsp;&emsp;SUBJECT <br>
&emsp;&emsp;CLASS <br>
&emsp;&emsp;FILE <br>
&emsp;&emsp;SUBAREA <br>
&emsp;&emsp;KNOWLEDGE_AREA <br>

##### Atributos

&emsp;&emsp;COMMON_USER (**userId**, fullName, email, passwordHash, phoneNumber, isAdmin) <br>
&emsp;&emsp;STUDENT (regNumber, **userId**, softSkills) <br>
&emsp;&emsp;PROFESSOR (regNumber, **userId**) <br>
&emsp;&emsp;JURIDICAL_AGENT (**userId**, cnpj, cep, companyName, socialReason) <br>
&emsp;&emsp;PHYSICAL_AGENT (**userId**, cpf) <br>
&emsp;&emsp;PROJECT (**projectId**, name, description (problem, expectedResult, knowledgeArea)) <br>
&emsp;&emsp;SUBAREA (**subAreaId**, description) <br>
&emsp;&emsp;SUBJECT (**subjectId**, name, courseSyllabus) <br>
&emsp;&emsp;CLASS (**classId**, subjectTerm, code, regNumber, subjectId) <br>
&emsp;&emsp;FILE (**fileId**, projectId, filename, byteContent) <br>

##### Relacionamentos

&emsp;&emsp;COMMON_USER - submits - PROJECT <br>
&emsp;&emsp;&emsp;&emsp;Um usuário submete um ou mais projetos e um projeto é proposto por apenas um usuário. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: 1:N. <br>
<br>
&emsp;&emsp;STUDENT - participates - CLASS <br>
&emsp;&emsp;&emsp;&emsp;Um estudante participa de uma ou mais turmas e uma turma é participada por um ou mais alunos. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M <br>
<br>
&emsp;&emsp;STUDENT - executes - PROJECT <br>
&emsp;&emsp;&emsp;&emsp;Um estudante executa um ou mais projetos e um projeto é executado por um ou mais alunos. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M <br>
<br>
&emsp;&emsp;PROFESSOR - lectures - SUBJECT <br>
&emsp;&emsp;&emsp;&emsp;Um professor pode lecionar várias disciplinas e uma disciplina pode ser lecionada por vários professores. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M. <br>
<br>
&emsp;&emsp;PROJECT - has - FILE <br>
&emsp;&emsp;&emsp;&emsp;Um projeto pode possuir vários arquivos e um arquivo pertence a somente um projeto. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: 1:N. <br>
<br>
&emsp;&emsp;SUBAREA - identifies - SUBJECT <br>
&emsp;&emsp;&emsp;&emsp;Uma sub-área pode identificar várias disciplinas e uma disciplina é identificada por uma ou mais sub-áreas. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M. <br>
<br>
&emsp;&emsp;KNOWLEDGE_AREA - contains - SUBAREA <br>
&emsp;&emsp;&emsp;&emsp;Uma área do conhecimento pode conter várias subáreas e uma subárea é contida por somente uma área do conhecimento. <br>
&emsp;&emsp;&emsp;&emsp;Cardinalidade: N:M. <br>

#### Diagrama Entidade-Relacionamento

![](../assets/imagens/arquitetura/DER.png)

#### Diagrama Lógico de Dados

![](../assets/imagens/arquitetura/DLD.png)

#### Dicionario de Dados

##### PROJECT
| Sigla | Tipo | Descrição |
| ----- | ---- | --------- |
| SB    | ENUM | Utilizado quando a proposta é submetida.                                           |
| RL    | ENUM | Utilizado quando professor/administrador realoca a proposta para outra disciplina. |
| AL    | ENUM | Utilizado quando a proposta não possui disciplina alocada (a disciplina adequada para a proposta não é conhecida pelo professor responsável). |
| AC    | ENUM | Utilizado quando a proposta for aceita por um professor/administrador, porém ainda não incluída a nenhum semestre.|
| RC    | ENUM | Utilizado quando a proposta for recusada por um professor/administrador.           |
| IC    | ENUM | Utilizado quando a proposta for incluída para o semestre de alguma disciplina.     |
| EX    | ENUM | Utilizado quando o(s) time(s) designado(s) inicia(m) o desenvolvimento do projeto. |
| EC    | ENUM | Utilizado quando o desenvolvimento do proejto for concluído.                       |


#### SEMESTER

| Sigla | Tipo | Descrição                                |
| ----- | ---- | ---------------------------------------- |
| AD    | ENUM | Para os semestres eu estão em andamento. |
| CD    | ENUM | Para os semestres concluídos.            |


#### POST

| Sigla | Tipo | Descrição                           |
| ----- | ---- | ----------------------------------- |
| ED    | ENUM | Para publicação de editais.         |
| NT    | ENUM | Para publicação de notícias.        |
| DP    | ENUM | Para divulgar os melhores projetos. |

### Referência 

<a id="ref1"></a>
[1] DOCKER. Disponível em: https://docs.docker.com/compose/. Acesso em 20 Jul 2022.

<a id="ref2"></a>
[2] DUARTE, Bruno; NOGUEIRA, Gustavo. Documento de Arquitetura do grupo PUMA 2021-2. Disponível em: https://github.com/fga-eps-mds/2021-2-PUMA-Doc. Acesso em 17 Jul 2022.

<a id="ref3"></a>
[3] WIKIPEDIA. Docker (software). Disponível em:  https://pt.wikipedia.org/wiki/Docker_(software). Acesso em 20 Jul 2022.

<a id="ref4"></a>
[4] WIKIPEDIA. Node.js. Disponível em: https://pt.wikipedia.org/wiki/Node.js. Acesso em 20 Jul 2022.

<a id="ref5"></a>
[5] WIKIPEDIA. PostgreSQL. Disponível em: https://pt.wikipedia.org/wiki/PostgreSQL. Acesso em 20 Jul 2022.

<a id="ref6"></a>
[6] WIKIPEDIA. Vue.js. Disponível em: https://pt.wikipedia.org/wiki/Vue.js. Acesso em 20 Jul 2022.