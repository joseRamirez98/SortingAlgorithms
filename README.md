# SortingAlgorithms

This python program is an extention of.

##  Calculation for the moving average.

First, prompt the user to input a window period for which they would like to calculate the moving average. Then create a range for the years to be used for the calculation, which is found through using the first year in the csv file + (plus) the window period and the last year in the csv file - (minus) the window period. For example, the first year in the csv file is 1880 and the last is 2018. Given a 60 year window period, the range for this calculation is 1940-1958. Now, let i equal a year contained within the given range, and let k equal the specified window period. The calculation goes as follows: moving_average = (i-k.temperature + ... + i-2.temperature + i-1.temperature + i.temperature + i+1.temperature + i+2.temperature + ... + i+k.temperature) / (2 * k + 1). In the stated example, to calculate the moving average temperture for the year 1940, sum the temperature values from 1880 through 2000 and divide by two times the window period plus one. This process would be repeated for all the years contained in the range.

### Prerequisites

The prerequisite for this program is the "NorCal-1880-2018" csv file, which is included in the repository.

### Example Output
Given a window period of 60, the output of the moving_average csv file should be the following:

Year:    1940     1941    1942  ...   1956    1957     1958
