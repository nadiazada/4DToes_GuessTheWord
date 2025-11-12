#python code. Everything can go into one file 
'''Task 1 — Leader setup

Owner: NILA
Focus: getting the secret word, asking number of players, and printing rules.
Implements the setup_game() function.'''

def setup_game(): 
    print("=== Welcome to the Secret Word Guessing Game! ===")
    print("""
    How to play: 
    - One leader secretly chooses a word (which will be hidden afterward!).
    - 2 to 4 platers will take turns asking questions or making guesses.
    - You have 10 turns total to guess correctly before the game ends! 
    """) 
    secret_word = input("Leader, please enter your secret word: ").strip().lower()
    print("\n" * 40)
    print("Secret word saved successfully!\n") 

while True: 
    try: 
        num_platers = int(input("Enter number of players (2-4): "))
        if 2 <= num_players <= 4:
            break
        else: 
            print("Please choose between 2 to 4 players.")
    except ValueError: 
        print("Invalid input. Please enter a number between 2 to 4.")

print(f"\nGame setup complete! {num_players} players will play.\n") 
return secret_word, num_players

'''Task 2 — Player input'''

def player_turn(player_name):
    print(f"\n{player_name}'s turn:")
    user_input = input("Ask a question or make a guess: ").strip()
    return user_input
    
''' Task 3 — Guess / question logic

Owner: NADIA 
Focus: detect guesses vs questions, check if correct, and manage responses.
Implements the handle_input() function.
Checks what the player typed.
 - If it starts with 'guess:', treat it as a guess and check correctness.
 - Otherwise, treat it as a question for the leader.
Returns True if the secret word was guessed correctly, otherwise False.'''
def handle_input(user_input, secret_word, player_name):
    # ---- check if it's a guess ----
    if user_input.lower().startswith("guess:"):
        # everything after 'guess:' is the guessed word
        guess = user_input.split(":", 1)[1].strip().lower() #got this line from gpt bc didnt undrstand how to split 

        # handle empty guess
        if not guess:
            print(" Format is: guess: <word>")
            return False

        # compare with secret word
        if guess == secret_word.lower():
            print(f"\n {player_name} guessed the secret word! It is '{secret_word}'.")
            return True
        else:
            print(" Nope, that's not it.")
            return False

    # ---- otherwise, treat it as a normal question ----
    else:
        leader_answer = input(" Leader, your answer: ")
        print(f" Leader says: {leader_answer}")
        return False


''' Task 4 — Main game flow

Owner: JAMES
Focus: connect all functions together, run rounds, handle win/loss.
Implements the play_game() function (calls all others) '''

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


    
