import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
outfile = os.path.join('budget_data.txt')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_months = 0
    total_net = 0
    prev_net = 0
    net_change = 0
    net_month_average = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999999999999]
    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        if total_months > 1:
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])

            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change
            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change

        else:
            prev_net = int(row[1])
            firstrev = int(row[1])

    net_month_average = (int(row[1]) - firstrev) / (total_months - 1)

    output = (f"\nFiancial Analysis\n"
              f"---------------------\n"
              f"Total Months: {total_months}\n"
              f"Total: $ {total_net}\n"
              f"Average Change: $ {net_month_average:.2f}\n"
              f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]}) \n"
              f"Greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]}) \n")
    print(output)

    with open(outfile, "w") as textfile:
        textfile.write(output)
