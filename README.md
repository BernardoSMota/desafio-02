# Sistema de Funcionários

Um sistema web feito com Django para cadastro, edição e listagem de funcionários.

## Funcionalidades

- Cadastro de profissionais (nome, telefone, e-mail, cidade)
- Listagem dos profissionais cadastrados
- Edição dos dados de um profissional
- Exclusão de registros

## Tecnologias utilizadas

- Python
- Django
- HTML5, CSS3

## Como rodar localmente

1. Clone o projeto:
   ```
   git clone https://github.com/BernardoSMota/desafio-02.git
   ```

2. Crie o ambiente virtual:
   ```
   python -m venv venv
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações e o servidor:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

5. Acesse: http://localhost:8000

## Observações

- Certifique-se de ter o Python 3.8+ instalado.
- Crie um arquivo `.env` se usar variáveis de ambiente sensíveis.
- O banco de dados padrão é SQLite (db.sqlite3).
