import random


# the symbols and their respective weights
symbols = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
weights = [0.4, 0.3, 0.2, 0.05, 0.03, 0.02]

# Function to spin the slot machine
def spin():
    # Generate three random symbols
    result = [random.choices(symbols, weights)[0] for _ in range(3)]
    return result

# Function to display the result
def display_result(result):
    print(' | '.join(result))
