import numpy as np
import pandas as pd

csv_budget = pd.read_csv("../Resources/budget_data.csv",parse_dates=True)

def currency(amount):
    if amount >= 0:
        #str $+numbers.2 dec places 
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#[0] = date, [1]= gain/loss
def Financial_Analysis(budget):

    date = budget["Date"]
    proloss = budget["Profit/Losses"]
    
    #Total Months
    total_months = date.count()
    
    #TotalProLoss
    total_returns = proloss.sum()

    #AvgChanges
    avg_changes = proloss.mean()
    
    #GreatestProfit
    greatest_profit = proloss.max()
    
    #greatestloss
    greatest_loss = proloss.min()


    print(f"Total Months: {total_months}")
    print(f"Total: {currency(total_returns)}")
    print(f"Average Change: {currency(avg_changes)}")
    print(f"Greatest Increase: {currency(greatest_profit)}")
    print(f"Greatest Decrease: {currency(greatest_loss)}")
    
with open("Output.txt", "w") as text_file:
    print(f"Total Months: {total_months}")
    print(f"Total: {currency(total_returns)}")
    print(f"Average Change: {currency(avg_changes)}")
    print(f"Greatest Increase: {currency(greatest_profit)}")
    print(f"Greatest Decrease: {currency(greatest_loss)}")

Financial_Analysis(csv_budget)