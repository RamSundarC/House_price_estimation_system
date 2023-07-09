import pandas as pd 
import matplotlib.pyplot as plt 
import datetime
import numpy as np


print("Welcome to House Price Prediction System") # welcome message

#time.sleep(2) # sleep for 2 seconds

df=pd.read_csv("Housing.csv")
# loading data from csv file





x=list(df['area'])
# converting data into list


y=list(df['bedrooms']) # bedrooms
z=list(df['bathrooms']) # bathrooms
target=list(df['price']) # price


new_y=[]
for u in range(0,len(y)):
    ans=y[u] + z[u]
    new_y.append(ans) # adding bedrooms and bathrooms



def mlr(x,new_y,target): # multiple linear regression
    target=np.array(target) # converting target into numpy array
    x=np.array(x) # converting x into numpy array
    new_y=np.array(new_y) # converting new_y into numpy array
    x1_sq=np.array(x)**2 # x1_sq
    x2_sq=np.array(new_y)**2 # x2_sq
    x1_y=np.array(x)*np.array(target) # x1_y
    x2_y=np.array(new_y)*np.array(target) # x2_y
    x1_x2=np.array(x)*np.array(new_y)  # x1_x2

    sum_x1=sum(np.array(x)) # sum of x1
    sum_x2=sum(np.array(new_y))    # sum of x2
    sum_y=sum(np.array(target))     # sum of y 
    sum_x1_sq=sum(x1_sq)   # sum of x1_sq
    sum_x2_sq=sum(x2_sq)  # sum of x2_sq
    sum_x1y=sum(x1_y)  # sum of x1_y
    sum_x2y=sum(x2_y) # sum of x2_y
    sum_x1_x2=sum(x1_x2) # sum of x1_x2

    #print(f"sum_x1:{sum_x1}\nsum_x2:{sum_x2}\nsum_y:{sum_y},\nsum_x1_sq={sum_x1_sq},\nsum_x2_sq={sum_x2_sq},\nsum_x1y={sum_x1y},\nsum_x2y={sum_x2y},\nsum_x1_x2={sum_x1_x2}")

    f_sum_x1_sq=sum_x1_sq-(sum(x)**2/len(x)) # final sum of x1_sq
    f_sum_x2_sq=sum_x2_sq-(sum(new_y)**2/len(x)) # final sum of x2_sq
    f_sum_x1_y=sum_x1y-(sum_x1*sum_y/len(x)) # final sum of x1_y
    f_sum_x2_y=sum_x2y-(sum_x2*sum_y/len(x)) # final sum of x2_y
    f_sum_x1_x2=sum_x1_x2-(sum_x1*sum_x2/len(x))   # final sum of x1_x2

    #print(f"f_sum_x1_sq:{f_sum_x1_sq}\nf_sum_x2_sq={f_sum_x2_sq}\nf_sum_x1y={f_sum_x1_y}\nf_sum_x2y={f_sum_x2_y},\nf_sum_x1_x2={f_sum_x1_x2}")

    b1=(f_sum_x2_sq*f_sum_x1_y)-(f_sum_x1_x2*f_sum_x2_y)/(f_sum_x1_sq*f_sum_x2_sq)-(f_sum_x1_x2)**2 # b1
    
    b2=(f_sum_x1_sq*f_sum_x2_y)-(f_sum_x1_x2*f_sum_x1_y)/(f_sum_x1_sq*f_sum_x2_sq)-(f_sum_x1_x2)**2 # b2

    b0=target.mean()-b1*x.mean()-b2*new_y.mean() # b0

    #print(f"b0={b0}\nb1={b1}\nb2={b2}")

    global ip1,ip2,sol
    ip1=float(input("Enter area in sq-feet: ")) # input 1
    ip2=float(input("Enter How many number of rooms? ")) # input 2

    sol=int(b0)+int(b1)*(ip1)+int(b2)*(ip2) # solution

    opener_3=input("How do  you want to see the predicted data? (1.Data/2.Visual Data) ") # opener 3
    if opener_3=='1': # if opener 3 is 1
        print(f"Price of house is {sol} rupees") # printing solution
    

    elif opener_3=='2': # if opener 3 is 2

        x1=list(x).append(int(ip1)) # appending ip1 to x1
        x2=list(new_y).append(int(ip2)) # appending ip2 to x2
        y=list(target).append(int(sol)) # appending sol to y

        fig=plt.figure() # creating figure
        ax = fig.add_subplot(111, projection='3d') # adding subplot

        ax.scatter(x,new_y,target,label ='Actual Data') # plotting actual data
        ax.scatter(ip1,ip2,sol,label='Predicted Data') # plotting predicted data

        ax.set_xlabel('Area(in sq-feet)',color='r') # setting x label
        ax.set_ylabel('Bedrooms(in numbers)',color='g') # setting y label
        ax.set_zlabel('Price(in rupees)',color='purple') # setting z label
        ax.set_title("Price of house",c='b') # setting title
        ax.legend()
        plt.show() # showing plot



mlr(x,new_y,target) # calling mlr function


