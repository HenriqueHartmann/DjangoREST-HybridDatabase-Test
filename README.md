# DjangoREST-HybridDatabase-Test

Sistema de submissões utilizando PostgreSQL e MongoDB

<h2>BACKEND</h2>

Requisitos:

<ul>
    <li><a href="https://docs.docker.com/engine/install/ubuntu/">Docker</a></li>
    <li><a href="https://docs.docker.com/compose/install/">Docker-Compose</a></li>
    <li><a href="https://python-poetry.org/docs/">Poetry</a></li>
</ul>

```
# Configurações (editar se necessário)
cp .env.sample .env

# Inicializar o banco de dados(OBS: crie o banco no postgres manualmente)
sudo docker-compose up -d

# Instalar as dependências
poetry install

# Para inicializar a aplicação
./manage.py runserver
```

<h2>TEARDOWN</h2>

```
# Parar o banco de dados
sudo docker-compose down
```
