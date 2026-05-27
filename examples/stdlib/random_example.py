"""
Random Example - Generating Random Numbers

This example demonstrates:
- Generating random floats and integers
- Random choices and shuffling
- Seeding for reproducibility
- Random strings
"""

import random
import string

print("=== Random Floats ===")

# Random float between 0 and 1
random_float = random.random()
print(f"random.random(): {random_float}")

# Random float in a range
random_range = random.uniform(1.5, 10.5)
print(f"random.uniform(1.5, 10.5): {random_range}")
print()

print("=== Random Integers ===")

# Random integer in range (inclusive)
random_int = random.randint(1, 10)
print(f"random.randint(1, 10): {random_int}")

# Random integer from range (step)
random_step = random.randrange(0, 100, 10)  # 0, 10, 20, ..., 90
print(f"random.randrange(0, 100, 10): {random_step}")

# Random integer in range (exclusive upper bound)
random_range = random.randrange(1, 11)  # 1 to 10
print(f"random.randrange(1, 11): {random_range}")
print()

print("=== Random Choices ===")

# Choose random element from a sequence
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print(f"random.choice({fruits}): {random_fruit}")

# Choose multiple random elements (with replacement)
random_fruits = random.choices(fruits, k=5)
print(f"random.choices({fruits}, k=5): {random_fruits}")

# Choose unique random elements (without replacement)
unique_fruits = random.sample(fruits, 2)
print(f"random.sample({fruits}, 2): {unique_fruits}")
print()

print("=== Shuffling ===")

# Shuffle a list in place
cards = ["A", "K", "Q", "J", "10", "9", "8", "7"]
print(f"Original cards: {cards}")

random.shuffle(cards)
print(f"Shuffled cards: {cards}")
print()

print("=== Seeding for Reproducibility ===")

# Set seed for reproducible results
random.seed(42)
print("With seed=42:")
print(f"  random.random(): {random.random()}")
print(f"  random.randint(1, 10): {random.randint(1, 10)}")

# Reset seed to get same results again
random.seed(42)
print("\nWith seed=42 again:")
print(f"  random.random(): {random.random()}")
print(f"  random.randint(1, 10): {random.randint(1, 10)}")
print()

print("=== Random Strings ===")

# Generate random string of letters
letters = string.ascii_letters  # a-zA-Z
random_letters = "".join(random.choices(letters, k=10))
print(f"Random letters (10 chars): {random_letters}")

# Generate random string of letters and digits
alphanumeric = string.ascii_letters + string.digits
random_string = "".join(random.choices(alphanumeric, k=12))
print(f"Random alphanumeric (12 chars): {random_string}")

# Generate random password
def generate_password(length=12):
    """Generate a random password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choices(chars, k=length))


print(f"Random password (12 chars): {generate_password()}")
print()

print("=== Weighted Random ===")

# Random with weights
items = ["apple", "banana", "cherry", "date"]
weights = [0.5, 0.3, 0.15, 0.05]  # apple is most likely

weighted_choices = random.choices(items, weights=weights, k=10)
print(f"Weighted choices: {weighted_choices}")
print()

print("=== Random Gaussian ===")

# Gaussian (normal) distribution
mean = 0
std_dev = 1
gaussian_value = random.gauss(mean, std_dev)
print(f"random.gauss({mean}, {std_dev}): {gaussian_value}")

# Generate multiple Gaussian values
gaussian_values = [random.gauss(0, 1) for _ in range(5)]
print(f"5 Gaussian values: {gaussian_values}")
print()

print("=== Practical Examples ===")

# Simulate rolling a die
def roll_die():
    """Simulate rolling a 6-sided die."""
    return random.randint(1, 6)


print("Rolling a die 5 times:")
for _ in range(5):
    print(f"  {roll_die()}")

# Simulate coin flip
def flip_coin():
    """Simulate flipping a coin."""
    return random.choice(["Heads", "Tails"])


print("\nFlipping a coin 5 times:")
for _ in range(5):
    print(f"  {flip_coin()}")

# Random lottery numbers
def generate_lottery_numbers(num_numbers=6, max_number=49):
    """Generate random lottery numbers."""
    return sorted(random.sample(range(1, max_number + 1), num_numbers))


print(f"\nLottery numbers: {generate_lottery_numbers()}")

# Random team assignment
def assign_teams(players, team_size=2):
    """Assign players to teams."""
    random.shuffle(players)
    teams = []
    for i in range(0, len(players), team_size):
        team = players[i:i + team_size]
        teams.append(team)
    return teams


players = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
teams = assign_teams(players, team_size=2)
print(f"\nTeams: {teams}")
