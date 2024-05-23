class Pergunta:
    def __init__(self, pergunta, opcoes, resposta):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta = resposta

    def exibir(self):
        print(f'Pergunta: {self.pergunta}\n')
        for i, opcao in enumerate(self.opcoes):
            print(f'{i}) {opcao}')
        print()

    def checar_resposta(self, escolha):
        if escolha.isdigit():
            escolha_int = int(escolha)
            if 0 <= escolha_int < len(self.opcoes):
                return self.opcoes[escolha_int] == self.resposta
        return False


class Quiz:
    def __init__(self, perguntas):
        self.perguntas = [Pergunta(**pergunta) for pergunta in perguntas]
        self.qtd_acertos = 0

    def executar(self):
        for pergunta in self.perguntas:
            pergunta.exibir()
            escolha = input('Escolha uma opção: ')
            if pergunta.checar_resposta(escolha):
                self.qtd_acertos += 1
                print('Acertou 👍')
            else:
                print('Errou ❌')
            print()

        self.exibir_resultado()

    def exibir_resultado(self):
        print(f'Você acertou {self.qtd_acertos} de {len(self.perguntas)} perguntas.')


def main():
    perguntas = [
        {
            'Pergunta': 'Quanto é 2+2?',
            'Opções': ['1', '3', '4', '5'],
            'Resposta': '4',
        },
        {
            'Pergunta': 'Quanto é 5*5?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': '25',
        },
        {
            'Pergunta': 'Quanto é 10/2?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': '5',
        },
    ]

    quiz = Quiz(perguntas)
    quiz.executar()


if __name__ == "__main__":
    main()
