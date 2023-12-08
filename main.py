"""
main.py - Main script to run the voting app.

This script initializes the PyQt application, creates an instance of the VoteGUI class,
and runs the main event loop to display the voting GUI.
"""

from vote_gui import *


def main() -> None:
    app = QApplication(sys.argv)
    vote_menu = VoteGUI()
    vote_menu.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
