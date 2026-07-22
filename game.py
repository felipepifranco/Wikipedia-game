from utils import *
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
    pass

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
    register history into the ranking
    '''
    pass

class Ranking:
  @staticmethod
  def show_ranking():
    '''
    prints ranking (from a json file)  
    '''

  @staticmethod
  def register_in_ranking():
    '''
    register a new game history into the ranking
    must be called when a game ends
    '''