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

  def test_register_target_page(self, set_up_game):
    page_info = ("Dog", 'https://en.wikipedia.org/wiki/Dog')

    set_up_game.register_page(page_info)

    assert set_up_game.page_history[1] == "Dog"
    assert set_up_game.won  == True
    assert set_up_game.round == 2
    assert set_up_game.current_url == "https://en.wikipedia.org/wiki/Dog"

  def test_show_history(self, subtests, set_up_game, capsys):
    with subtests.test("One page"):
      set_up_game.show_history()
      captured = capsys.readouterr()

      assert 'The BMJ\n' in captured.out
      assert 'Dog' not in captured.out

    with subtests.test("More Pages"):
      set_up_game.page_history.append("World Wide Web")
      set_up_game.page_history.append('Sydney')
      set_up_game.page_history.append('Africa')
      set_up_game.page_history.append('Agriculture')
      set_up_game.page_history.append('Alexander the Great')
      set_up_game.page_history.append('DNA')

      set_up_game.show_history()

      captured = capsys.readouterr()
      assert "World Wide Web" in captured.out
      assert 'Sydney' in captured.out
      assert 'Africa' in captured.out
      assert 'Agriculture' in captured.out
      assert 'Alexander the Great' in captured.out
      assert 'DNA' in captured.out

    
    
  def test_print_pages_end(self, capsys):
    link_list = [("World Wide Web", "https://en.wikipedia.org/wiki/World_Wide_Web"), ("Dog", 'https://en.wikipedia.org/wiki/Dog')]    

    has_ended, index_continue = Game.print_pages_end(link_list)
    
    captured = capsys.readouterr()
    assert captured.out == '1 - World Wide Web\n2 - Dog\n'

  def test_print_big_page(self, capsys):
    links_101 = [
    ('Sydney', 'https://en.wikipedia.org/wiki/Sydney'),
    ('Africa', 'https://en.wikipedia.org/wiki/Africa'),
    ('Agriculture', 'https://en.wikipedia.org/wiki/Agriculture'),
    ('Albert Einstein', 'https://en.wikipedia.org/wiki/Albert_Einstein'),
    ('Alexander the Great', 'https://en.wikipedia.org/wiki/Alexander_the_Great'),
    ('Algebra', 'https://en.wikipedia.org/wiki/Algebra'),
    ('Amazon River', 'https://en.wikipedia.org/wiki/Amazon_River'),
    ('Anatomy', 'https://en.wikipedia.org/wiki/Anatomy'),
    ('Ancient Egypt', 'https://en.wikipedia.org/wiki/Ancient_Egypt'),
    ('Ancient Greece', 'https://en.wikipedia.org/wiki/Ancient_Greece'),
    ('Antarctica', 'https://en.wikipedia.org/wiki/Antarctica'),
    ('Architecture', 'https://en.wikipedia.org/wiki/Architecture'),
    ('Aristotle', 'https://en.wikipedia.org/wiki/Aristotle'),
    ('Art', 'https://en.wikipedia.org/wiki/Art'),
    ('Asia', 'https://en.wikipedia.org/wiki/Asia'),
    ('Astronomy', 'https://en.wikipedia.org/wiki/Astronomy'),
    ('Atlantic Ocean', 'https://en.wikipedia.org/wiki/Atlantic_Ocean'),
    ('Australia', 'https://en.wikipedia.org/wiki/Australia'),
    ('Bacteria', 'https://en.wikipedia.org/wiki/Bacteria'),
    ('Beijing', 'https://en.wikipedia.org/wiki/Beijing'),
    ('Berlin', 'https://en.wikipedia.org/wiki/Berlin'),
    ('Biology', 'https://en.wikipedia.org/wiki/Biology'),
    ('Buddha', 'https://en.wikipedia.org/wiki/Buddha'),
    ('Buddhism', 'https://en.wikipedia.org/wiki/Buddhism'),
    ('Cairo', 'https://en.wikipedia.org/wiki/Cairo'),
    ('Chemical element', 'https://en.wikipedia.org/wiki/Chemical_element'),
    ('Chemistry', 'https://en.wikipedia.org/wiki/Chemistry'),
    ('Chess', 'https://en.wikipedia.org/wiki/Chess'),
    ('China', 'https://en.wikipedia.org/wiki/China'),
    ('Christianity', 'https://en.wikipedia.org/wiki/Christianity'),
    ('Cinema', 'https://en.wikipedia.org/wiki/Cinema'),
    ('Climate change', 'https://en.wikipedia.org/wiki/Climate_change'),
    ('Computer science', 'https://en.wikipedia.org/wiki/Computer_science'),
    ('DNA', 'https://en.wikipedia.org/wiki/DNA'),
    ('Earth', 'https://en.wikipedia.org/wiki/Earth'),
    ('Economics', 'https://en.wikipedia.org/wiki/Economics'),
    ('Electricity', 'https://en.wikipedia.org/wiki/Electricity'),
    ('Energy', 'https://en.wikipedia.org/wiki/Energy'),
    ('Engineering', 'https://en.wikipedia.org/wiki/Engineering'),
    ('Europe', 'https://en.wikipedia.org/wiki/Europe'),
    ('Evolution', 'https://en.wikipedia.org/wiki/Evolution'),
    ('First World War', 'https://en.wikipedia.org/wiki/First_World_War'),
    ('Fungus', 'https://en.wikipedia.org/wiki/Fungus'),
    ('Galileo Galilei', 'https://en.wikipedia.org/wiki/Galileo_Galilei'),
    ('Geography', 'https://en.wikipedia.org/wiki/Geography'),
    ('Geometry', 'https://en.wikipedia.org/wiki/Geometry'),
    ('Hinduism', 'https://en.wikipedia.org/wiki/Hinduism'),
    ('History', 'https://en.wikipedia.org/wiki/History'),
    ('Human', 'https://en.wikipedia.org/wiki/Human'),
    ('India', 'https://en.wikipedia.org/wiki/India'),
    ('Industrial Revolution', 'https://en.wikipedia.org/wiki/Industrial_Revolution'),
    ('Insect', 'https://en.wikipedia.org/wiki/Insect'),
    ('Internet', 'https://en.wikipedia.org/wiki/Internet'),
    ('Islam', 'https://en.wikipedia.org/wiki/Islam'),
    ('Japan', 'https://en.wikipedia.org/wiki/Japan'),
    ('Jesus', 'https://en.wikipedia.org/wiki/Jesus'),
    ('Judaism', 'https://en.wikipedia.org/wiki/Judaism'),
    ('Language', 'https://en.wikipedia.org/wiki/Language'),
    ('Latin America', 'https://en.wikipedia.org/wiki/Latin_America'),
    ('Leonardo da Vinci', 'https://en.wikipedia.org/wiki/Leonardo_da_Vinci'),
    ('Literature', 'https://en.wikipedia.org/wiki/Literature'),
    ('London', 'https://en.wikipedia.org/wiki/London'),
    ('Mammal', 'https://en.wikipedia.org/wiki/Mammal'),
    ('Mathematics', 'https://en.wikipedia.org/wiki/Mathematics'),
    ('Medicine', 'https://en.wikipedia.org/wiki/Medicine'),
    ('Microorganism', 'https://en.wikipedia.org/wiki/Microorganism'),
    ('Moon', 'https://en.wikipedia.org/wiki/Moon'),
    ('Music', 'https://en.wikipedia.org/wiki/Music'),
    ('New York City', 'https://en.wikipedia.org/wiki/New_York_City'),
    ('North America', 'https://en.wikipedia.org/wiki/North_America'),
    ('Ocean', 'https://en.wikipedia.org/wiki/Ocean'),
    ('Pacific Ocean', 'https://en.wikipedia.org/wiki/Pacific_Ocean'),
    ('Painting', 'https://en.wikipedia.org/wiki/Painting'),
    ('Paris', 'https://en.wikipedia.org/wiki/Paris'),
    ('Philosophy', 'https://en.wikipedia.org/wiki/Philosophy'),
    ('Physics', 'https://en.wikipedia.org/wiki/Physics'),
    ('Plant', 'https://en.wikipedia.org/wiki/Plant'),
    ('Plato', 'https://en.wikipedia.org/wiki/Plato'),
    ('Poetry', 'https://en.wikipedia.org/wiki/Poetry'),
    ('Psychology', 'https://en.wikipedia.org/wiki/Psychology'),
    ('Pyramid', 'https://en.wikipedia.org/wiki/Pyramid'),
    ('Quantum mechanics', 'https://en.wikipedia.org/wiki/Quantum_mechanics'),
    ('Religion', 'https://en.wikipedia.org/wiki/Religion'),
    ('Renaissance', 'https://en.wikipedia.org/wiki/Renaissance'),
    ('Rome', 'https://en.wikipedia.org/wiki/Rome'),
    ('Science', 'https://en.wikipedia.org/wiki/Science'),
    ('Sculpture', 'https://en.wikipedia.org/wiki/Sculpture'),
    ('Second World War', 'https://en.wikipedia.org/wiki/Second_World_War'),
    ('Shakespeare', 'https://en.wikipedia.org/wiki/William_Shakespeare'),
    ('Social science', 'https://en.wikipedia.org/wiki/Social_science'),
    ('Sociology', 'https://en.wikipedia.org/wiki/Sociology'),
    ('Solar System', 'https://en.wikipedia.org/wiki/Solar_System'),
    ('South America', 'https://en.wikipedia.org/wiki/South_America'),
    ('Sun', 'https://en.wikipedia.org/wiki/Sun'),
    ('Technology', 'https://en.wikipedia.org/wiki/Technology'),
    ('Theatre', 'https://en.wikipedia.org/wiki/Theatre'),
    ('Tokyo', 'https://en.wikipedia.org/wiki/Tokyo'),
    ('United States', 'https://en.wikipedia.org/wiki/United_States'),
    ('Virus', 'https://en.wikipedia.org/wiki/Virus'),
    ('Water', 'https://en.wikipedia.org/wiki/Water'),
    ('World War II', 'https://en.wikipedia.org/wiki/World_War_II')
    ]

    has_ended, index_continue = Game.print_pages_end(links_101)
        
    captured = capsys.readouterr()
    assert index_continue == 100
    assert has_ended == False
    assert "continue seeing the links" in captured.out

    has_ended, index_continue = Game.print_pages_end(links_101, index_continue)

    captured = capsys.readouterr()
    assert index_continue == 101
    assert has_ended == True
    assert '101 - World War II\n' == captured.out