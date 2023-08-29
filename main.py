# Globals
player_range_select = ""
playyer_guess = ""
# Functions 
def validate_input(input):
  try :
    int(input)
  else:
    raise Exception("not valid input")

# Call Stack

while True : 
  player_range_select = input("Please the number at the top of the range you would like? " )
  player_guess = input("Please Place your Guess: ")
  validate_input(player_range_select)
  validate_input(player_guess)
