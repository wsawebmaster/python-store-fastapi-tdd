# 📂 Desenvolvendo uma API com FastAPI utilizando TDD

## 📃 Descrição

Neste projeto, iremos desenvolver uma API com FastAPI utilizando o Test-Driven Development (Desenvolvimento Guiado por Testes ou simplesmente TDD) que é uma metodologia que prioriza a criação de testes antes do código, vamos entender como criar tests com o `pytest`. Construindo testes de Schemas, Usecases e Controllers (teste de integração).

## 🚀 Tecnologias Utilizadas

- Python
- TDD com FastAPI + Pytest;
- Docker
- Pydantic
- Pyenv + Poetry
- Make
- MongoDB
- Git e Github

## Ciclo do TDD
![TDD](/docs/img/tdd.webp "Desenvolvimento Guiado por Testes")

O TDD segue um ciclo de três etapas principais, conhecido como Red-Green-Refactor:

1 - Red (Vermelho - Escrever o teste)

- Escreva um teste unitário para a funcionalidade desejada.
- Execute o teste e verifique que ele falha (já que o código ainda não foi implementado).

2 - Green (Verde - Fazer o teste passar)

- Implemente o código mínimo necessário para que o teste passe.
- Execute os testes novamente e verifique que o código está funcionando.

3 - Refactor (Refatoração)

- Refatore o código para melhorar sua estrutura e qualidade sem alterar sua funcionalidade.
- Execute os testes novamente para garantir que tudo ainda funciona corretamente.

Esse ciclo é repetido continuamente durante o desenvolvimento.

### Arquitetura
|![C4](/docs/img/store.drawio.png)|
|:--:|
| Diagrama de C4 da Store API |

### Banco de dados - MongoDB
|![C4](/docs/img/product.drawio.png)|
|:--:|
| Database - Store API |

## Preparar ambiente

Vamos utilizar Pyenv + Poetry, link de como preparar o ambiente abaixo:

[poetry-documentation](https://github.com/nayannanara/poetry-documentation/blob/master/poetry-documentation.md)

[oficial](hhttps://python-poetry.org/docs/)

### Subir Container do Projeto

    docker-compose up -d

### Remover todos os contêineres, redes e volumes definidos no arquivo docker-compose.yml

    docker-compose down

### Remover contêineres, imagens e limpar redes não utilizadas.

    [ "$(docker ps -q)" ] && docker stop $(docker ps -q); [ "$(docker ps -aq)" ] && docker rm $(docker ps -aq); [ "$(docker images -q)" ] && docker rmi $(docker images -q); docker network prune -f

## Links uteis de documentação
[mermaid](https://mermaid.js.org/)

[pydantic](https://docs.pydantic.dev/dev/)

[validatores-pydantic](https://docs.pydantic.dev/latest/concepts/validators/)

[model-serializer](https://docs.pydantic.dev/dev/api/functional_serializers/#pydantic.functional_serializers.model_serializer)

[mongo-motor](https://motor.readthedocs.io/en/stable/)

[pytest](https://docs.pytest.org/en/7.4.x/)

---
---

### 📧 Contato

[LinkedIn](https://www.linkedin.com/in/wsawebmaster/)

[wsawebmaster@yahoo.com.br](mailto:wsawebmaster@yahoo.com.br)
