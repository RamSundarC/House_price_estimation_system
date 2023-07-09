# House_price_estimation_system

The code is used to forecast the price of house by using multiple linear regression algorithm with two independent variables which are area as x1 and number of rooms as x2 to find dependent variable as price.

A csv file named House.csv, contains 545 rows with 4 columns which is used in the code to forecast the house price.

Pre-requisite to the code:
1.Data file
2.Pandas
3.Matplotlib
4.Numpy

It uses Multiple linear Regression for Y=b0+b1 x1 +b2 x2.
First it calculate the co-efficient for the points and slope then it finds the straight line equation.

Then finds the value of Y for the input are x1 and x2.

Then lastly visualises the data points in a three dimension (3d) scatter plot by the matplotlib library.

Example :

Welcome to House Price Forecasting System
Enter area in sq-feet: 5800
Enter How many number of rooms? 6
How do  you want to see the predicted data? (1.Data/2.Visual Data) 1
Price of house is 2.8677521973369344e+18 rupees
