class Game:
  def __init__(self, start_page, target_page):
    self._round = 0
    self.won = False
    self.page_history = [start_page]
    self.target_page = target_page
    self.current_page = start_page

  def show_history(self):
    """Prints all pages visited so far."""
    pass

  def register_page(self, page):
    '''
    adds a page to the page_history and increases the counter
    must be called when a new page is clicked on
    '''
    pass

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