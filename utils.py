TITLE = 0
LINK = 1

def prSeparator():
  print("=============================================")

def prWelcome(welcomemsg):
  print(f"\033[1m\033[92m{welcomemsg}\033[00m")

def prError(msg):
  print(f"\033[1m\033[91m{msg}\033[00m")

def prWarning(msg):
  print(f"\033[1m\033[93m{msg}\033[00m")

def prSubMsg(msg):
  print(f"\033[97m{msg}\033[00m")

def prPageName(name):
  print(f"\033[35m{name}\033[00m")