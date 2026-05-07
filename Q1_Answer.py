
#############################################################

#############################################################

import random

FILE_PATH = "file.txt"
MIN_REPEAT = 1
MAX_REPEAT = 20
FORWARD = "1"
BACKWARD = "2"
TREASURE_WORD = "TREASURE"


# =========================
# File Creation
# =========================
def generate_game_string():
    """
    Create the game string:
    digits 0-9 (random repeats) + TREASURE + digits 9-0 (random repeats)
    """
    game_string = ""

    # 0 → 9
    for digit in range(10):
        repeat_count = random.randint(MIN_REPEAT, MAX_REPEAT)
        game_string += str(digit) * repeat_count

    game_string += f" {TREASURE_WORD} "

    # 9 → 0
    for digit in range(9, -1, -1):
        repeat_count = random.randint(MIN_REPEAT, MAX_REPEAT)
        game_string += str(digit) * repeat_count

    return game_string


def write_to_file(file_path, content):
    """
    Write content to file safely.
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except PermissionError:
        print("Error: No permission to write to file.")
    except Exception as e:
        print("Unexpected error while writing file:", e)


def read_from_file(file_path):
    """
    Read content from file safely.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error while reading file:", e)

    return ""


# =========================
# Game Logic
# =========================
def get_user_input():
    """
    Get validated user input for direction and steps.
    """
    direction = input("Where do you want to move? [1-Forward 2-Backwards]: ")
    steps_input = input("How many characters? ")

    if not steps_input.isdigit():
        print("Invalid number")
        return None, None

    return direction, int(steps_input)


def move_cursor(cursor, direction, steps):
    """
    Move cursor based on direction and steps.
    """
    if direction == FORWARD:
        return cursor + steps
    elif direction == BACKWARD:
        return cursor - steps
    else:
        print("Invalid choice")
        return None


def fix_cursor_bounds(cursor, text_length):
    """
    Ensure cursor stays within valid range.
    """
    if cursor < 0:
        return 0
    if cursor >= text_length:
        return text_length - 1
    return cursor


def play_game(game_text):
    """
    Main game loop: move cursor until TREASURE is found.
    """
    cursor = 0
    moves = 0

    while True:
        direction, steps = get_user_input()
        if direction is None:
            continue

        new_cursor = move_cursor(cursor, direction, steps)

        if new_cursor is None:
            continue

        cursor = fix_cursor_bounds(new_cursor, len(game_text))

        print("You landed on:", game_text[cursor])
        moves += 1

        # Check if landed on TREASURE letter
        if game_text[cursor] in TREASURE_WORD:
            print("\n🎉 Found the Treasure! 🎉")
            print("Total moves:", moves)
            break


# =========================
# Main Execution
# =========================
def main():
    """
    Main function to run the program.
    """
    game_string = generate_game_string()
    write_to_file(FILE_PATH, game_string)

    game_text = read_from_file(FILE_PATH)

    if game_text:
        play_game(game_text)
    else:
        print("Game cannot start without valid data.")


if __name__ == "__main__":
    main()