# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


# Saves qualifying loans as a .csv file.
def save_csv(qualifying_loans):
    """
    Saves qualifying loans per user information into a .csv file.

    Args:
        qualifying_loans (List): Qualifying loans in a List data structure.

    Returns:
        NONE
    """

    # Set the output header.
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    # Write qualifying_loans to a new .csv file named 'qualifying_loans.csv'.
    print("\nCommencing data writing...")
    with open("./data/output/qualifying_loans.csv", "w", newline = "") as f:
        csvwriter = csv.writer(f)

        # Write header to file.
        csvwriter.writerow(header)

        # Append all qualifying loans into the .csv file. 
        for loan in qualifying_loans:
            csvwriter.writerow(loan)
    
    print(".csv file successfully written! \n")