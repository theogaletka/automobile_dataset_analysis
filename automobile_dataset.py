import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import math
import itertools


plt.style.use('default')

""" AGENDA:
CURRENT OBJECTIVES:


test branch
-Create seaborn heatmap or correlation matrix (using the column pairs)
-analyze whitch makes have certain charachteristics(Price prediciton, risk, etc.)
-Create a for loop that can run all posssible parameter combos and analyse them for correlation
-new message
-change 


COMPLETED OGJECTIVES:

-Create a dynamic scatter plot function COMPLETE
-Create a scatter plot of risk asociated with year COMPLETE

"""

#loads data set
df = pd.read_csv('/Users/theogaletka/Documents/General_Code/data projects/data_files/Automobile_data.csv', na_values=['?'])

#finds all data type pairs
def find_all_pairs(columns):
    #finds all unqique pairs of data types,returns list of tuples
    combinations = list(itertools.combinations(columns, 2))
    return combinations

# Get all column names
all_columns = df.columns.tolist()

# All pairs
column_pairs = find_all_pairs(all_columns)

#gets list of manufacturers
unique_makes = df['make'].unique()

#retuns price and risk or each entry, keeps rows that have valid entries for data type querry
def return_two_values(val1, val2):

    df_clean = df.dropna(subset=[val1, val2])
     
    setx = df_clean[val1]
    sety = df_clean[val2] 
        
    return setx, sety

#alias for value pair getter
getter = return_two_values

#prints list of unique makes 
def print_get_makes():
    
    unique_makes = df['make'].unique()

    print("All unique car makes in the dataset:")
    print("=" * 40)

    for make in unique_makes:
        print(make)
    return 

#Creates scatter plot
def scatter(x, y, title, xlabel, ylabel):  
    plt.figure(figsize = (8,8))
    plt.scatter(x, y, alpha=0.3)

    #finds the amount of unique values
    unique_x = len(set(x))
    unique_y = len(set(y))
    
    #this section creates a cap at 10 values on each axis
    #and plots the points
    if unique_x <= 10:
        #shows all unique values
        x_ticks = sorted(set(x))
        plt.xticks(x_ticks, rotation = 45)
    
    else: 
        #evenly spaced subset capped at 10
        x_min, x_max = min(x), max(x)
        x_ticks = np.linspace(x_min, x_max, 10)
        plt.xticks(x_ticks)


    if unique_y <= 10:
        # Show all unique values
        y_ticks = sorted(set(y))
        plt.yticks(y_ticks)
    else:
        # Show evenly spaced subset (cap at 10)
        y_min, y_max = min(y), max(y)
        y_ticks = np.linspace(y_min, y_max, 10)
        plt.yticks(y_ticks)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()

    return 

#Program for creating a two dimensional scatter plot
def two_value_scatter_plot(xkey, ykey):
    
    #calls return two values and returns two values
    xplot, yplot = getter(xkey, ykey)

    #generates title 
    title = (f"{ykey} and {xkey}")

    #scatter plot for the returned values
    scatter(xplot, yplot, title, xkey, ykey)

#alias for two parameter scatter plot
compare = two_value_scatter_plot

#Creates multi value bar chart
def multi_value_bar_chart():

    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    product_a = [20, 35, 30, 35]
    product_b = [25, 32, 34, 20]
    product_c = [30, 25, 30, 25]

    x = np.arange(len(categories))
    width = 0.25 

    plt.figure(figsize=(10, 6))

    plt.bar(x - width, product_a, width, label='Product A', color='#FF6B6B')

    plt.bar(x, product_b, width, label='Product B', color='#4ECDC4')

    plt.bar(x + width, product_c, width, label='Propduct C', color='#95E1D3')

    plt.xlabel('Quarter')
    plt.ylabel('Sales')
    plt.title('Quarterly Sales Comparison')
    plt.xticks(x, categories)
    plt.legend()
    plt.grid(True, alpha= 0.3, axis= 'y')
    plt.show()
    return 

#creates alias
mvbc = multi_value_bar_chart


#Pick two data types to compare
compare('price', 'engine-size') 






