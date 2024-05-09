import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# A bank issues credit cards undeer the scheme of Master Card. Based on the past data, the bank has found out that 60% of all accounts pay their bills on time. If a sample of 7 accounts are selected from the current database, construct the binomial distribution of acounts paying on time.

n= 7 # no. of records selected to be found probability on
p= 0.60 # possibility of success 
k = np.arange(1,80) # an array consisting those 7 accounts
print(k)

binomial_distribution = stats.binom.pmf(k, n, p)
print(binomial_distribution)


plt.plot(k, binomial_distribution, 'o-')
plt.title("Binomial Distribution for n=%d and p=%.2f" %(n, p)) 
plt.xlabel("Number of succcess")
plt.ylabel("Probability of succcess")
plt.show()
