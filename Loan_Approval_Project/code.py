# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path) # create dataframe 'bank_data' to pass path file


#Code starts here
categorical_var = bank_data.select_dtypes(include = 'object') # checking all categorical values of objects
numerical_var = bank_data.select_dtypes(include = 'number') # checking all categorical values of number
banks = bank_data.drop(['Loan_ID'],axis = 1) # remove 'Loan_ID' column using drop()
print(banks.isnull().sum()) # to checking null values
bank_mode = banks.mode() # calculate mode of banks dataframe
banks.fillna(bank_mode.iloc[0]) # filling NaN values with bank_mode values 
avg_loan_amount = banks.pivot_table(index =['Gender','Married','Self_Employed'],values = ['LoanAmount'],aggfunc = np.mean) # check loan amount of average person according to 'Gender','Married','Self_Employed'
print(avg_loan_amount)

loan_approved_se =banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]

loan_approved_nse =banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
percentage_se  = (len(loan_approved_se)/ 614) * 100
percentage_nse = (len(loan_approved_nse) / 614) * 100
print(np.round(percentage_se,2))
print(np.round(percentage_nse,2))

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 )
big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)

loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.agg(np.mean)
print(np.round(mean_values,2))





