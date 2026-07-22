import os, json
from datetime import datetime
from utils import *

class ScoreBoard:
  @staticmethod
  def show_scores():
    '''prints scores (from a json file)'''

    try:
      with open(FILE_NAME, "r") as score_file:
        score_board = json.load(score_file)
    except (FileNotFoundError, json.JSONDecodeError):
      print("No scores found!")
      return

    if not score_board:
      print("No scores registered yet!")
      return

    prPageName("\nScoreboard:")
    for rank, entry in enumerate(score_board, start=1):
      pages = entry.get("Number of visited pages", 0)
      start = entry.get("First page", "Unknown")
      target = entry.get("Target page", "Unknown")
      date = entry.get("Date", "N/A")

      print(f"{rank}. {start} -> {target} | {pages} pages | {date}")
    print()


  @staticmethod
  def register(game):
    '''register a new game history into the scoreboard
       must be called when a game ends'''
    try:
      with open(FILE_NAME, 'r') as score_file:
        score_board = json.load(score_file)
    except FileNotFoundError:
      score_board = []

    now = datetime.now()
    today = now.strftime("%d-%m-%Y")

    game_score = {
      "Number of visited pages": game.round,
      "First page": game.page_history[0],
      "Target page": game.target_name,
      "Date": today,
      "Pages visited": game.page_history
    }

    score_board.append(game_score)
    score_board.sort(key=lambda item: (item["Number of visited pages"], item["Date"]))

    with open(FILE_NAME, 'w') as score_file:
      json.dump(score_board, score_file, indent=2)
    
    

    