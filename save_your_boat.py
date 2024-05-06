import random

# List of words with hints for the game
words = [
    {
        "word": "ocean",
        "hints": [
            "It's a large body of salt water.",
            "Many marine animals live here.",
            "Great for sailing.",
            "Has various zones like the abyssal zone.",
        ],
    },
    {
        "word": "sail",
        "hints": [
            "Part of a boat that catches the wind.",
            "Allows boats to move forward.",
            "Made of fabric or other materials.",
            "Comes in various shapes and sizes.",
        ],
    },
    {
        "word": "anchor",
        "hints": [
            "Used to keep a boat in place.",
            "Typically made of heavy metal.",
            "Dropped into the water to hold a boat stationary.",
            "Has a shank, a stock, and flukes.",
        ],
    },
]


def hints_generator(hints, index):
    if index > len(hints) - 1:
        return "no more hints"
    return hints[index]


def choose_word():
    return random.choice(words)


def check_letters(word, array):
    for letter in word:
        if letter not in array:
            return False
    return True


print("\nWelcome to Save Your Boat!\n")
print("In this game, you need to guess the word by entering one letter at a time.")
print("You have 5 lives. If you lose all your lives, your boat will sink!\n")


def play_game():
    lives = 5
    hint_index = 0
    guess = choose_word()
    guessed_letters = []
    answer = guess["word"]

    play = input("Would you like to play? (y/n): ").lower()

    if play != "y":
        print("Maybe next time! Goodbye.")
        return

    print("\nType 'exit' at any time to quit the game.")

    while lives > 0:

        result = check_letters(answer, guessed_letters)
        if result == True:
            print("Congratulations, you saved the boat")
            return

        print("Lives remaining:", lives)

        hint = hints_generator(guess["hints"], hint_index)
        print(f"\nHint: {hint}\n")

        display_word = ""
        for letter in answer:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        user_input = input("Enter a letter: \n").lower()

        if user_input == "exit":
            print("Thanks for playing! Goodbye.")
            return

        if len(user_input) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        if user_input in answer:
            print(f"The letter '{user_input}' is in the word.")
            guessed_letters.append(user_input)
            hint_index += 1
        else:
            print("Incorrect guess. You lose a life.")
            hint_index += 1
            lives -= 1
            if lives == 0:
                print("Oops! Your boat sank. The word was:", answer)
                return


play_game()

# ("ocean", ["It's a large body of salt water.", "Many marine animals live here.", "Great for sailing.", "Has various zones like the abyssal zone."]),
# ("sail", ["Part of a boat that catches the wind.", "Allows boats to move forward.", "Made of fabric or other materials.", "Comes in various shapes and sizes."]),
# ("anchor", ["Used to keep a boat in place.", "Typically made of heavy metal.", "Dropped into the water to hold a boat stationary.", "Has a shank, a stock, and flukes."]),
# ("wave", ["Forms in the ocean due to wind.", "Can be large or small.", "Surfers love to ride them.", "Caused by disturbances in the water."]),
# ("ship", ["A large vessel for transporting goods or passengers.", "Often used in international trade.", "Can be powered by sails or engines.", "Has a captain and a crew."]),
# ("captain", ["The leader of a ship or boat.", "Responsible for navigation and safety.", "Gives orders to the crew.", "Often portrayed as brave and authoritative."]),
# ("seagull", ["A common seabird.", "Found near coasts and oceans worldwide.", "Known for its distinctive cry.", "Often scavenges for food near shorelines."]),
# ("fisherman", ["A person who catches fish for a living or as a hobby.", "Uses various methods like nets, lines, and traps.", "Often spends long hours at sea.", "Part of the maritime industry."]),
# ("buoy", ["A floating object used for navigation or marking hazards.", "Can be anchored to the seabed or allowed to drift.", "Comes in different shapes and colors.", "Often used in conjunction with nautical charts."]),
# ("lighthouse", ["A tall structure with a light at the top.", "Used to guide ships and boats at sea.", "Located on coastlines and near dangerous reefs.", "Has a distinctive pattern of light flashes."])
