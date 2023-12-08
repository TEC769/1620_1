"""
vote_calculator.py - Module for calculating & recording votes.

Provides functions for calculating and recording votes in a CSV.
"""

import csv


def calculate_votes(candidate: str) -> dict:
    """
    Calculate and record the vote for the specified candidate.

    Args:
        candidate (str): The candidate for whom the vote is calculated & recorded.

    Returns:
        dict: A dictionary containing the updated vote counts for each candidate.
    """

    # Perform calculations or other processing based on the candidate (if needed)

    # Update the votes dictionary
    votes = {'John': 0, 'Jane': 0}
    votes[candidate] += 1

    # Save the votes to the CSV file
    save_votes_to_csv(votes)

    return votes


def save_votes_to_csv(votes: dict) -> None:
    """
    Saves the votes to a CSV.

    Args:
        votes (dict): A dictionary containing vote counts for each candidate.

    Returns:
        None
    """

    filename = 'votes.csv'
    fieldnames = ['Candidate', 'Votes']

    # Check if the file exists
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_votes = {row['Candidate']: int(row['Votes']) for row in reader}
    except FileNotFoundError:
        existing_votes = {}

    # Update the votes
    for candidate, votes_count in votes.items():
        if candidate in existing_votes:
            existing_votes[candidate] += votes_count
        else:
            existing_votes[candidate] = votes_count

    # Write the updated votes to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for candidate, votes_count in existing_votes.items():
            writer.writerow({'Candidate': candidate, 'Votes': votes_count})
