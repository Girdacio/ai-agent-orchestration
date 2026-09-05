class FatorRecuperacao:
    @staticmethod
    def calcular(perda: float) -> float:
        """Retorna o ganho necessário para recuperar uma perda percentual.

        A perda deve ser informada em formato decimal (ex.: 20% -> 0.20).
        Se um percentual inteiro for informado (ex.: 20), ele será convertido
        automaticamente para decimal.
        """
        if perda < 0:
            raise ValueError("A perda não pode ser negativa.")

        if perda > 1:
            if perda <= 100:
                perda = perda / 100
            else:
                raise ValueError("A perda deve estar entre 0 e 1 (decimal) ou entre 0 e 100 (percentual).")

        if perda >= 1:
            raise ValueError("Uma perda de 100% ou mais não pode ser recuperada.")

        return perda / (1 - perda)


class Main:
    def hello_world(self):
        return "Hello, World!"

    def fator_de_recuperacao(self, perda: float) -> float:
        return FatorRecuperacao.calcular(perda)


if __name__ == "__main__":
    print(Main().hello_world())
    print(FatorRecuperacao.calcular(0.33))
