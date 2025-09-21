"""
    Contains utility functions
"""
import os

def clear_screen():
    """Function to clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
