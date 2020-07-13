# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
df_fico = df[df['fico']>700]
len_fico = len(df_fico)
total = len(df)
p_a = len_fico/total
df1 = df[df['purpose']=='debt_consolidation']
len_df1 = len(df1)
p_b = len_df1/total
p_b_a = len_fico/len_df1
p_a_b = (p_b_a*p_b)/p_a
result = p_b_a == p_a
print("Independency:", result)

# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan']=='Yes'].shape[0]/total
prob_cs = df[df['credit.policy']=='Yes'].shape[0]/total
new_df = df[df['paid.back.loan']=='Yes']
new_df1 = df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')]
prob_pd_cs = (len(new_df1)/total)/prob_lp
bayes = (prob_pd_cs * prob_lp)/prob_cs

# code ends here


# --------------
# code starts here
plt.bar(df.index, df['purpose'])
df1 = df[df['paid.back.loan']=='No']
plt.bar(df1.index, df1['purpose'])


# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
plt.hist(df['installment'])
plt.hist(df['log.annual.inc'])


# code ends here


