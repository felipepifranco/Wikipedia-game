from webScraper import *

class Test_WebScraper():
  def test_get_title_and_links(self):
    url = 'https://en.wikipedia.org/wiki/The_BMJ'
    info = WebScraper.get_title_and_links(url)
    title = info["title"]
    assert title == "The BMJ"

  def test_get_links(self):
    url = 'https://en.wikipedia.org/wiki/AMTC'
    info = WebScraper.get_title_and_links(url)
    links = info["links"]

    target_links = [
      ("Allied Maritime Transport Council", "https://en.wikipedia.org/wiki/Allied_Maritime_Transport_Council")
    ]

    assert target_links == links
  
  def test_get_links_empty(self):
    url = "https://en.wikipedia.org/wiki/Paulius_Stankevicius"
    info = WebScraper.get_title_and_links(url)
    links = info["links"]

    assert [] == links

  def test_random_pages(self):
    random_page = WebScraper.get_random_page()
    assert "https://en.wikipedia.org/wiki/" in random_page

  def test_random_end_page(self):
    random_page = WebScraper.get_ending_page()
    assert "https://en.wikipedia.org/wiki/" in random_page

    vital_url = "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level_3"
    vital_pages = WebScraper.get_title_and_links(vital_url)["links"]
    
    random_title = WebScraper.get_title(random_page)

    assert (random_title, random_page) in vital_pages