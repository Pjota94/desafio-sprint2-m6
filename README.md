# Desafio Python Sprint 2

Essa aplicação consiste em tratar dados CNAB e envia-los para um banco de dados PostgreSQL. Ao abrir a aplicação, você poderá selecionar um arquivo CNAB em formato .txt e enviar, ao enviar os dados serão salvos no banco de dados.

### O que é CNAB?

O CNAB (Centro Nacional de Automação Bancária) é uma ferramenta padrão da FEBRABAN (Federação Brasileira de Bancos). Ela é utilizada tanto para a remessa quanto para o retorno de informações sobre clientes para as empresas que utilizam este tipo de serviço.

# Instruções de instalação e execução

```bash

    # 1º Instale o venv
    $ python -m venv venv

    # 2º Faça a ativação do venv
    $ source venv/bin/activate

    # 3º Instale os pacotes necessários para o projeto
    $ pip install -r requirements.txt

    # 4º Execute a migração
    $ python manage.py migrate

    # 5º Rode o servidor
    $ python manage.py runserver

    # 6º Abra o navegador e acesse o endereço abaixo
    http://127.0.0.1:8000/

```

| 🛠 Tecnologias Utilizadas |
| ------------------------ |
| Python                   |
| Django Rest-FrameWork    |
| PostgreSQL               |
