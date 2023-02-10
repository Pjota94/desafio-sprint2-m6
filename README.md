# Desafio Python Sprint 2

Essa aplicação consiste em tratar dados CNAB e envia-los para um banco de dados PostgreSQL. Ao abrir a aplicação, você poderá selecionar um arquivo CNAB em formato .txt e enviar, ao enviar os dados serão salvos no banco de dados.

### O que é CNAB?

O CNAB (Centro Nacional de Automação Bancária) é uma ferramenta padrão da FEBRABAN (Federação Brasileira de Bancos). Ela é utilizada tanto para a remessa quanto para o retorno de informações sobre clientes para as empresas que utilizam este tipo de serviço.

# Instruções de instalação e execução

```bash

    # 1º Faça o Clone deste repositorio
    $ git clone git@github.com:Pjota94/desafio-sprint2-m6.git

    # 2º Instale o venv
    $ python -m venv venv

    # 3º Faça a ativação do venv
    $ source venv/bin/activate

    # 4º Instale os pacotes necessários para o projeto
    $ pip install -r requirements.txt

    # 5º Faça uma copia do arquivo .env.example e renomeie para apenas .env, preencha os dados de acordo com os dados do seu banco.

    # 6º Execute a migração
    $ python manage.py migrate

    # 7º Rode o servidor
    $ python manage.py runserver

    # 8º Abra o navegador e acesse o endereço abaixo
    http://127.0.0.1:8000/

```

| 🛠 Tecnologias Utilizadas |
| ------------------------ |
| Python                   |
| Django Rest-FrameWork    |
| PostgreSQL               |
