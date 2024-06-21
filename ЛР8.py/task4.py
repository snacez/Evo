import random

def generate_doors(num_doors, num_prizes):
    """
    This function generates a list representing doors, where:
    - "prize" means there's a prize behind the door
    - "no prize" means there's nothing behind the door

    Args:
        num_doors: Total number of doors
        num_prizes: Number of prizes

    Returns:
        A list representing doors, for example: ["prize", "no prize", "no prize"]
    """
    doors = ["prize"] * num_prizes + ["no prize"] * (num_doors - num_prizes)
    random.shuffle(doors)
    return doors

def simulate_game(num_doors, num_prizes):
    """
    This function simulates the Monty Hall game multiple times and calculates win rates.

    Args:
        num_doors: Total number of doors
        num_prizes: Number of prizes

    Prints:
        The win rate for Player 1 staying and switching, and Player 2 staying.
    """
    # Generate the doors and players' initial choices
    doors = generate_doors(num_doors, num_prizes)
    player1_choice = random.randint(0, num_doors - 1)
    player2_choice = random.randint(0, num_doors - 1)

    # Initialize win counters
    player1_stays_wins = 0
    player1_switches_wins = 0
    player2_stays_wins = 0

    # Simulate 100,000 games
    for _ in range(100000):
        revealed_door = 0
        while doors[revealed_door] == "prize" or revealed_door == player1_choice:
            revealed_door = random.randint(0, num_doors - 1)

        # Player 1 stays or switches
        if player1_choice == revealed_door:
            # Player 1 stays, Player 2 gets the other un-revealed door (which must have the prize)
            player2_stays_wins += 1
        else:
            # Player 1 switches, they win
            player1_switches_wins += 1

    # Calculate win rates
    total_games = 100000
    player1_stays_rate = player1_stays_wins / total_games
    player1_switches_rate = player1_switches_wins / total_games
    player2_stays_rate = player2_stays_wins / total_games

    # Print results
    print(f"Player 1 staying wins: {player1_stays_rate:.4f}")
    print(f"Player 1 switching wins: {player1_switches_rate:.4f}")
    print(f"Player 2 staying wins: {player2_stays_rate:.4f}")

# Запуск симуляции для 3 дверей и 1 приза
simulate_game(3, 1)
