from webScraper import WebScraper
from game import Game

def game_round():
  first_page = WebScraper.get_random_page()
  target_page = WebScraper.get_ending_page()

  game = Game(first_page, target_page)

  while(game.won == False):
    pass
    # pega o título da página e printa
    # armazena o título nas páginas passadas
    # pega os links da página em uma lista e printa eles
    
    # usuário escolhe uma próximo página
      # confere se é o objetivo
        # se sim, vai pra função de finalizar jogo
        # se não, vai para a próxima iteração
    # usuário pode desistir -> chama função de finalizar

  game.end_game()


def main():
  while True:
    print("Welcome to the wikipedia game?\n" \
    "What do ou want to do?\n" \
    "1 - see ranking\n" \
    "2 - play new game\n" \
    "3 - exit\n")

    user_action = input()
    
  # mensagem de boas vindas
  # ver histórico
  # novo jogo

def testes():
  print("au")
  WebScraper.get_title("a")

if __name__ == "__main__":
  testes()