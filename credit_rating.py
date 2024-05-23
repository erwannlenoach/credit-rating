import os
import pandas as pd
import numpy as np

# Define the sample data structure
np.random.seed(42)  # For reproducibility

# Define the credit ratings as per Moody's scale
credit_ratings = ['Aaa', 'Aa', 'A', 'Baa', 'Ba', 'B', 'Caa', 'Ca', 'C']

import numpy as np

def determine_credit_rating(borrower_credit_score, debt_to_income_ratio, loan_to_value_ratio, 
                            annual_income, loan_amount, interest_rate, collateral_value, 
                            economic_growth_rate, unemployment_rate):
    # Factors weights based on their importance
    credit_score_weight = 0.35
    dti_weight = 0.15
    ltv_weight = 0.10
    income_weight = 0.10
    loan_amount_weight = 0.10
    interest_rate_weight = 0.05
    collateral_weight = 0.05
    economic_growth_weight = 0.05
    unemployment_weight = 0.05

    # Normalize inputs
    max_credit_score = 850
    max_income = 200000
    max_loan_amount = 500000
    max_interest_rate = 15
    max_collateral_value = 1000000
    max_growth_rate = 0.1  # 10%
    max_unemployment_rate = 0.1  # 10%

    # Calculate normalized values
    normalized_credit_score = borrower_credit_score / max_credit_score
    normalized_dti = 1 - debt_to_income_ratio  # Lower DTI is better
    normalized_ltv = 1 - loan_to_value_ratio / 1.2  # Assuming 120% as very high risk
    normalized_income = annual_income / max_income
    normalized_loan_amount = 1 - loan_amount / max_loan_amount  # Lower loan amount is better
    normalized_interest_rate = 1 - interest_rate / max_interest_rate  # Lower interest rate is better
    normalized_collateral = collateral_value / max_collateral_value
    normalized_growth_rate = (economic_growth_rate + 0.05) / max_growth_rate  # Adjust to a 0-1 scale
    normalized_unemployment_rate = 1 - unemployment_rate / max_unemployment_rate  # Lower unemployment is better

    # Calculate overall score
    score = (normalized_credit_score * credit_score_weight +
             normalized_dti * dti_weight +
             normalized_ltv * ltv_weight +
             normalized_income * income_weight +
             normalized_loan_amount * loan_amount_weight +
             normalized_interest_rate * interest_rate_weight +
             normalized_collateral * collateral_weight +
             normalized_growth_rate * economic_growth_weight +
             normalized_unemployment_rate * unemployment_weight)


    # Determine credit rating based on  score
    if score > 0.9:
        return np.random.choice(['Aaa', 'Aa'])
    elif score > 0.8:
        return 'A'
    elif score > 0.7:
        return 'Baa'
    elif score > 0.6:
        return 'Ba'
    elif score > 0.5:
        return 'B'
    elif score > 0.4:
        return 'Caa'
    elif score > 0.3:
        return 'Ca'
    else:
        return 'C'


# Function to simulate realistic data
def generate_sample_data(num_samples):
    borrower_credit_score = np.random.randint(300, 850, num_samples)
    debt_to_income_ratio = np.random.uniform(0.1, 0.6, num_samples)
    loan_to_value_ratio = np.random.uniform(0.5, 1.2, num_samples)
    annual_income = np.random.uniform(30000, 200000, num_samples)
    loan_amount = np.random.uniform(5000, 500000, num_samples)
    collateral_value = np.random.uniform(10000, 1000000, num_samples)
    
    # Economic indicators
    unemployment_rate = np.random.uniform(0, 0.1, num_samples)
    economic_growth_rate = 0.05 - unemployment_rate  # Inversely related

    # Interest rate based on debt_to_income_ratio, annual_income, and collateral_value
    interest_rate = (0.15 * debt_to_income_ratio 
                     + 0.02 * (1 - annual_income / 200000)
                     + 0.02 * (1 - collateral_value / 1000000)) * 15

    credit_ratings = [determine_credit_rating(borrower_credit_score[i], debt_to_income_ratio[i], 
                                              loan_to_value_ratio[i], annual_income[i], loan_amount[i], 
                                              interest_rate[i], collateral_value[i], economic_growth_rate[i], 
                                              unemployment_rate[i]) for i in range(num_samples)]

    data = {
        "Loan_ID": np.arange(1, num_samples + 1),
        "Borrower_Credit_Score": borrower_credit_score,
        "Debt_to_Income_Ratio": debt_to_income_ratio,
        "Loan_to_Value_Ratio": loan_to_value_ratio,
        "Annual_Income": annual_income,
        "Loan_Amount": loan_amount,
        "Interest_Rate": interest_rate,
        "Loan_Term_Years": np.random.randint(1, 30, num_samples),
        "Collateral_Value": collateral_value,
        "Industry_Sector": np.random.choice(['Technology', 'Healthcare', 'Finance', 'Real Estate', 'Consumer Goods', 'Energy'], num_samples),
        "Credit_History_Length_Years": np.random.randint(1, 30, num_samples),
        "Past_Due_Payments": np.random.randint(0, 10, num_samples),
        "Current_Economic_Growth_Rate": economic_growth_rate,
        "Consumer_Confidence_Index": np.random.uniform(0, 1, num_samples),
        "Business_Confidence_Index": np.random.uniform(0, 1, num_samples),
        "Unemployment_Rate": unemployment_rate,
        "Inflation_Rate": np.random.uniform(0, 1, num_samples),
        "GDP_Growth_Rate": np.random.uniform(0, 1, num_samples),
        "Loan_Type": np.random.choice(['Corporate', 'Government', 'Personal'], num_samples),
        "Credit_Rating": credit_ratings
    }
    
    return pd.DataFrame(data)

# Create a directory in your local path if it doesn't exist
output_dir = "credit_rating_data"
os.makedirs(output_dir, exist_ok=True)

# Generate sample data
num_samples = 10000
df = generate_sample_data(num_samples)

df.to_csv("data.csv", index=False)


