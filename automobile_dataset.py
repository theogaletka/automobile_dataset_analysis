import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools
from pathlib import Path
from scipy import stats


plt.style.use('default')

""" AGENDA:
CURRENT OBJECTIVES:



COMPLETED OGJECTIVES:


"""
#file handler
def load_csv():
    #loads data set
    DATA = Path(__file__).parent / "data_files" / "Automobile_data.csv"

    #case if file is not found
    if not DATA.exists():
        raise FileNotFoundError(f"CSV not found")
    return pd.read_csv(DATA, na_values=["?"])


#finds all data type pairs
def find_all_pairs(columns):
    #finds all unqique pairs of data types,returns list of tuples
    combinations = list(itertools.combinations(columns, 2))
    return combinations


#retuns price and risk or each entry, keeps rows that have valid entries for data type querry
def return_two_values(df, val1, val2):

    df_clean = df.dropna(subset=[val1, val2])
     
    setx = df_clean[val1]
    sety = df_clean[val2] 
        
    return setx, sety


#Creates scatter plot
def scatter(x, y, title, xlabel, ylabel):  
    plt.figure(figsize = (8,8))
    ax = plt.gca()
    ax.scatter(x, y, alpha=0.3)

    #finds the amount of unique values
    unique_x = len(set(x))
    unique_y = len(set(y))
    
    #this section creates a cap at 10 values on each axis
    #and plots the points
    #first if condition checks if the data type is numeric
    
    if pd.api.types.is_numeric_dtype(x) and pd.api.types.is_numeric_dtype(y):
        ax.scatter(x, y, alpha=0.3)
        _add_trend_line(ax, x, y)
        
    
    if pd.api.types.is_numeric_dtype(x):
        if unique_x <= 10:
            #shows all unique values
            x_ticks = sorted(set(x))
            plt.xticks(x_ticks, rotation = 45)
        
        else: 
            #evenly spaced subset capped at 10
            x_min, x_max = min(x), max(x)
            x_ticks = np.linspace(x_min, x_max, 10)
            plt.xticks(x_ticks)
    
    #formats non numerical data for the graph
    else:
        
        x_ticks = sorted(set(x))
        plt.xticks(x_ticks, rotation=45, ha='right')

    if pd.api.types.is_numeric_dtype(y):
        if unique_y <= 10:
            # Show all unique values
            y_ticks = sorted(set(y))
            plt.yticks(y_ticks)
        else:
            # Show evenly spaced subset (cap at 10)
            y_min, y_max = min(y), max(y)
            y_ticks = np.linspace(y_min, y_max, 10)
            plt.yticks(y_ticks)
    
    #formats non numerical data for y axis
    else:
        y_ticks = sorted(set(y))
        plt.yticks(y_ticks)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()


#Program for creating a two dimensional scatter plot
def two_value_scatter_plot(df, xkey, ykey):
    
    #calls return two values and returns two values
    xplot, yplot = return_two_values(df, xkey, ykey)

    #generates title 
    title = (f"{ykey} and {xkey}")

    #scatter plot for the returned values
    scatter(xplot, yplot, title, xkey, ykey)


#alias for two parameter scatter plot
compare = two_value_scatter_plot

#creates a linear regression line and R2 label on axis for numeric functions
def _add_trend_line(ax, x, y):
    slope, intercept, r, _, _ = stats.linregress(x, y)

    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept
    ax.plot(x_line, y_line, 'r--', label=f'y = {slope:.2f}x + {intercept:.2f}\nR² = {r**2:.3f}')
    ax.legend(loc='best')
    

#main
def main():

    #data
    df = load_csv()

    #Pick two data types to compare
    compare(df,'width','normalized-losses') 

#runs main
if __name__ == "__main__":
    main()





