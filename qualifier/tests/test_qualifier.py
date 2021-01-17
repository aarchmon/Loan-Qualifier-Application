# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# Import retrievers from utils.
from utils.retrievers import retrievers

def test_save_csv():
    assert Path("../data/output/qualifying_loans.csv").exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filter_credit_score():

    # Bank data.
    bank_data = fileio.load_csv(Path("./data/daily_rate_sheet.csv"))

    # Current credit score.
    current_credit_score = 750

    # Filter bank data per current credit score and save all credit scores in list.
    filtered_bank_data = credit_score.filter_credit_score(current_credit_score, bank_data)
    credit_scores = retrievers.retrieve_credit_scores(bank_data) 

    # Assertion.
    assert all(credit_scores) <= current_credit_score

# def test_filters():
#     
#     debt = 1500
#     income = 4000
#     loan = 210000
#     home_value = 250000

#     monthly_debt_ratio = 0.375

#     loan_to_value_ratio = 0.84
#     assert True