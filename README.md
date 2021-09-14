# ADF
A simple implementation of Augmented Dickey–Fuller test to determine stationarity of time series. The script takes input a .csv file, creates a graph of the data and returns ADF statistic, p-value, critical values and test results at singificance levels 1%, 5% and 10%

# Example

Data: Births in Greece between the years 1950-2020

![Figure_1](https://user-images.githubusercontent.com/58198596/133328065-8751f4db-83c2-41e5-a03a-6cd16eb84094.png)

Results:

        ADF Statistic:
        -0.31712689342853145

        p-Value:
        0.9230433813636383

        Critical Values:  
        1%: -3.5463945337644063
        5%: -2.911939409384601
        10%: -2.5936515282964665

        Null Hypothesis cannot be rejected. The time series is non-stationary
