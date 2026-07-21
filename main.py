from webScraper import WebScraper, notFound
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
      # se não tiver links, é gamewover
    
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
  url = 'https://en.wikipedia.org/wiki/The_BMJ'
  try:
    # print(WebScraper.get_title(url))
    pass
  except notFound as e:
    print(f"error! {e}")

  print(WebScraper.get_vital_articles())

if __name__ == "__main__":
  testes()