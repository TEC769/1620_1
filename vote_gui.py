"""
vote_gui.py - GUI for the voting app.

Provides a graphical user interface (GUI) for users to vote for a candidate.
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QMessageBox, QWidget
from PyQt6.QtCore import Qt
from vote_calculator import calculate_votes


class VoteGUI(QMainWindow):
    """
    Main class representing the Voting GUI.

    This class defines the graphical user interface for users to cast their votes.
    """

    def __init__(self):
        """
        Initialize the VoteGUI.

        Sets up the main window, layout, labels, and buttons.
        """
        super().__init__()

        self.setWindowTitle("Vote GUI")
        self.setFixedSize(300, 200)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.label = QLabel("Select one of the vote buttons to vote. Select 'Done' when complete.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        main_layout.addWidget(self.label)

        # Buttons for candidates
        self.john_button = QPushButton("Vote for John")
        self.jane_button = QPushButton("Vote for Jane")
        self.done_button = QPushButton("Done")

        main_layout.addWidget(self.john_button)
        main_layout.addWidget(self.jane_button)
        main_layout.addWidget(self.done_button)

        self.john_button.clicked.connect(lambda: self.cast_vote('John'))
        self.jane_button.clicked.connect(lambda: self.cast_vote('Jane'))
        self.done_button.clicked.connect(self.confirm_done)

        # Variable to track the voted candidate
        self.voted_candidate = None

    def cast_vote(self, candidate: str) -> None:
        """
        Cast a vote for the specified candidate.

        Args:
            candidate (str): The candidate for whom the vote is cast.
        """
        # Allow changing the vote before clicking "Done"
        self.voted_candidate = candidate
        self.label.setText(f"Currently voting for: {candidate}")

    def confirm_done(self) -> None:
        """
        Confirm and record the vote.

        Displays a confirmation dialog and records the vote if the user confirms.
        """
        if self.voted_candidate is not None:
            # Display a confirmation dialog
            confirm_dialog = QMessageBox()
            confirm_dialog.setIcon(QMessageBox.Icon.Question)
            confirm_dialog.setText(f"Do you want to submit your vote for {self.voted_candidate}?")
            confirm_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirm_dialog.setDefaultButton(QMessageBox.StandardButton.No)

            button_clicked = confirm_dialog.exec()

            if button_clicked == QMessageBox.StandardButton.Yes:
                # Call the modified calculate_votes function
                calculate_votes(self.voted_candidate)

                # Display a message confirming the vote
                QMessageBox.information(self, 'Vote Recorded',
                                        f"Your vote for {self.voted_candidate} has been recorded.")
                # Close the application
                sys.exit()
        else:
            # Display a message if no vote has been cast
            QMessageBox.warning(self, 'No Vote', 'Please vote before clicking "Done".')
