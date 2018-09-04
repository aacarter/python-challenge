import os
import csv

budget_csv = os.path.join('budget_data.csv')

with open(budget_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    total_months = 0

    initial_profit_losses = 0
    profit_losses_change = 0
    #greatest_increase = ["", 0]
    #greatest_decrease = ["", 9999999999999999999999]

    #profitchange = []


    for row in csvreader:
        total_months = total_months + 1
        total += int(row[1])
        value = int(row[1])

        # Keep track of changes
        
        #profit_losses_change = int(row[1]) - initial_profit_losses
        # print(profit_losses_change)

        # Reset the value of initial_revenue to the row I completed my analysis
        #Initial_revenue = value 


    print("Financial Analysis")
    print(value)
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total))
    #print("Average Change: " + "$" + str(round(sum(profitchange) / len(profitchange),2)))
    #print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
    #print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")














        #total = total + value

    #def average(profit):
        #length = len(profit)
        #total = 0.0
        #for number in profit:
         #   total += number
        #return total / length

#print(average(range(11)))

        # Keep track of changes
        #value = int(row[1])
        #value_change = (value) + 1 - 867884
        # print(profit_losses_change) but reserved for later

        # Set the Revenue average
        #avg_profit_losses = sum(profitchange) 
        #/ len(profit_losses_change)

    #print(total_months)   
    #print(total)
    #print(average(row[1]))
    #print (avg_profit_losses)




