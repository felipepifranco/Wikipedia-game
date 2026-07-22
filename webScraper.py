import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class notFound(Exception):
  # print(page.status_code
  pass

class WebScraper:
  headers = {'User-Agent': 'WikipediaGameBot/0.0 (https://github.com/felipepifranco/Wikipedia-game.git)'}

  @staticmethod
  def get_title(url):
    '''gets the title of the page'''
    
    res = requests.get(url, headers=WebScraper.headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    # title
    title_content = soup.find('title')
    if title_content:
      main_title =  title_content.text.strip().replace(" - Wikipedia", "")
    else:
      raise notFound("page not found")
    
    return main_title
  
  @staticmethod
  def get_title_and_links(url):
    '''gets the title of the page'''
    
    res = requests.get(url, headers=WebScraper.headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    # title
    title_content = soup.find('title')
    if title_content:
      main_title =  title_content.text.strip().replace(" - Wikipedia", "")
    else:
      raise notFound("page not found")
    
    # links
    body = soup.find(id="bodyContent")
    links = [] # tuple list (title, url)
    
    if body:
      for tag in body.find_all('a', href=True):
        href = tag['href']

        if '/wiki/' in href and ':' not in href.replace("https:", "") and 'wikidata' not in href and '?' not in href:
          full_url = urljoin('https://en.wikipedia.org', href)
          title_from_url = (href.split('/wiki/')[-1].replace('_', ' '))
          link_title = tag.get('title', title_from_url)

          links.append((link_title, full_url))
          
    else:
      raise notFound("Invalid page")  
    
    info = {
      "title": main_title,
      "links": links
    }
    return info
  
  @staticmethod
  def get_random_page():
    '''returns a random page from wikipedia'''
    random_url = "https://en.wikipedia.org/wiki/Special:Random"

    res = requests.get(random_url, headers=WebScraper.headers)
    return res.url
  
  @staticmethod
  def get_ending_page():
    '''returns a random "vital" page from wikipedia
       these are the most known pages in it
       the ending page is set like this so the game doesnt get to hard'''

    random_url = "https://randomincategory.toolforge.org/?category=A-Class%20level-3%20vital%20articles&category2=B-Class%20level-3%20vital%20articles&category3=C-Class%20level-3%20vital%20articles&category4=FA-Class%20level-3%20vital%20articles&category5=FL-Class%20level-3%20vital%20articles&category6=GA-Class%20level-3%20vital%20articles&category7=List-Class%20level-3%20vital%20articles&category8=Start-Class%20level-3%20vital%20articles&category9=Stub-Class%20level-3%20vital%20articles&server=en.wikipedia.org&cmnamespace=&cmtype=&returntype=subject"

    res = requests.get(random_url, headers=WebScraper.headers)
    return res.url



