import os
import csv 

# path created to collect data from resource folder
csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
net_profit = 0
average_change = 0 
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]

# # open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    jan_data = next(csvreader)
    total_months = total_months + 1
    net_profit = net_profit + int(jan_data[1])

    previous_data = int(jan_data[1]) 
    
    for row in csvreader:
        total_months = total_months + 1
        net_profit = net_profit + int(row[1])
        change = int(row[1]) - previous_data   
        previous_data = int(row[1]) 
        net_change_list += [change]

        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row[0]

        if change < greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = row[0]

print("Budget Data Analysis")
print("---------------------------")
print("Total Months:", total_months)
print("Total:", "$", net_profit)
average_change = round(sum(net_change_list)/len(net_change_list),2)
print("Average Change:", "$",average_change)
print("Greatest Increase in Profits:", greatest_increase[0], "$",greatest_increase[1])
print("Greatest Decrease in Profits:", greatest_decrease[0], "$",greatest_decrease[1])

outputpath = os.path.join("Analysis", "budget_results.txt")
with open(outputpath, 'w') as textfile:
    csv_writer = csv.writer(textfile)
    textfile.write(
     
"Budget Data Analysis"
    "\n"
"---------------------------"
    "\n"
f"Total Months: {total_months}"
    "\n"
f"Total: ${net_profit}"
    "\n"
f"Average Change: ${average_change}"
    "\n"
f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}"
    "\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}"
    "\n"
)