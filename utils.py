TITLE = 0
LINK = 1

FILE_NAME = "scoreboard.json"

def prSeparator():
  print("=============================================")

def prWelcome(welcomemsg, end = '\n'):
  print(f"\033[1m\033[92m{welcomemsg}\033[00m", end)

def prError(msg):
  print(f"\033[1m\033[91m{msg}\033[00m")

def prWarning(msg, end = '\n'):
  print(f"\033[1m\033[93m{msg}\033[00m", end=end)

def prSubMsg(msg):
  print(f"\033[97m{msg}\033[00m")

def prPageName(name):
  print(f"\033[35m{name}\033[00m")