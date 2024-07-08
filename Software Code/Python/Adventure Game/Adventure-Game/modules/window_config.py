import shutil
import os

def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    centered_text = ' ' * padding + text
    return centered_text

def print_centered(text):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    centered = center_text(text)
    print(centered)

