# Plano de Custos

| Versão | Data       | Descrição | Autores |
| ------ | ---------- | --------- | ------- |
| 1.0    | 11/07/2022 | Abertura do documento | Ana Hoffmann e Marcelo |
| 1.1    | 16/07/2022 | Adição de planilha dinâmica | Marcelo |
| 1.2    | 22/07/2022 | Adição de descrições e melhorias | Ana Hoffmann |

## Introdução

Esse documento foi criado com o objetivo de registrar as estimativas dos custos financeiros relacionados à realização do projeto PUMA no semestre 2022.1. Para sua montagem, foram utilizados dados disponíveis no Mural, no Zenhub e no backlog do produto, além de consultas a preços de produtos disponíveis em lojas virtuais e serviços ofertados em Brasília, DF.

Sabendo que os valores, especialmente de equipamentos, são variáveis e que uma estimativa depende de diversos fatores, o plano de custos poderá sofrer alterações ao longo do projeto. Tais mudanças terão sempre como objetivo ilustrar os custos com boa precisão e abrangência.

Por fim, note que não há estimativa de custos para publicação do produto e, nos gastos totais, não serão levados em consideração os gastos com equipamentos. Isso se deve ao fato de que o PUMA ainda não chegou em sua fase ideal para publicação, além de que os integrantes já possuíam seus próprios equipamentos para realizar o projeto.

## Custo com Pessoal

Considerando que a equipe é formada por 13 membros matriculados em Engenharia de Software na Universidade de Brasília, e utilizando informações presentes no inforgráfico disponibilizado em [O Globo](https://infograficos.oglobo.globo.com/brasil/raio-x-do-custo-por-aluno-nas-universidades-federais.html), têm-se que o custo por aluno em tal universidade, no ano de 2016, foi de R$ 38.805,00. Convertendo o valor anual para mensal e diário, têm-se, respectivamente, R$3.233,75 e R$104,31.

É importante destacar que a jornada de trabalho será de 30 horas semanais, ou seja, 5 horas diárias. Assim, o cálculo do custo total com os desenvolvedores será dado por:

<p style="text-align: center; background-color: lightgray; margin: 2em;">custoPessoal = valorHora X qtdDias X qtdPessoas</p>

## Custos com Equipamentos

Para o desenvolvimento do PUMA, é necessário que cada integrante da equipe possua equipamentos capazes de executar o projeto sem impedimentos. Também se faz necessário o uso de dispositivos de áudio de qualidade, visto que ocorrerão reuniões online recorrentes e é imprescindível um bom áudio para que a comunicação seja eficaz. Com isso em mente, cada desenvolvedor deverá possuir um notebook e um headset, sendo outros periféricos opcionais para aquisição.

As configurações recomendadas de hardware para este projeto são: i5 de 10a geração ou posterior, 16gb de RAM e armazenamento SSD.

<p style="text-align: center; background-color: lightgray; margin: 2em;">custoEquipamento = (valorFone X qtd) + (valorNotebook X qtd)</p>

## Custo com Serviços

O desenvolvimento do projeto exige conexão estável com a internet, sendo, portanto, recomendada a contratação de um pacote de internet por operadora. Há ofertas de planos de conexão para uso individual a partir de R$79,90 mensais. O plano escolhido tem custo de R$99,90 mensais e oferece 400MB.

Há o gasto diário de energia, associado ao tempo que cada desenvolvedor irá gastar no projeto. A planilha leva como base a tarifa de R$0,57, representada na seção B1 - Residencial [deste documento](https://www.neoenergiabrasilia.com.br/residencial-e-rural/Documents/2022-04-tarifas-abril/Grupo-B.pdf) para cálculo do consumo.

<p style="text-align: center; background-color: lightgray; margin: 2em;">custoServiços = (valorInternet X qtdMeses X qtdPessoas) + (valorEnergia X qtdHorasPessoas X qtdPessoas)</p>

## Planilha de Custos de Base
<iframe width="700" height="300" style="-webkit-transform:scale(0.8);-moz-transform:scale(0.8);" frameborder="0" scrolling="yes" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vR-uoHT7nQ1_pbrrsAzkZMbWH6IKPO05uSthJbX1kUIjEyupD0MX2sOnP8ApCiUyqlwJE7tpYc42EZ0/pubhtml"></iframe>

## Custo Total

Os custos acima são referentes unicamente aos gastos durante o semestre atual, sem considerar quaisquer gastos prévios com o projeto. Os dados abaixo visam ilustrar os valores estimados para o projeto, caso fosse, por exemplo, contratada uma empresa privada para desenvolver este software.

## Metodologia Utilizada

## Planilha de Custo do Produto

<!-- <iframe width="700" height="300" style="-webkit-transform:scale(0.8);-moz-transform:scale(0.8);" frameborder="0" scrolling="yes" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTC4ZzWCCuY3Tg95AruukpsHFe1irj-x9_wWBihO6ZthOh03CDklZQdLr1fzqwAXxCEQq813CU9y58w/pubhtml"></iframe> -->

## Referências

Planos de Internet em Brasília. Acesso em Jul. 2022. Disponível em: [https://podecomparar.com.br/telecom/internet](https://podecomparar.com.br/telecom/internet)

Infográfico O Globo: Ranking do custo anual por aluno nas federais (2016). Acesso em Jul. 2022. Disponível em: [https://infograficos.oglobo.globo.com/brasil/raio-x-do-custo-por-aluno-nas-universidades-federais.html]( https://infograficos.oglobo.globo.com/brasil/raio-x-do-custo-por-aluno-nas-universidades-federais.html)

Tabela de Tarifas de Energia Elétrica. Acesso em Jul. 2022. Disponível em: [https://www.neoenergiabrasilia.com.br/residencial-e-rural/Documents/2022-04-tarifas-abril/Grupo-B.pdf](https://www.neoenergiabrasilia.com.br/residencial-e-rural/Documents/2022-04-tarifas-abril/Grupo-B.pdf)
