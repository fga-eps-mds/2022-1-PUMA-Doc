# Documento de Arquitetura

## Histórico de Revisão

| Data       | Versão | Modificação | Autor |
| :--------- | :----- | :---------- | :---- |
| 10/07/2022 | 0.1    | Criação do documento e adição da introdução | Eduardo    |
| 17/07/2022 | 0.2    | Acrescentando tópicos                       | Breno Yuri | 

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

#### Diagrama Entidade-Relacionamento

[]()

#### Diagrama Lógico de Dados

[]()
#### Dicionario de Dados

| Sigla | Tipo | Descrição |
| ----- | ---- | --------- |
|       |      |           |

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