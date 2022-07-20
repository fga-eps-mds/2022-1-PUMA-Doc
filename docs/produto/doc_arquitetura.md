# Documento de Arquitetura

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-- | :-- | :-- | :-- |
| 10/07/2022 | 0.1 | Criação do documento e adição da introdução | Eduardo    |
| 17/07/2022 | 0.2 | Acrescentando tópicos                       | Breno Yuri | 

### 1. Introdução  

<p  align="justify">    Este documento tem como função explicar e exemplificar a arquitetura de software utilizada no desenvolvimento do projeto PUMA, afim de garantir uma maior facilidade na visualização dos requisitos e da estrutura para os desenvolvedores.</p>

#### 1.1 Finalidade  

<p  align="justify">    Fazendo um projeto da arquitetura do projeto PUMA, possibilitará uma visão ampla da arquitetura do projeto. Portanto esse documento tem como finalidade mostrar as decisões tomadas pela equipe no desenvolvimento PUMA.</p>

#### 1.2 Escopo

<p  align="justify">    O PUMA tem como principal função dar suporte para a Engenharia de Produção, sendo no auxilio na seleção de times, propostas, projetos e feedbacks aos agentes externos. Neste documento será exposto os padrões arquiteturais utilizados no desenvolvimento do projeto. Será apresentado neste documento a lógica de construção do sistema, tecnologias utilizadas, implementação e frameworks.</p>

#### 1.3 Visão Geral

Estrutura do documento:  

* Introdução;
* Representação da Arquitetura; 
* Metas e Restrições de Arquitetura;
* Visão lógica;


#### 1.4 Definições, Acrônimos e Abreviações

| Sigla       | Significado |
| :---------  | :-----      | 
| HTML	| Hypertext Markup Language (Linguagem de Marcação de Hipertexto) |
| HTTP  | Hypertext Transfer Protocol (Protocolo de Transferência de Hipertexto)|
| SQL   | Structured Query Language (Linguagem de Consulta Estruturada) |
| API   | Application Programming Interface (Interface de Programação de Aplicações)|


### Representação dos Serviços

#### Front End

<p> O front end é a interface onde o usuário irá se comunicar com o sistema. É composto por uma tela de cadastro e outra de registro, o que leva à página inicial do PUMA, a página de perfil de usuário. Nesse ponto, há a possibilidade de seguir diversos caminhos dentro do sistema, como as páginas de cadastro de proposta, avaliação de proposta e repositório de projetos.
</p>

#### API Gateway

<p> O API Gateway é utilizado como um mutex para a comunicação entre a interface de usuário e os outros micro-serviços. Dessa forma, ao receber uma requisição o gateway atua como uma ponte entre o front end e o serviço desejado.
</p>

#### Project-Service

<p>    O serviço "Project-Service" foi planejado para lidar com todas as tarefas envolvendo projetos do sistema. Assim, o envio de propostas, o encaminhamento para o professor / disciplina adequada e as possíveis alterações nos projetos seriam todas tarefas para o Project-Service resolver.
</p>

#### User-Service
<p> Desenvolvido para manter o controle de usuários, desde sua criação até o controle das rotas de acesso permitidas, criação de times dentre outros. </p>

### Tecnologias

#### Vue.js 
<p  align="justify">    É um framework Javascript open-source para criação de aplicações web, ele é muito utilizado para criação de aplicações SPA (Single Page Applications) e também pra vários outros tipos de interface, com foco na interação e experiência do usuário.
</p>

#### Node.js
<p  align="justify">    É uma plataforma de aplicação para Javascript, que tem como principal objetivo facilitar a construção de softwares escaláveis. Ele geralmente é usado ao lado do servidor e é orientado para o estilo de programação voltada a evento. Isso faz com que ele seja leve, eficiente e uma boa alternativa para arquitetura de microsserviços.
</p>

#### PostgreSQL 
<p  align="justify">    O PostgreSQL é um gerenciador de banco de dados relacionais que proporciona forte confiabilidade, robustez de recursos e desempenho.
</p>

#### Docker
<p  align="justify">    Docker é uma plataforma, open-source para criação, execução e deploy de contêineres. Esses contêineres são pacotes da aplicação contendo suas dependências, bibliotecas e arquivos de configuração.
</p>

#### Docker Compose
<p  align="justify">    Docker Compose é um orquestrador de contêineres Docker. Com ele é possível gerenciar vários contêineres de uma única vez, definindo o comportamento de cada um deles.
</p>


### Referência 

* DUARTE, Bruno; NOGUEIRA, Gustavo. Documento de Arquitetura do grupo PUMA 2021-2. Disponível em: https://github.com/fga-eps-mds/2021-2-PUMA-Doc. Acesso em 17 Jul 2022.