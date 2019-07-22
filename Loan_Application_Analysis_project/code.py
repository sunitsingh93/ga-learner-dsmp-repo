# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
categorical_var

numerical_var = bank.select_dtypes(include = 'number')
numerical_var

# code ends here


# --------------
# code starts here

banks = bank
#code ends here
banks = bank.drop(columns = 'Loan_ID')
#banks

print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
print(bank_mode)
#banks_mode
banks = banks.fillna(bank_mode)
banks.isnull().sum()


# --------------
# Code starts here




# code ends here
avg_loan_amount = pd.pivot_table(data = banks, index = ['Gender','Married','Self_Employed'], values = 'LoanAmount')
avg_loan_amount


# --------------
# code starts here

loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
loan_approved_se
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
loan_approved_nse

# code ends here

banks['Loan_Status'].count()

percentage_se = loan_approved_se * 100/614
percentage_se

percentage_nse = loan_approved_nse * 100/614
percentage_nse


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)

big_loan_term = len(loan_term[loan_term >= 25])
big_loan_term


# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']

loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

mean_values=loan_groupby.agg([np.mean])
# code ends here
print(mean_values)


