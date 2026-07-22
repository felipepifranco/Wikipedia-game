from game import *
import pytest

@pytest.fixture
def set_up_game():
  start_page = 'https://en.wikipedia.org/wiki/The_BMJ'
  start_page_name = "The BMJ"
  target_page = 'https://en.wikipedia.org/wiki/Dog'
  target_page_name = "Dog"
  game_test = Game(start_page, start_page_name, target_page, target_page_name)
  return game_test

class Test_game:
  def test_register_page(self, set_up_game):
    page_info = ("World Wide Web", "https://en.wikipedia.org/wiki/World_Wide_Web")

    set_up_game.register_page(page_info)

    assert set_up_game.page_history[1] == "World Wide Web"
    assert set_up_game.won  == False
    assert set_up_game.round == 2
    assert set_up_game.current_url == "https://en.wikipedia.org/wiki/World_Wide_Web"
    
    
