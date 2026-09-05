# IA

## Objetivo
Este projeto é uma implementação mínima em Python para demonstrar:
- um hello world funcional;
- a lógica de cálculo do fator de recuperação para determinar o ganho necessário para recuperar uma perda percentual.

## Tecnologias
- Python 3
- unittest

## Estrutura do projeto
- main.py: contém as classes `Main` e `FatorRecuperacao`.
- test_hello_world.py: valida o hello world e o cálculo do fator de recuperação.
- unit_test.py: exemplo adicional com testes de soma.

## Função de fator de recuperação
A classe `FatorRecuperacao` implementa o cálculo:

```python
ganho = perda / (1 - perda)
```

Ela recebe a perda em formato decimal, como `0.20` para 20%, e retorna o percentual necessário para recuperar o valor perdido, arredondado para 2 casas decimais.

## Serviços expostos
Este projeto não expõe endpoints HTTP REST; trata-se de um exemplo simples de aplicação Python não web.

## Dependências
- Nenhuma dependência externa declarada no projeto atual.

## Como rodar localmente
```bash
python main.py
```

Saída esperada:
```text
Hello, World!
0.33
```

## Como executar testes
```bash
python -m unittest -v
```

## Contribuidores
- girdacio

## Última atualização
- Branch: master
- Último commit: a59ffbb - 2026-09-05T14:20:36-03:00 - girdacio - função fator recuperação

## Observações
- O projeto está funcional e validado por testes unitários.
- A documentação reflete o código presente no diretório atual e o estado real do repositório Git.
