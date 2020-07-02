# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind = 'bar')

#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
property_and_loan.plot(kind = 'bar', stacked = False)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind = 'bar', stacked = True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
plt.violinplot(graduate['LoanAmount'].values)
plt.violinplot(not_graduate['LoanAmount'].values)

#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1)
ax_1 = plt.scatter(data['ApplicantIncome'], data['LoanAmount'], label = 'Applicant Income')
ax_2 = plt.scatter(data['CoapplicantIncome'], data['LoanAmount'], label = 'Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3 = plt.scatter(data['TotalIncome'], data['LoanAmount'], label = 'Total Income')


