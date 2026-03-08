import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.ui.app import main
import flet as ft

if __name__ == "__main__":
    ft.app(target=main)