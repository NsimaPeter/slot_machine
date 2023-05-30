import random

# This is the symbols and their respective weights
symbols = ['Football', 'Bell', 'Lemon', 'Orange', 'Star', 'Moon']
weights = [0.4, 0.3, 0.2, 0.05, 0.03, 0.02]

# This is Function to spin the slot machine
def spin():
    
    # Generate three random symbols
    result = [random.choices(symbols, weights)[0] for _ in range(3)]
    return result


# This is Function to display the result
def display_result(result):
    print(' | '.join(result))


# This is Function to check if the result is a winning combination
def check_win(result):
    if result[0] == result[1] == result[2]:
        return True
    return False


# Function to play the game
def play_game():
    print('=== Welcome to the Text-Based Slot Machine ===')
    while True:
        input('Press Enter to spin the slot machine...')
        result = spin()
        display_result(result)
        if check_win(result):
            print('Congratulations! You won!')
        else:
            print('Sorry, you lost. Try again!')
        choice = input('Do you want to play again? (y/n): ')
        if choice.lower() != 'y':
            break


# Start the game
play_game()
