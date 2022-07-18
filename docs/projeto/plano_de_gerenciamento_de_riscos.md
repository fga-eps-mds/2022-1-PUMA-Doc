## Histórico de Versão

|    Data    | Versão |                             Alteração                             |                    Autor                    |
|:----------:|:------:|:-----------------------------------------------------------------:|:-------------------------------------------:|
|09/07/2022|0.1|Criação do Documento|Enzo Gabriel e Breno Yuri|
|11/07/2022|1.0|Atualização das referências|Enzo Gabriel|

## Introdução

&emsp;&emsp;Segundo Freitas(2018)[2] A função do Plano de Gerenciamento de Riscos é definir como serão conduzidas as atividades de Gestão de Risco, ou seja, informar quais serão as medidas adotadas pela empresa para lidar com as possíveis ameaças ou oportunidades.
## Estrutura Analítica de Riscos (EAR)

&emsp;&emsp;É uma técnica que permite agrupar possíveis causas de riscos. A estrutura analítica dos riscos ajuda a equipe do projeto a considerar muitas fontes a partir dos quais os riscos podem surgir em um exercício de identificação de riscos. O EAR é dividido em 4 categorias[1], que são citadas abaixo:

- **Técnico:** Riscos agregados à tecnologia, requisitos e qualidade.
- **Externo:** Riscos vinculados ao cliente, mercado ou ambiente.
- **Organizacional:** Referente à priorização e recursos do projeto.
- **Gerência:** Afetam a estimativa, planejamento, controle e comunicação

## Análise Quantitativa

Mapear os riscos por probabilidade, impacto e com isso verificar as prioridades.

### Probabilidade

|Probabilidade|Intervalo|Peso|
|:----:|:-----:|:------:|
|**Muito Baixa**|0 a 5|1|
|**Baixa**| 6 a 30|2|
|**Média**| 31 a 50|3|
|**Alta**| 51 a 75|4|
|**Muito Alta**| 76 a 100| 5|

### Impacto

|Impacto|Descrição|Peso|
|:----:|:-----:|:------:|
|**Muito Baixo**|Impacto pouco relevante na execução do projeto|1|
|**Baixo**| Pouco impacto no processo do projeto|2|
|**Médio**| Impacto facilmente solucionado|3|
|**Alto**| Impacta consideravelmente a continuidade do projeto|4|
|**Muito Alto**| Impossibilita o desenvolvimento do projeto|5|

### Prioridade

Com base nas metricas do impacto e da probabilidade, realiza-se um cálculo Probabilidade/Impacto para organizar os niveis de prioridade dos riscos a serem resolvidos.

|Probabilidade/Impacto|Muito Baixa|Baixo|Média|Alta|Muito Alta|
|:----:|:-----:|:------:|:------:|:------:|:------:|
|**Muito Baixa**|1|2|	3|	4|	5|
|**Baixa**| 2|4	|6	|8	|10|
|**Média**| 3|6|	9	|12|	15|
|**Alta**| 4| 8	|12	|16|	20|
|**Muito Alta**| 5| 	10|	15	|20	|25|

Sendo que:

- Prioridade de 21 a 25: Muito Alto
- Prioridade de 16 a 20: Alto
- Prioridade de 11 a 15: Médio
- Prioridade de 6 a 10: Baixo
- Prioridade de 1 a 5: Muito Baixo

## Identificação dos Riscos

É feito um levantamento dos riscos analisando eventos anteriores de outros projetos e do time atual, fazendo comparações e analisando o presente momento de execução do projeto, para podermos categorizar os riscos levantados.

## Riscos levantados

|Risco|Descrição|Ação Preventiva|Ação Corretiva|Categoria|Probabilidade|Impacto|Prioridade|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|**R01**|Dificuldade com as tecnologias do projeto|Criar tarefas para estudo e aplicar treinamentos|Estudo e pareamentos efetivos|Técnico|3|5|15|
|**R02**|Atraso nas entregas|Organizar melhor o tempo dos integrantes|Definir novas datas e caso precise um novo pareamento|Gerência|4|4|17|
|**R03**|Qualidade do projeto não atender às expectativas do cliente|Alinhar frequentemente o estado do projeto e captar feedbacks dos clientes|Adaptar o projeto de acordo com as demandas do cliente|Externo|3|5|15|
|**R04**|Alguns dos membros contrair o Corona Vírus ou outra doença|Tomar vacinas, usar máscara com frequência e evitar ficar em lugares muito cheios|Realocar as tarefas do membro adoentado para outras pessoas do grupo|Externo|4|3|11|
|**R05**|A pandemia do Corona Vírus piorar ou surgir uma nova pandemia de alguma doença|Tomar cuidado, e seguir as recomendações das autoridades|Não há nada a ser feito|Externo|2|5|18|
|**R06**|Indisponibilidade de membros da equipe|Ter uma transparência de horários disponíveis e indisponíveis|Ter uma maior organização de tempo e redistribuição de tarefas|Externo|2|4|8|
|**R07**|Baixa produtividade dos integrantes do grupo|Motivação dos membros, e uma maior integração com reuniões constantes|Ter conversas para saber o motivo e agir diretamente no problema|Gerência|4|5|18|
|**R08**|Falta dos membros durante Daily e reunião de planejamento|Definir datas, horários e locais que sejam acessíveis a todos|Procurar saber os motivos da pessoa, e agir sobre esses motivos|Gerência|5|5|19|
|**R09**|Alteração do escopo|Manter boa comunicação com as partes envolvidas do projeto|Documentar e aprimorar os requisitos|Gerência|5|4|20|
|**R10**|Desistência da disciplina|Estimular a máxima participação dos membros da equipe|Distribuir tarefas para a quantidade de membros atuais do projeto|Gerência|3|5|15|
|**R11**|Falta de comunicação|Elaborar e seguir plano de comunicações|Rever plano de comunicação|Organizacional|4|3|13|
|**R12**|Conflito entre entregas da sprint e de tarefas de outras disciplinas|Organização das tarefas para não haver choque de entrega|Diminuir o escopo da sprint e redistribuir tarefas|Externo|5|3|13|
|**R13**|Alteração nas datas da disciplina|Não há nenhuma ação a ser feita|Redefinir datas das entregas|Externo|2|4|8|
|**R14**|Aperto nas entregas devido ao semestre mais curto|Se organizar previamente para evitar muitas tarefas acumuladas|Se empenhar para fazer a tarefa de maneira correta e melhorar para as próximas|Gerência|4|5|19|
|**R15**|Greves na UNB|Não há nenhuma ação a ser feita|Não há nenhuma ação a ser feita|Externo|2|5|1|

## Medidas de gerenciamento

<iframe width="700" height="300" style="-webkit-transform:scale(0.8);-moz-transform-scale(0.8);" frameborder="0" scrolling="yes" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRadOwXUyGLBt_2fbIkZx446JHsAbbQi8Mo8Lrmi3sdPvA8sKFV_lXYHIyYh6xX6aavPU6cEquGNdsR/pubhtml"></iframe>

## Bibliografia

[1] JOÃO, Lucas. Plano de Gerenciamento de Riscos do grupo ArBC. Disponível em: https://github.com/fga-eps-mds/2019.2-ArBC/blob/develop/docs/Plano-Gerenciamento-Riscos.md. Acesso em 09 jul 2022.

[2] FREITAS, Renata. Aplique o Plano de Gerenciamento de Riscos no seu negócio. Disponível em: https://www.glicfas.com.br/plano-de-gerenciamento-de-riscos/. Acesso em 09 jul 2022.