# Wikipedia Game

A Python-based terminal game where players navigate between Wikipedia pages using only in-text links to reach a target destination.

---

## About the Project

The **Wikipedia Game** challenges players to navigate from a random starting Wikipedia article to a designated target article purely by following hyperlinks within each page. 

This repository contains a modular Python implementation that fetches live data directly from Wikipedia, manages game state, tracks history, and logs player scores into a local scoreboard system.

It was made purely for educational purposes.

---

### Features
- **Live Wikipedia Scraping:** Interacts with Wikipedia pages to extract real-time article titles and embedded links.
- **Dynamic Target Generation:** Pick random target articles or "Vital Articles" (the most iconic Wikipedia pages) for balanced difficulty.
- **Game State Tracking:** Logs visited pages and counts rounds
- **Persistent:** Saves completed game statistics, round counts, and scores in a structured JSON file.

### Architecture

```
.
├── game.py
├── main.py              # Program input and menu handler
├── Readme.md            # Documentation
├── requirements.txt     # Required libraries
├── scoreboard.py        # Score storage functions (uses JSON files)
├── test_samples.py      # Unit tests for classes
├── test_webScraper.py   # Unit Tests for Web scraper (takes more time)
├── utils.py             # Utility functions
└── webScraper.py        # Wikipedia web scraping functions
```

### Installation

1. Clone the repository

2. Install dependencies (venv recommended):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python main.py
   ```