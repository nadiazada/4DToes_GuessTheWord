""" A simple "guess the word" game. A leader is chosen to select a secret word 
    while 2-4 players either ask questions about the secret word or try to 
    guess it. The round is over when a player correctly guesses the 
    secret word.
"""

# Leader setup
def setup_game(): 
    print("=== Welcome to the Secret Word Guessing Game! ===")
    print("""
    How to play: 
    - One leader secretly chooses a word (which will be hidden afterward!).
    - 2 to 4 players will take turns asking questions or making guesses.
    - You have 10 turns total to guess correctly before the game ends! 
    """) 
    
    secret_word = input("Leader, please enter your secret word: ").strip().lower()
    print("\n" * 40)
    print("Secret word saved successfully!\n") 

    while True: 
        try: 
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else: 
                print("Please choose between 2 to 4 players.")
        except ValueError: 
            print("Invalid input. Please enter a number between 2 to 4.")

    print(f"\nGame setup complete! {num_players} players will play.\n") 
    return secret_word, num_players

# Player Input
def player_turn(player_name):
    print(f"\n{player_name}'s turn:")
    user_input = input("Ask a question or type \"guess: (word)\" to make a guess: ").strip()
    return user_input

# Guess / question logic
def handle_input(user_input, secret_word, player_name):
    # ---- check if it's a guess ----
    if user_input.lower().startswith("guess:"):
        # everything after 'guess:' is the guessed word
        guess = user_input.split(":", 1)[1].strip().lower()

        # handle empty guess
        if not guess:
            print("Format is: guess: <word>")
            return False

        # compare with secret word
        if guess == secret_word.lower():
            print(f"\n{player_name} guessed the secret word! It is '{secret_word}'.")
            return True
        else:
            print("Nope, that's not it.")
            return False

    # ---- otherwise, treat it as a normal question ----
    else:
        leader_answer = input("Leader, your answer: ")
        print(f"Leader says: {leader_answer}")
        return False

# Main game flow
def play_game():
    secret_word, num_players = setup_game()

    # Track turns
    max_turns = 10
    current_turn = 1
    game_won = False

    # Main loop
    while current_turn <= max_turns and not game_won:
        print(f"\n--- Turn {current_turn} ---")

        # Each player gets a turn
        for i in range(num_players):
            player_name = f"Player {i + 1}"

            # Get player's input
            user_input = player_turn(player_name)

            # Process guess/question
            result = handle_input(user_input, secret_word, player_name)

            # if True => someone guessed correctly
            if result:
                game_won = True
                break  # Stop looping through players

        current_turn += 1

    # Game end handling
    if not game_won:
        print(f"\nNo one guessed the word. The secret word was: '{secret_word}'.")
    print("\nThanks for playing!")

# Start main game
play_game()