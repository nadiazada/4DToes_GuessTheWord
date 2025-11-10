#python code. Everything can go into one file 
'''
Task 1 — Leader setup

Owner: NILA
Focus: getting the secret word, asking number of players, and printing rules.
Implements the setup_game() function.

Task 2 — Player input

def player_turn(player_name):
    """
    Handles one player's turn.
    Prompts the player to ask a question or make a guess.
    Returns the player's input as a string.
    """
    print(f"\n{player_name}'s turn:")
    user_input = input("Ask a question or make a guess: ").strip()
    return user_input
    
Task 3 — Guess / question logic

Owner: NADIA 
Focus: detect guesses vs questions, check if correct, and manage responses.
Implements the handle_input() function.

Task 4 — Main game flow

Owner: JAMES
Focus: connect all functions together, run rounds, handle win/loss.
Implements the play_game() function (calls all others)
'''
def handle_win_conditions(Player, Leader):
  if Player.guess() and Leader.guess():
    Player.declare_winner()
    is_game_running = false # Round is over
  else:
    is_game_running = true
  return is_game_running

# Checks number of players in Lobby
def check_player_count(player_count):
  if player_count < 2:
    print("Not enough players to start game")
    return False
  
  elif player_count > 4:
    print("Player count cannot exceed 4")
    return False

  else:
    return True

# Main game flow
def play_game():
  while is_game_running = true:
    if check_player_count == false:
      print("Error: Player count must be between 2 and 4 Players")
      return False
    else:
      # Leader is chosen, secret word is made, and rules are printed
      setup_game()

      # Prompt Players and collect input
      player_turn()

      # Detect guesses vs questions, manage responses
      handle_input()

      # Checks Player and Leader guess and declares winner
      handle_win_conditions()


    
