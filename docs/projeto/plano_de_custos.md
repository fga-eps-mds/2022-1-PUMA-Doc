# Plano de Custos
## Introdução

Esse documento foi criado com o objetivo de registrar as estimativas dos custos financeiros relacionados à realização do projeto PUMA no semestre 2022.1. Para sua montagem, foram utilizados dados disponíveis no Mural, no Zenhub e no backlog do produto, além de consultas a preços de produtos disponíveis em lojas virtuais e serviços ofertados em Brasília, DF.

Sabendo que os valores, especialmente de equipamentos, são variáveis e que uma estimativa depende de diversos fatores, o plano de custos poderá sofrer alterações ao longo do projeto. Tais mudanças terão sempre como objetivo ilustrar os custos com boa precisão e abrangência.

Por fim, note que não há estimativa de custos para publicação do produto e, nos gastos totais, não serão levados em consideração os gastos com equipamentos. Isso se deve ao fato de que o PUMA ainda não chegou em sua fase ideal para publicação, além de que os integrantes já possuíam seus próprios equipamentos para realizar o projeto.

## Custo com Pessoal

Considerando que a equipe é formada por 13 membros matriculados em Engenharia de Software na Universidade de Brasília, e utilizando informações presentes no inforgráfico disponibilizado em [O Globo](https://infograficos.oglobo.globo.com/brasil/raio-x-do-custo-por-aluno-nas-universidades-federais.html), têm-se que o custo por aluno em tal universidade, no ano de 2016, foi de R$ 38.805,00. Convertendo o valor anual para mensal e diário, têm-se, respectivamente, R$3.233,75 e R$104,31 [[2]](#ref2).

É importante destacar que a jornada de trabalho será de 30 horas semanais, ou seja, 5 horas diárias. Assim, o cálculo do custo total com os desenvolvedores será dado por:

<p style="text-align: center; background-color: lightgray; margin: 2em;">custoPessoal = valorHora X qtdDias X qtdPessoas</p>

## Custos com Equipamentos

Para o desenvolvimento do PUMA, é necessário que cada integrante da equipe possua equipamentos capazes de executar o projeto sem impedimentos. Também se faz necessário o uso de dispositivos de áudio de qualidade, visto que ocorrerão reuniões online recorrentes e é imprescindível um bom áudio para que a comunicação seja eficaz. Com isso em mente, cada desenvolvedor deverá possuir um notebook e um headset, sendo outros periféricos opcionais para aquisição.

As configurações recomendadas de hardware para este projeto são: i5 de 10a geração ou posterior, 16gb de RAM e armazenamento SSD.

<p style="text-align: center; background-color: lightgray; margin: 2em;">custoEquipamento = (valorFone X qtd) + (valorNotebook X qtd)</p>

## Custo com Serviços

O desenvolvimento do projeto exige conexão estável com a internet, sendo, portanto, recomendada a contratação de um pacote de internet por operadora. Há ofertas de planos de conexão para uso individual a partir de R$79,90 mensais. O plano escolhido tem custo de R$99,90 mensais e oferece 400MB [[3]](#ref3).

Há o gasto diário de energia, associado ao tempo que cada desenvolvedor irá gastar no projeto. A planilha leva como base a tarifa de R$0,57, representada na seção B1 - Residencial [deste documento](https://www.neoenergiabrasilia.com.br/residencial-e-rural/Documents/2022-04-tarifas-abril/Grupo-B.pdf) para cálculo do consumo [[4]](#ref4).

<p style="text-align: center; background-color: lightgray; margin: 2em;">custoServiços = (valorInternet X qtdMeses X qtdPessoas) + (valorEnergia X qtdHorasPessoas X qtdPessoas)</p>

### Custo com hospedagem na nuvem

Nesse projeto é necessario levar em conta o custo de publicação na nuvem. Foi pensado em valores base de hospedagem cobrada em Dólar americano e foi feita uma equivalência com a cotação do dia 28 de julho de 2022 para R$99,64 mensais.

<p style="text-align: center; background-color: lightgray; margin: 2em;">Custo hospedagem = (valorHospedagem X qtdMeses)</p>

## Planilha de Custos de Base
<iframe width="700" height="300" style="-webkit-transform:scale(0.8);-moz-transform:scale(0.8);" frameborder="0" scrolling="yes" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQukIJxgB9rI68ySzAPsyFXSLf-TOnjljPT126DsTgey6jvmTDPSt6SI3f2JQbID0QiFhQC6p8Hdioz/pubhtml"></iframe>

## Custo Total

Os custos acima são referentes unicamente aos gastos durante o semestre atual, sem considerar quaisquer gastos prévios com o projeto. Os dados abaixo visam ilustrar os valores estimados para o projeto, caso fosse, por exemplo, contratada uma empresa privada para desenvolver este software.

## Metodologia Utilizada

### Gerenciamento de Valor Agregado (EVM – Earned Value Management)

A Análise do Valor Agregado é um método de mensuração do desempenho desenvolvido pelo departamento de defesa dos EUA. Usado para estabelecer padrões de análise de contratos que considerassem não somente os custos e prazos mas também a performance e a eficiência do projeto [[1]](#ref1), [[5]](#ref5).

Ele usa algumas informações como:

1. Quantas Sprints ou Iterações tem o seu projeto ou release
2. Quantas Sprints ou Iterações foram concluídas até o momento
3. Qual o total de esforço para concluir o seu projeto ou release (seja em horas, seja em pontos ou outra métrica)
4. Qual o esforço concluído (Done) até o momento
5. Qual o orçamento do projeto ou release
6. Quanto foi gasto até o momento

Para isso temos alguns parametros para EVM, dentro do projeto e suas releases, para cada release tem também das sprints: 

#### Parâmetros EVM 

* BAC – Orçamento estimado para a Release, detalhado na tabela de custos
* AC = EV / BAC – Custo até o momento
* PV = BAC * (TSC / TSE) – Valor Planejado
* EV = BAC * (RPC / PRP) – Valor Agregado
* CPI = EV / AC – Índice de Desempenho de Custos
* CPV = EV - AC – Variação de Desempenho de Custo
* SPI = EV / PV – Índice de Desempenho de Prazo
* SPV = EV - PV – Variação de Desempenho de Prazo

#### Parâmetros Gerais do Projeto
* CPI – Índice de Desempenho de Custos
* SPI – Índice de Desempenho de Prazo
* CPV – Variação de Desempenho de Custo
* SPV – Variação de Desempenho de Prazo

#### Parâmetros das Releases

* PRP	– Pontos Planejados por Release
* RPC	– Pontos Concluídos por Release
* BAC	– Orçamento estimado por Release
* AC	– Custo até o momento
* PV	– Valor Planejado por Release
* EV	– Valor Agregado por Release

#### Parâmetros das Sprints

* PP	- Pontos Planejados por Sprint
* PC	- Pontos Concluídos por Sprint
* PI	- Pontos Incompletos por Sprint
* AP	- Pontos Adicionados por Sprint
* SC	- Orçamento gasto por Sprint
* TSC	- Total de Sprints Concluídas
* TSE	- Total de Sprints Estimadas

### Planilha EVM
<iframe width="700" height="300" style="-webkit-transform:scale(0.8);-moz-transform:scale(0.8);" frameborder="0" scrolling="yes" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQRhanQHg-5c_-EcjrciTQnGJkHgv3BZQZGXix11V6Rjmr7e4C9-IT84_H7ctLwXFOiciw6j1ZAHexT/pubhtml"></iframe>

## Referências 

<a id="ref1"></a>
[1] Hiflex consultoria. Gerenciamento De Valor Agregado (EVM) Em Projetos Ágeis. Acesso em Jul. 2022. Disponível em: <https://hiflexconsultoria.com.br/gerenciamento-de-valor-agregado-evm-em-projetos-ageis/>

<a id="ref2"></a>
[2] Infográfico O Globo: Ranking do custo anual por aluno nas federais (2016). Acesso em Jul. 2022. Disponível em: [https://infograficos.oglobo.globo.com/brasil/raio-x-do-custo-por-aluno-nas-universidades-federais.html]( https://infograficos.oglobo.globo.com/brasil/raio-x-do-custo-por-aluno-nas-universidades-federais.html)


<a id="ref3"></a>
[3] Planos de Internet em Brasília. Acesso em Jul. 2022. Disponível em: [https://podecomparar.com.br/telecom/internet](https://podecomparar.com.br/telecom/internet)


<a id="ref4"></a>
[4] Tabela de Tarifas de Energia Elétrica. Acesso em Jul. 2022. Disponível em: [https://www.neoenergiabrasilia.com.br/residencial-e-rural/Documents/2022-04-tarifas-abril/Grupo-B.pdf](https://www.neoenergiabrasilia.com.br/residencial-e-rural/Documents/2022-04-tarifas-abril/Grupo-B.pdf)

<a id="ref5"></a>
[5] VEC. Análise de Valor Agregado (EVM) em Projetos: Conheça e aprenda a calcular. Acesso em Jul. 2022. Disponível em: <http://valorecompetencia.com.br/gestao_de_projetos/analise-de-valor-agregado-evm-em-projetos-conheca-e-aprenda-a-calcular>

| Versão | Data       | Descrição | Autores |
| ------ | ---------- | --------- | ------- |
| 0.1    | 11/07/2022 | Abertura do documento | Ana Hoffmann e Marcelo |
| 0.2    | 16/07/2022 | Adição de planilha dinâmica | Marcelo |
| 0.3    | 22/07/2022 | Adição de descrições e melhorias | Ana Hoffmann |
| 0.4    | 28/07/2022 | Adição de custo de hospedagem | Giovanna |
| 0.5    | 28/07/2022 | Adição de EVM | Giovanna |
| 0.6    | 28/07/2022 | Retira inglês de EVM | Giovanna |
| 0.7    | 28/07/2022 | Adiciona planilha EVM | Giovanna e Marcelo |