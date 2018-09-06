import os
import csv

budget_csv = os.path.join('budget_data.csv')

with open(budget_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    total_months = 0
    last = None
    initial_profit_losses = 0
    profit_losses_change = 0


    for row in csvreader:
        total_months = total_months + 1
        total += int(row[1])

        change = []
        value = int(row[1])
        if last is not None:
            change.append(value - last)
        last = value
        print(change)
        #avg_change = sum(change) / len(change)
        #print(max(change))
        #print(min(change))




    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total))

















    #print("Average Change: " + "$" + str(round(sum(change) / len(change),2)))
    #print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
    #print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")








