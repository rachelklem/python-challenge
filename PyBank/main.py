import csv

#set variables
header = []
budget_file_path = "Resources/budget_data.csv"
total_months = 0
current_month_total = 0
previous_month_total = 0
total_profits_losses = 0
total_change = 0
changes = []
average_change = 0
greatest_increase = 0
greatest_decrease = 0

# open data file
with open(budget_file_path) as budget_file:
    csv_file = csv.reader(budget_file)
    header = next(csv_file)
    #read a row in the file
    for row in csv_file:
        # Total number of months included in the dataset
        total_months +=1
        # Net total amount of "Profits/Losses" over the entire period
        current_month_total = int(row[1])
        # calculate average change over entire period
        if total_months > 1:
            monthly_change = current_month_total - previous_month_total
            changes.append(monthly_change)
            total_change += monthly_change
            # convert total_change value to currency
            average_change = total_change / len(changes)
            # convert average_change to currency
        
            # find greatest increase in profits
            
        if total_profits_losses > 1:
            greatest_increase = int(row[1])
            print(max(greatest_increase))

        # find greatest decrease in profits
        if total_profits_losses > 1:
            greatest_decrease = int(row[1])
            print(min(greatest_decrease))



# Greatest increase in profits over the period
    #date and amount
#Greatest decrease in profits over the period
    #date and amount

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {total_change}')
print(f'Average Change: {average_change}')


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)