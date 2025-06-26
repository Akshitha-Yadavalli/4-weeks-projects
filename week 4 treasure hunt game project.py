import random

def create_grid(size):
    return [["🟦" for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def hide_treasure(grid):
    size = len(grid)
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return (x, y)

def play_game():
    print("🏴‍☠️ Welcome to the Treasure Hunt Game!")
    size = 5
    grid = create_grid(size)
    treasure_location = hide_treasure(grid)
    attempts = 5

    while attempts > 0:
        print_grid(grid)
        print(f"\nYou have {attempts} attempts left.")

        try:
            guess_x = int(input("Enter row (0-4): "))
            guess_y = int(input("Enter column (0-4): "))
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers.")
            continue

        if guess_x < 0 or guess_x >= size or guess_y < 0 or guess_y >= size:
            print("🚫 Out of bounds! Try again.")
            continue

        if (guess_x, guess_y) == treasure_location:
            grid[guess_x][guess_y] = "💰"
            print_grid(grid)
            print("🎉 Congratulations! You found the treasure!")
            return
        else:
            grid[guess_x][guess_y] = "❌"
            print("💨 No treasure here... Keep trying!")
            attempts -= 1

    print("😢 Game over! You're out of attempts.")
    tx, ty = treasure_location
    grid[tx][ty] = "💰"
    print("The treasure was at:")
    print_grid(grid)

if __name__ == "__main__":
    play_game()
