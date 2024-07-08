# Description: Our First Python Game!
# Author(s): Colin, Cody
# Date: July 2, 2024 - 

# import libraries
from modules import window_config as wc
from modules import dung_build as dungb
import time


# main game loop
def main():
    wc.print_centered("Welcome to the RPG Adventure")
    time.sleep(3)

    playerName = input(f"\nEnter Your Name: ")
    time.sleep(1)
    print(wc.center_text(playerName))
    print(wc.center_text(f"Welcome, {playerName}!"))

    # Game loop
    while True:
        # Display game options
        print("\nWhat do you want to do?")
        print("1. Explore the dungeon")
        print("2. Talk to the NPC")
        print("3. Quit\n")
        while True:
            choice = input("Enter your choice: ")

            if choice == '1':
                time.sleep(1)
                dungb.explore_dungeon()
            elif choice == '2':
                time.sleep(1)
                dungb.talk_to_npc()
            elif choice == '3':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Try again.")

        break

if __name__ == "__main__":
    main()
