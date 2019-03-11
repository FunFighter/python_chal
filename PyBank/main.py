import os
import csv
#import numpy as np

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

def currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#[0] = date [1]= gain/loss
def Financial_Analysis(budget):
    total_months = count(budget[0])
    #TotalProLoss
    total_returns = sum(int(budget[1]))

    #AvgChanges
    AvgChanges = sum(int(budget[1]))/count(budget[1])
    #sort data
    sorted_data = sorted(budget[1])

    #GreatestProfit
    GreatestProfit = sorted_data[0]
    
    #[item[0] for item in sorted_data] for a larger group first items
#def GreatestDecrease():
    GreatestDecrease = sorted_data[-1]

    print(f"Total Months: {total_months}")
    print(f"Total: {currency(total_returns)}")
    print(f"Average Change: {currency(AvgChanges)}")
    print(f"Greatest Increase: {currency(GreatestProfit)}")
    print(f"Greatest Decrease: {currency(GreatestDecrease)}")
