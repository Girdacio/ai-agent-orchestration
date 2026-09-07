---
name: hello-wrld
description: Verifica se o projeto tem um hello world funcional. Para projetos web, garante um endpoint simples; para projetos não web, cria uma classe Main com método hello_world e um teste unitário. Keywords: hello world, endpoint, web, unit test, bootstrap, scaffold.
---

# Skill: hello-wrld

Use esta skill quando o projeto atual ainda não tiver uma implementação mínima de hello world e for necessário garantir um ponto de entrada verificável por teste.

## Objetivo

A skill deve:

1. Inspecionar o projeto atual para identificar se ele é um projeto web ou não web.
2. Se for web, confirmar se há um endpoint de hello world funcionando; se não houver, criar um endpoint mínimo.
3. Se não for web, confirmar se há uma classe `Main` com método `hello_world`; se não houver, criar a classe mínima.
4. Garantir que exista pelo menos um teste unitário executando esse hello world.
5. Executar o teste e corrigir qualquer falha antes de concluir.

## Regras

- Web project: procure frameworks como Flask, FastAPI, Django, Express, Spring, ASP.NET, etc.
- Se for web, use um endpoint simples como `/hello`, `/`, ou `/hello-world` que retorne a string `Hello, World!`.
- Se não for web, use a forma mínima em Python:

```python
class Main:
    def hello_world(self):
        return "Hello, World!"
```

- O teste unitário deve chamar esse método ou o endpoint e validar a resposta exata.
- Se não existir nenhum hello world, a skill deve criar os arquivos necessários em vez de apenas reportar o problema.
- Preserve a estrutura do projeto existente; adicione o mínimo possível.

## Fluxo recomendado

### 1) Detectar o tipo do projeto

- Verificar `package.json`, `requirements.txt`, `pyproject.toml`, `pom.xml`, `build.gradle`, arquivos de framework web, ou código com rotas.
- Se houver indicadores de framework web, tratar como web.
- Caso contrário, tratar como não web.

### 2) Verificar a implementação existente

- Web: procurar rota ou função equivalente a `hello`, `hello_world`, `@app.route('/hello')`, `@app.get('/hello')`, `router.get('/hello')`, etc.
- Não web: procurar `class Main` ou `def hello_world` em arquivos como `main.py`, `app.py`, `server.py`, `src/...`.

### 3) Criar o mínimo necessário

#### Projeto web

```python
from flask import Flask

app = Flask(__name__)

@app.get("/hello")
def hello():
    return "Hello, World!"
```

#### Projeto não web

```python
class Main:
    def hello_world(self):
        return "Hello, World!"


if __name__ == "__main__":
    print(Main().hello_world())
```

### 4) Garantir o teste

```python
import unittest

from main import Main


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(Main().hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
```

### 5) Validar

- Rodar o comando de testes unitários do projeto.
- Se falhar, corrigir imediatamente até obter sucesso.
- Concluir apenas quando houver pelo menos um teste que execute o hello world e passe.

## Exemplo de execução

Se o projeto for Python simples, a skill deve criar algo como:

- `main.py` com a classe `Main` e o método `hello_world`
- `test_hello_world.py` com um `unittest` válido
- Executar `python -m unittest -v`

Se o projeto for web, a skill deve criar um endpoint mínimo e, idealmente, um teste que acesse esse endpoint em vez de chamar um método interno.

## Critério de aceitação

A skill está completa quando:

- existe um hello world funcional;
- o projeto tem pelo menos um teste unitário cobrindo esse hello world;
- o teste passa ao ser executado.