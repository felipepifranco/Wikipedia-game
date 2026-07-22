from webScraper import WebScraper, notFound
from game import Game
from utils import *

def game_round():
  first_page = WebScraper.get_random_page()
  first_page_title = WebScraper.get_title(first_page)
  target_page = WebScraper.get_ending_page()
  target_page_title = WebScraper.get_title(target_page)

  game = Game(first_page, first_page_title, target_page, target_page_title)
  game_ended = False

  while(game_ended == False):
    # round set up
    current_page = WebScraper.get_title_and_links(game.current_url)

    prSeparator()
    prPageName(f"Target: {game.target_name}")
    prWarning(f"Round {game.round}")
    prWarning("Current page:")

    # title print
    prPageName(current_page["title"])
    
    # links print
    prWarning("\nLinks in it:")

    has_ended, last_index = Game.print_pages_end(current_page["links"])
    
    if last_index == -1:
      prError("You've reach a page that has no links! Game over!")
      break
    
    # user input
    print("\n Chose a number to go to that page.\n" \
    "('exit' to give up, 'history' to see all pages visited)")
    while True:
      user_action = input()

      if user_action == 'exit':
        game_ended = True
        break

      elif user_action == 'history':
        game.show_history()
        print()
        input("press enter to continue\n")
        break

      elif user_action == '+' and has_ended == False:
        Game.print_pages_end(current_page["links"], last_index)
        break

      else:
        try:
          user_action = int(user_action)
          if user_action <= 0: raise IndexError
          next_page = current_page["links"][user_action -1]
          game.register_page(next_page)
          break
        except ValueError:
          print("Invalid input! Choose a number or a special command!")
        except IndexError:
          print("invalid number! Choose one in range")

  game.end_game()


def main():
  prWelcome("Welcome to the wikipedia game!") 
  while True:
    print("What do ou want to do?\n" \
    "1 - see ranking\n" \
    "2 - see game rules\n" \
    "3 - play new game\n" \
    "4 - exit")

    user_action = input()
    match user_action:
      case "1":
        pass
      case "2":
        pass
      case "3":
        game_round()
      case "4":
        break
      case _:
        prError("Invalid option! Choose again")
  
  
  prSeparator()
  print("Thank you for playing!\n")

def testes():
  url = 'https://en.wikipedia.org/wiki/The_BMJ'
  try:
    # print(WebScraper.get_title(url))
    pass
  except notFound as e:
    print(f"error! {e}")

  print(WebScraper.get_vital_articles())

def testes():
  url = "https://en.wikipedia.org/wiki/ABN_(TV_station)"
  info = WebScraper.get_title_and_links(url)
  print(info["links"])


if __name__ == "__main__":
  main()