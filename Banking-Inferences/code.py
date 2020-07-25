# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size, random_state =0)
sample_mean = data_sample["installment"].mean()
sample_std = data_sample["installment"].std()
margin_of_error = (z_critical*sample_std)/(sample_size**(1/2))
confidence_interval = [sample_mean-margin_of_error, sample_mean+margin_of_error]
true_mean = data["installment"].mean()


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(nrows=3, ncols=1)
for i in range (len(sample_size)):
    m = []
    for j in range (1000):
        m.append(data['installment'].sample(n= sample_size[i], random_state=0))
    mean_series = pd.Series(m)
    axes[0].plot(mean_series[0])


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = data['int.rate'].map(lambda x: str(x)[:-1])
data['int.rate'] =  data['int.rate'].astype(float)/100
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'], value=data['int.rate'].mean(), alternative='larger')
if(p_value<0.05):
    inference = 'Reject'
else:
    inference = 'Fail to Reject'


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])
if(p_value<0.05):
    inference = 'Reject'
else:
    inference = 'Fail to Reject'


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
yes_trans = yes.transpose()
no_trans = no.transpose()
observed = pd.concat([yes_trans, no_trans], keys=['Yes', 'No'], axis=1)
chi2, p, dof, ex = chi2_contingency(observed)
if (chi2>critical_value):
    inference = 'Reject'
else:
    inference = 'Fail to Reject'


