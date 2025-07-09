# ETL de Artistas com Python e PostgreSQL

Este é um projeto de pipeline **ETL (Extract, Transform, Load)** desenvolvido com **Python 3.12**. Ele realiza scraping de uma página com listas de artistas, transforma os dados extraídos e os insere em um banco de dados **PostgreSQL**.

Projeto feito durante as aulas da playlist [Scrapper Python: ETL Pipeline](https://www.youtube.com/playlist?list=PLAgbpJQADBGLuI1oR39tVfELOEZJSSbxQ) do [Programador Lhama](https://github.com/programadorLhama), adaptado para uso com PostgreSQL e `psycopg3`.

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Preparando o Banco de Dados](#preparando-o-banco-de-dados)
- [Configure o .env](#configure-o-env)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
  - [Opção 1: Usando uv](#opção-1-usando-uv)
  - [Opção 2: Usando venv tradicional + pip](#opção-2-usando-venv-tradicional--pip)

## Tecnologias Utilizadas

- Python 3.12  
- psycopg3  
- Requests  
- BeautifulSoup4  
- python-dotenv  
- pylint
- pytest
- [uv](https://docs.astral.sh/uv/) (opcional, como gerenciador de ambiente e pacotes)

## Preparando o Banco de Dados

Antes de rodar a pipeline, você precisa criar a tabela no seu banco PostgreSQL.
Para isso, utilize o arquivo `db.sql`, que contém os comandos necessários.

**Atenção**: não execute o arquivo diretamente, pois isso pode criar a tabela no banco errado. Em vez disso:

1. Acesse seu banco de dados destino (ex: pipeline_db) via terminal ou interface gráfica (como DBeaver ou pgAdmin).

2. Copie o conteúdo do arquivo db.sql.

3. Cole e execute dentro da sessão conectada ao banco correto.

## Configure o .env

Crie um arquivo .env na raiz do projeto com as credenciais do banco:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pipeline_db
DB_USER=postgres
DB_PASSWORD=sua_senha
```

## Como Rodar o Projeto

Você pode executar este projeto de duas formas: com **uv** ou com o **Python tradicional**.

### Opção 1: Usando `uv`

```bash
uv venv
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows
uv sync --all-groups
python main.py
```
### Opção 2: Usando venv tradicional + pip

```bash
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows
pip install -r requirements.txt  # ou use pip-tools para converter o pyproject
python main.py
```
