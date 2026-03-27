import sys   # Import sys module so we can exit the program using sys.exit()

# Variable to store the player's name (initially empty)
player_name = ""


def play_again(prompt=None):
    # This function asks the player if they want to play again

    if prompt is None:
        prompt = "Would you like to play again? (y/n): "

    while True:  # Loop forever until the user enters a valid answer
        # Ask the user if they want to play again
        # strip() removes extra spaces
        # lower() converts the input to lowercase so 'Y' and 'y' are treated the same
        again = input(f"\n{prompt}").strip().lower()

        # If the player says yes → restart the game
        if again in ["y", "yes"]:
            return True 

        # If the player says no → end the game
        elif again in ["n", "no"]:
            print(f"Goodbye, {player_name}. Thanks for playing!")
            sys.exit(0)  # Immediately stop the program

        # If the input is anything else
        else:
            print("Invalid input: please enter y or n.")


def explore_forest():
    # This function runs when the player chooses "Explore a forest"

    print(f"\n{player_name}, you step into the forest. Trees whisper, and sunlight filters through leaves.")
    print("You find a hidden path and a sparkling stream. Adventure awaits!")

    while True:  # Keep showing forest options until the player leaves
        print("\nForest choices:")
        print("1. Follow the river")
        print("2. Climb a tree")
        print("3. Return to main menu")

        try:
            # Take input and convert it to an integer
            forest_choice = int(input("Enter 1, 2, or 3: "))

        # If the user enters something that is not a number
        except ValueError:
            print("Invalid input: please enter a number between 1 and 3.")
            continue  # Go back to the start of the loop

        # Choice 1 → Player follows the river and finds treasure
        if forest_choice == 1:
            print(f"\n{player_name}, you follow the river. The water is clear and you spot fish and a small waterfall.")
            print("You discover a cool pool and a hidden glade.")
            print("You discover a treasure chest filled with gold and jewels!")

            # Ask if the player wants to restart the game
            if play_again():
                return "restart"

        # Choice 2 → Player climbs a tree but loses the game
        elif forest_choice == 2:
            print(f"\n{player_name}, you climb a tall tree and enjoy the breathtaking view over the canopy.")
            print("You have made a poor decision and the game ends.")
            if play_again("You have made a poor decision. Would you like to play again? (y/n): "):
                return "restart"
            else:
                return "quit"

        # Choice 3 → Return to main menu
        elif forest_choice == 3:
            print("Returning to the main menu...")
            break

        # If the user enters a number other than 1, 2, or 3
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def enter_cave():
    # This function runs when the player chooses "Enter a cave"

    print(f"\n{player_name}, you step into a shadowy cave. Stalactites hang from the ceiling, and faint blue crystals light the walls.")
    print("The ground is damp and you hear the distant drip of water. A narrow passage stretches deeper into mystery.")

    while True:  # Loop to keep showing cave options
        print("\nCave choices:")
        print("1. Light a torch")
        print("2. Proceed in the dark")
        print("3. Return to main menu")

        cave_choice = input("Enter 1, 2, or 3: ")

        # If player chooses to light a torch
        if cave_choice == "1":
            print("\nTorch is ON. The cave is illuminated and the shadows retreat.")
            print("Two tunnels appear: left and right.")

            while True:
                # Ask the player which direction to go
                direction = input("Choose a direction (left/right): ").strip().lower()

                if direction == "left" or direction == "l":
                    print("You have made a poor decision and the game ends.")
                    if play_again("You have made a poor decision. Would you like to play again? (y/n): "):
                        return "restart"
                    else:
                        return "quit"

                elif direction == "right" or direction == "r":
                    print("You have made a poor decision and the game ends.")
                    if play_again("You have made a poor decision. Would you like to play again? (y/n): "):
                        return "restart"
                    else:
                        return "quit"

                else:
                    print("Invalid input: please enter left or right.")

        # If player walks in the dark
        elif cave_choice == "2":
            print(f"\n{player_name}, the crystal light shows you glittering mineral veins in the rock.")
            print("The cave feels calm and otherworldly, and you sense there is something special further ahead.")
            print("You have made a poor decision and the game ends.")
            if play_again("You have made a poor decision. Would you like to play again? (y/n): "):
                return "restart"
            else:
                return "quit"

        # Return to main menu
        elif cave_choice == "3":
            print("Returning to the main menu...")
            break

        # Invalid input
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def start_game():
    # This function starts the game and shows the main menu

    print("Welcome to the Adventure Game!")

    global player_name  # Allows us to modify the global variable
    player_name = input("What is your name, adventurer? ")

    print(f"Hello, {player_name}! Your adventure begins now.")

    while True:  # Main game loop
        print("\nChoose your action:")
        print("1. Explore a forest")
        print("2. Enter a cave")
        print("3. Quit")

        try:
            # Take input and convert it to an integer
            choice = int(input("Enter 1, 2, or 3: "))

        except ValueError:
            print("Invalid input: please enter a number between 1 and 3.")
            continue

        # Start forest adventure
        if choice == 1:
            result = explore_forest()

            # Restart the game if treasure was found
            if result == "restart":
                return start_game()

        # Start cave adventure
        elif choice == 2:
            cave_result = enter_cave()
            if cave_result == "restart":
                return start_game()

        # Quit the game
        elif choice == 3:
            print(f"Goodbye, {player_name}. Thanks for playing!")
            break

        # Invalid number
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


# This ensures the game runs only when this file is executed directly
if __name__ == "__main__":
    start_game()