# Modules
import csv
import os

# Path for input file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Define variables
total_months = 0
total_revenue = 0
total_profit = []
profit = 0
sum_profit = 0
sum_loss = 0
monthly_profit_change = []
month_list = []

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # For loop to count the total months
    for row in csvreader:
        total_months += 1

        # Formula to count the total revenue
        profit = int(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum_loss = sum_loss + profit
        
        # Keep list for months and profits
        total_profit.append(int(row[1]))
        month_list.append(row[0])
    
    # for loop to make list of changes in profit between months
    for i in range(len(total_profit)-1):
         monthly_profit_change.append(total_profit[i+1]-total_profit[i])
    
    # find the greatest increase and decrease in profits
    max_increase = max(monthly_profit_change)
    max_decrease = min(monthly_profit_change)

    # find the index of the month that the greatest increase decrease occurs in
    max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

    # Formula to determine final revenue
    total_revenue = sum_profit + sum_loss

# Print final results
print("```text")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change = ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {month_list[max_increase_month]} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {month_list[max_decrease_month]} (${str(max_decrease)})")
print("'''")

# Path for output file
output_file = os.path.join(".", "analysis", "financial_analysis_results.txt")

# Write to the text file
with open(output_file,"w") as file:
    file.write("```text")
    file.write("\n")
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${total_revenue}")
    file.write("\n")
    file.write(f"Average Change = ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {month_list[max_increase_month]} (${str(max_increase)})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {month_list[max_decrease_month]} (${str(max_decrease)})")
    file.write("\n")
    file.write("'''")
