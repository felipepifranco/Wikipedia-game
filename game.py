from utils import *
from scoreboard import ScoreBoard

class Game:
  def __init__(self, start_page, start_page_name, target_page, target_name):
    self.round = 1
    self.won = False
    self.page_history = [start_page_name]
    self.target_url = target_page
    self.target_name = target_name
    self.current_url = start_page

  def show_history(self):
    """Prints all pages visited so far."""
    prSeparator()

    prWarning("Number of pages visited: ", "")
    print()
    print(len(self.page_history))

    prWarning("List of visited pages:")
    for page in self.page_history:
      print(page)

  def register_page(self, page_info):
    '''
    adds a page to the page_history and increases the counter
    must be called when a new page is clicked on
    page_info -> tuple in format (title, link)
    '''
    title = page_info[TITLE]
    self.page_history.append(title)
    self.round +=1
    self.current_url = page_info[LINK]
    
    if self.current_url == self.target_url:
      self.won = True

  def end_game(self):
    '''
    checks if user has won or lost, and display a message according to that
    shows game history (page history and counter)
    register history into the scoreboard
    '''
    print()
    prSeparator()

    if self.won == False:
      prError("You have lost!")
    elif self.won == True:
      prWelcome("You have won! Congratulations")

    
    self.show_history()
    prSeparator()
    print()
    ScoreBoard.register(self)

  @staticmethod
  def print_pages_end(links_list, index_begin=0):
    '''prints all pages
       has a limit of 100. If it passed that, it warns the user
       to print the remaining, it is uses:
       - the first return value, that is True only if all links were already print
       - the index_begin, which represents the value that the last print stopped (and is the second return value)
       returns: (has_ended, last_index)
       '''
    if len(links_list) == 0:
      print("No links!")
      return True, -1
    elif index_begin >= len(links_list):
      raise IndexError

    limit = 0
    while index_begin < len(links_list) and limit < 100:
      link = links_list[index_begin]
      print(f'{index_begin +1} - {link[TITLE]}') 
      index_begin += 1
      limit +=1

    if index_begin >= len(links_list):
      return True, index_begin
    else:
      prSubMsg("Type '+' to continue seeing the links...")
      return False, index_begin 

  @staticmethod
  def print_rules():
    '''prints the Wikipedia Game rules and available commands.'''
    prSeparator()
    prWelcome("\n         WIKIPEDIA GAME RULES     ")
    prSeparator()
    
    prPageName("\nOBJECTIVE:") 
    print('Navigate from a starting Wikipedia article to a target article using only the links within each page in as few clicks as possible.')

    prPageName("\nHOW TO PLAY:") 
    print('1. You start on a randomly assigned Wikipedia page.\n' \
    '2. You will see a target page you need to reach.\n' \
    '3. In each round, choose a numbered link to travel to that page.\n' \
    '4. You win when you land on the target page!')

    prPageName("\nCOMMANDS:")
    print("- <number> : Go to the corresponding page link.\n"
    "- '+'      : View the next batch of links (if there are more than 100).\n"
    "- 'history': See all pages you have visited so far.\n"
    "- 'exit'   : Give up and return to the main menu.\n")

    prSeparator()    


