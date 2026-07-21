import requests

class WebScraper:
  @staticmethod
  def get_title(page):
    '''gets the title of the page'''
    url = 'https://en.wikipedia.org/wiki/The_BMJ'
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}

    res = requests.get(url, headers=headers)
    print(res.status_code)
    print(res.content)
  
  @staticmethod
  def get_links(page):
    '''gets all page links in a page'''
    pass
  
  @staticmethod
  def get_random_page():
    '''returns a random page from wikipedia'''
    pass

  def get_ending_page():
    '''returns a random "vital" page from wikipedia
       this are the most known pages in it
       the ending page is set like this so the game doesnt get to hard'''
    pass

