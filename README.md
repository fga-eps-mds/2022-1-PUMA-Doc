# 2022-1-PUMA-Doc

**Código da Disciplina:** FGA0138
**Time:** Time 03

## Sobre

O PUMA é um projeto que tem por objetivo auxiliar os professores no gerenciamento das disciplinas da
Engenharia de Produção da Universidade de Brasilia.

## Time

| Disciplina  | Matrícula | Nome                              | Github                                                  |
| ----------- | --------- | --------------------------------- | ------------------------------------------------------- |
| EPS         | 160124581 | Hugo Aragão de Oliveira           | [codehg](https://github.com/codehg)                     |
| EPS         | 160119006 | Enzo Gabriel                      | [enzoggqs](https://github.com/enzoggqs)                 |
| EPS         | 160114705 | Bruno Alves Félix                 | [bruno-felix](https://github.com/bruno-felix)           |
| EPS         | 170011267 | Giovanna Borges Bottino           | [giovannabbottino](https://github.com/giovannabbottino) |
| EPS         | 160035481 | Marcelo Araújo dos Santos         | [santosm46](https://github.com/santosm46)               |
| MDS         | 202015984 | Breno Henrique de Souza           | [bhsouza](https://github.com/bhsouza)                   |
| MDS         | 190059001 | Samuel Victor Oliveira Lima       | [samuelvictorol](https://github.com/samuelvictorol)     |
| MDS         | 180014412 | Cainã Valença de Freitas          | [freitasc](https://github.com/freitasc)                 |
| MDS         | 202042927 | Eduardo Schuindt Santos           | [edudsan](https://github.com/edudsan)                   |
| MDS         | 200018001 | Gabriel da Silva Cabral           | [GabriellCabrall](https://github.com/GabriellCabrall)   |
| MDS         | 202015901 | Ana Luiza Hoffmann Ferreira       | [AnHoff](https://github.com/AnHoff)                     |
| MDS         | 180098683 | Breno Yuri Barbosa Gomes          | [YuriBre](https://github.com/YuriBre)                   |
| MDS         | 190086971 | Felipe Direito Corrieri de Macedo | [FelipeDireito](https://github.com/FelipeDireito)       |

## Repositórios 

- [Notify Service](https://github.com/fga-eps-mds/2022-1-PUMA-NotifyService)
- [Alocate Service](https://github.com/fga-eps-mds/2022-1-PUMA-AlocateService)
- [Deploy](https://github.com/fga-eps-mds/2022-1-PUMA-Deploy)
- [API Gateway](https://github.com/fga-eps-mds/2022-1-PUMA-ApiGateway)
- [Project Service](https://github.com/fga-eps-mds/2022-1-PUMA-ProjectService)
- [User Service](https://github.com/fga-eps-mds/2022-1-PUMA-UserService)
- [Frontend](https://github.com/fga-eps-mds/2022-1-PUMA-Frontend)
## Como Rodar o Projeto
---

### GitHub Pages - Desenvolvimento Local

**Dependências**

Virtualenv: 
```pip3 install virtualenv```

**Preparando Ambiente e Subindo Servidor**

No diretório raiz do repositório, crie o ambiente: 
```python3 -m venv env```

Ative o ambiente: 
```source env/bin/activate```

Instale o Material mkdocs: 
```pip3 install mkdocs-material```

Inicie o servidor de desenvolvimento:
```mkdocs serve```

### PUMA - Desenvolvimento Local

1. Crie uma pasta para armazenar os repositórios do projeto.

2. Insira os scripts dentro da pasta criada.

3. Insira a pasta env dentro da pasta criada.

4. Recupere o IP da sua máquina(ifconfig) e insira nas variáveis de IP dos .envs que estão dentro da pasta envs.

5. Entre na pasta criada a partir do terminal.

6. Clone os repositórios do projeto:
   - Via ssh:
      ```source clone_repos_ssh.sh```
   - Via http:
      ```source clone_repos_http.sh```
        
7. Utilize o script move_envs.sh para mover todos os .envs para os seus respectivos repositórios.
   ```source move_envs.sh```
    


8. Entre no repositório Api-Gateway e execute:
   ```make up-build```
    
9. Após subir todos os containers com make up-build, abra outro terminal na pasta criada na etapa 1 e popule o banco de dados da aplicação:
   ```source db_script.sh populate```
    


10. Pronto ! Agora é só acessar http://localhost:8080/