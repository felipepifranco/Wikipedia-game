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
    register history into the ranking
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

    
    pass

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



class Ranking:
  @staticmethod
  def show_ranking():
    '''prints ranking (from a json file)  
    '''

  @staticmethod
  def register_in_ranking():
    '''
    register a new game history into the ranking
    must be called when a game ends
    '''