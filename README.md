# 📂 Desenvolvendo API com FastAPI, Python e Docker

## 📃 Descrição

Neste projeto, iremos desenvolver uma poderosa API assíncrona para uma academia, focada em uma competição de Crossfit. Essa experiência nos ajudará a entender e lidar com operações simultâneas de maneira eficaz e escalável.

## 🚀 Tecnologias Utilizadas

- Python
- FastAPI
- Alembic
- Docker
- SQLAlchemy
- Pydantic
- PostgreSQL
- Git e Github

## Modelagem de entidade e relacionamento - MER
![MER](/mer.jpg "Modelagem de entidade e relacionamento")

### Subir Containers do Projeto

    docker-compose up -d

### Acessar
API: [http://localhost:8000/docs](http://localhost:8000/docs)<br /><br />


Acessar o container python
```sh
# Acessar o container
docker-compose exec python bash

# 1. Limpar migrações existentes (se necessário)
rm -rf alembic/versions/*

# 2. Criar migração inicial
PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "init_db"

# 3. Aplicar migração
PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

# 4. Verificar tabelas criadas
psql -U workout -d workout -h db -c "\dt"

# 5. Verificar estrutura das tabelas
psql -U workout -d workout -h db -c "\d atletas"
psql -U workout -d workout -h db -c "\d categorias"
psql -U workout -d workout -h db -c "\d centros_treinamento"
```

### 🔍 Troubleshooting

Se encontrar o erro "Can't locate revision":
```bash
# Remover migrações antigas
rm -rf alembic/versions/*

# Recriar migrations do zero
PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "init_db"
PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

```

### Atualizar o conteúdo do requirements.txt

    pip freeze > requirements.txt

### Instalar todas dependências

    pip install -r requirements.txt

### Remover todos os contêineres, redes e volumes definidos no arquivo docker-compose.yml

    docker-compose down

### Remover contêineres, imagens e limpar redes não utilizadas.

    [ "$(docker ps -q)" ] && docker stop $(docker ps -q); [ "$(docker ps -aq)" ] && docker rm $(docker ps -aq); [ "$(docker images -q)" ] && docker rmi $(docker images -q); docker network prune -f

# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/

---
---

### 📧 Contato

[LinkedIn](https://www.linkedin.com/in/wsawebmaster/)

[wsawebmaster@yahoo.com.br](mailto:wsawebmaster@yahoo.com.br)
