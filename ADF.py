from pandas import read_csv
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot

file_name = "Greece Births.csv"

# Reading the data
series = read_csv(file_name, header=0, index_col=0, squeeze=True)

# Visualizing the data
series.plot()
pyplot.show()

# ADF testing
X = series.values
result = adfuller(X)
pValue = result[1]
print('ADF Statistic:\n{}\n'.format(result[0]))
print('p-Value:\n{}\n'.format(result[1]))
print('Critical Values:')
for key, value in result[4].items():
	print('{}: {}'.format(key, value))
if pValue >= 0.1:
	print("\nNull Hypothesis cannot be rejected. The time series is non-stationary")
elif 0.1 > pValue >= 0.5:
	print("\nNull hypothesis is rejected at significance level a = 0.1. The time series is stationary")
elif 0.5 > pValue >= 0.1:
	print("\nNull hypothesis is rejected at singificance level a = 0.05. The time series is stationary")
elif 0.1 > pValue:
	print("\nNull hypothesis is rejected at singificance level a = 0.01. The time series is stationary")