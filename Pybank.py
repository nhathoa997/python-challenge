import os
import csv

total_months = 0
total_netProfit_Loss = 0
monthly_change1 = monthly_change2 = 0
average_change = 0
total_change = 0
initial = 0
recent = 0
greatest_increase = 0
greatest_decrease = 0


with open('budget_data.csv.csv', "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        total_months += 1
        total_netProfit_Loss += int(row[1])
        recent = int(row[1])

        if initial != 0 and recent != 0:
            monthly_change2 = recent - initial
            if(monthly_change2 >= monthly_change1):
                if(monthly_change2 >= greatest_increase):
                    GI_row = row[0]
                    greatest_increase = monthly_change2
            elif(monthly_change2 < monthly_change1):
                if(monthly_change2 < greatest_decrease):
                    greatest_decrease = monthly_change2
                    GD_row = row[0]


        monthly_change1 = monthly_change2
        total_change += monthly_change2
        print(f"{row[0]}:  {monthly_change2}")
        initial = int(row[1])

    average_change = total_change/(total_months - 1)

    print("Financial Analysis: \n------------------------------------\n")
    print(f"Total Months: {total_months}")
    print(f"Total: $ {total_netProfit_Loss}")
    print(f"Average change: {round(average_change,2)}")
    print(f"Greatest Increase in Profits: {GI_row} ${greatest_increase}")
    print(f"Greatest Decrease in Profits: {GD_row} ${greatest_decrease}")

file_name = "py_bank.txt"
file = open(file_name,'w')

file.writelines("Financial Analysis: \n------------------------------------\n")
file.writelines(f"Total Months: {total_months}")
file.writelines(f"\nTotal: $ {total_netProfit_Loss}")
file.writelines(f"\nAverage change: {round(average_change,2)}")
file.writelines(f"\nGreatest Increase in Profits: {GI_row} ${greatest_increase}")
file.writelines("\nGreatest Decrease in Profits: {GD_row} ${greatest_decrease}")
