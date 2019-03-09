import csv

#IO
input_file = 'c:/data/budget_data.csv'
output_file = 'c:/data/budget_output.txt'

# Variables
total_months = []
total_profit = []
monthly_profit_change = []
 

with open(input_file,newline="", encoding="utf-8") as budget:

    csvreader = csv.reader(budget,delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 

        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        
        # difference between two months 
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Max and min of profit change
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min month 
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

output = (
f"Financial Analysis"
f"\n--------------------------"
f"\nTotal Months: {len(total_months)}"
f"\nTotal: ${sum(total_profit)}"
f"\nAverage Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}"
f"\nGreatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})"
f"\nGreatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})"
)

#print to screen
print(output)

#write to file
with open(output_file, "w") as txt_file:
    txt_file.write(output)