import csv

#set variables

month = []
revenue = []
revenue_change = [] 
monthly_change = []
budget_file_path = "Resources/budget_data.csv"


# open data file
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    header = next(csv_file)
    # read a row in the file
    # calculate total months
    for row in csv_file:
        month.append(row[0])
        revenue.append(row[1])

    # calculate net revenue over entire period
    # use map function to pull data from each row
    # use int to convert base=10 date to integer
    revenue_int = map(int,revenue)
    net_revenue = (sum(revenue_int))

     # calculate average change over entire period
    current_month = 0
    for current_month in range(len(revenue) - 1):
        profit_loss = int(revenue[current_month+1]) - int(revenue[current_month])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    
    # calculate greatest increase in profits over entire period
    profit_increase = max(revenue_change)
    max_increase = revenue_change.index(profit_increase)
    month_increase = month[max_increase+1]
    
    # calculate greatest decrease in profits over entire period
    # print date and amount
    profit_decrease = min(revenue_change)
    max_decrease = revenue_change.index(profit_decrease)
    month_decrease = month[max_decrease+1]

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(month)}')
print(f'Total: ${net_revenue}')
print(f'Average Change: ${monthly_change}')
print(f'Greatest Increase in Profits: {month_increase} (${profit_increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${profit_decrease})')