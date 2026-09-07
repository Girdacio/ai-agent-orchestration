---
name: readme-updater
description: Lê o projeto atual, detecta mudanças importantes na estrutura, bibliotecas, endpoints e infraestrutura, e atualiza ou cria o README.md com informações confiáveis sobre objetivo, tecnologias, serviços expostos, dependências, execução local, testes, contribuidores e última atualização do Git. Keywords: README, documentation, project scan, dependencies, endpoints, run locally, tests, git, changelog.
---

# Skill: readme-updater

Use esta skill sempre que houver uma mudança relevante no projeto que afete a documentação: nova estrutura, adição/remoção de biblioteca, mudança de tecnologia, ajuste de endpoint, alteração de ambiente de execução, ou qualquer modificação que mude como o projeto é usado.

## Objetivo

A skill deve:

1. Ler o projeto atual e identificar seu tipo, estrutura e tecnologias.
2. Detectar se houve mudança relevante em relação ao README existente.
3. Atualizar ou criar o README.md com base no estado real do repositório.
4. Documentar nome, objetivo, tecnologias, serviços expostos, dependências, execução local, testes e contribuidores.
5. Coletar informações do Git quando disponíveis: branch ativa, última alteração, autor e data.
6. Garantir que a documentação reflita exatamente o que está no código.

## Quando rodar

Execute esta skill quando qualquer uma destas condições acontecer:

- criação ou remoção de arquivos importantes;
- adição ou remoção de bibliotecas/dependências;
- alteração de endpoints HTTP REST;
- mudança de framework ou arquitetura;
- mudança no processo de execução local;
- alteração em scripts de setup/testes;
- criação de novo serviço, API, CLI, job ou worker;
- qualquer modificação que altere o comportamento documentado.

Se não houver README.md, a skill deve criá-lo. Se ele existir, deve atualizar apenas o que mudou e preservar os blocos estáticos relevantes.

## Regras de análise

### 1) Identificar o nome e objetivo do projeto

- Observar a pasta raiz, nomes de arquivos e descrição do domínio do código.
- Para projetos Python: verificar `pyproject.toml`, `requirements.txt`, `setup.cfg`, `setup.py`, `main.py`, etc.
- Para projetos Node: verificar `package.json` e scripts.
- Para projetos Java: verificar `pom.xml`, `build.gradle`, `settings.gradle`.
- O objetivo deve ser descrito em linguagem clara e curta.

### 2) Identificar tecnologias e dependências

- Ler arquivos de configuração e importações relevantes.
- Detectar:
  - linguagem principal;
  - frameworks web/utilizados;
  - bibliotecas; 
  - versões relevantes quando disponíveis.
- Registrar dependências externas e internas em seção própria.

### 3) Identificar serviços expostos

- Para aplicações web, procurar rotas/endpoints em arquivos como `app.py`, `routes.py`, `api.py`, `server.py`, controllers e arquivos de framework.
- Documentar endpoints HTTP REST no formato:

```
GET /hello -> retorna "Hello, World!"
```

- Quando não houver aplicação web, indicar que o projeto não expõe endpoints HTTP e documentar a natureza da execução local.

### 4) Identificar como rodar localmente

- Procurar `README`, scripts de inicialização, `makefile`, `docker-compose`, `requirements`, `package.json`, `pyproject.toml`, `.env.example`.
- Registrar os passos reais:
  - instalação de dependências;
  - comando de execução;
  - variáveis de ambiente se existirem.

### 5) Identificar como executar testes

- Buscar `pytest`, `unittest`, `vitest`, `jest`, `mvn test`, `gradlew test`, etc.
- Documentar o comando mínimo necessário para validar o projeto.

### 6) Identificar contribuidores

- Tentar ler dados do Git:
  - autores dos commits recentes;
  - branch atual;
  - última alteração e data.
- Se não for um repositório Git, indicar "Contribuidores: não informado".

### 7) Identificar última atualização do projeto

- Se o diretório estiver em Git, usar:

```bash
git branch --show-current
git --no-pager log -1 --date=iso-strict --pretty=format:'%h %ad %an %s'
```

- Se não houver Git, registrar:
  - "Controle de versão: não disponível neste ambiente."
  - ou "Última atualização: não disponível."

## Saída esperada

O README deve conter, no mínimo:

1. Título do projeto
2. Descrição objetiva
3. Tecnologias utilizadas
4. Estrutura principal do projeto
5. Serviços expostos (endpoints) se houver
6. Dependências
7. Como rodar localmente
8. Como executar testes
9. Contribuidores
10. Última atualização / info de Git

## Formato sugerido

```md
# Nome do Projeto

## Objetivo
Breve descrição do que o projeto faz.

## Tecnologias
- Python 3.11
- Flask
- unittest

## Estrutura do projeto
- main.py
- test_hello_world.py

## Serviços expostos
| Método | Endpoint | Descrição |
| --- | --- | --- |
| GET | /hello | Retorna "Hello, World!" |

## Dependências
- Flask
- pytest

## Como rodar localmente
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Como executar testes
```bash
python -m unittest -v
```

## Contribuidores
- Nome do autor do último commit, se disponível

## Última atualização
- Branch: main
- Último commit: abc1234 - 2026-09-05T12:00:00+00:00 - Nome do autor
```

## Critério de aceitação

A skill está completa quando:

- o README existe ou foi atualizado;
- ele reflete a estrutura real do projeto;
- tecnologias, dependências, execução e testes estão documentados;
- endpoints e serviços expostos são listados quando existirem;
- informações do Git foram usadas quando disponíveis;
- o arquivo final é coerente com o estado atual do código.

## Observações importantes

- Não inventar tecnologias, endpoints ou dependências inexistentes.
- Priorizar evidência direta do código e dos arquivos de configuração.
- Se as informações do Git não estiverem disponíveis, deixar explícito no README e não inventar dados.
- Sempre que houver mudança material no projeto, rodar esta skill para revalidar a documentação.