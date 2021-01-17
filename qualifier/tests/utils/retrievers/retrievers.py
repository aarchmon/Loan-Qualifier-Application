# Import calculators.
from qualifier.utils import calculators

# Import filters.
from qualifier.filters import (
    credit_score,
    debt_to_income,
    loan_to_value,
    max_loan_size
)

# Retrieve credit scores from .csv file.
def retrieve_credit_scores(bank_data):
    """
    Retrieves all of the credit scores from a set of bank data (.csv format).

    Args:
        bank_data (csv): .csv format of bank data.
    
    Returns: 
        credit_scores (List): List of credit scores from bank data.
    """

    credit_scores = []
    for bank in bank_data:
        credit_scores.append(bank[4])
    
    return credit_scores

# Retrieve 