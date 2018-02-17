# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
choice = 0
datasetname=["budget_data_1.csv", "budget_data_2.csv"]
for choice in range(1,3):
    total_months = 0
    total_revenue = []
    datecoll=[]
    totRev = 0
    begRev=0
    greatestInc=0
    greatestDec=0
    greatDecdate='Sep-06'
    greatIncdate='Sep-06'
    TotRevChange=0
    print()
    print("          Datasets          ")
    print("1. " + datasetname[0])
    print("2. " + datasetname[1])

    print()
    print()
    print("Dataset number " + str(choice))
    print(datasetname[int(choice-1)])
    csvpath = os.path.join('Resources', datasetname[int(choice-1)])    

    import csv
    with open(csvpath, newline='') as csvfile:
    
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
    
        # Prints the object
        #print(csvreader)
    
        #  Each row is read as a row
        for row in csvreader:
            
            #print(total_months, row,)
            if total_months > 0:
                total_revenue.append(row[1])
                datecoll.append(row[0])
            total_months = total_months + 1
          

    for month in range(0,total_months-1):

            
        if int(total_revenue[month]) > greatestInc:
           greatestInc = int(total_revenue[month])
           greatIncdate=datecoll[month]
            
        if int(total_revenue[month]) < greatestDec:
            greatestDec = int(total_revenue[month])
            greatDecdate=datecoll[month]
        totRev = totRev + int(total_revenue[month])

        TotRevChange=totRev-begRev
        if month==0:
            begRev=int(total_revenue[month])
        else:
            avgAbsTotRevChange=round(TotRevChange/(total_months-1),2)    
    
    print()
    print()
    print("Total Months                 ", total_months-1)
    print("Total Revenue                ", '${}'.format(totRev))
    print("Average Revenue Change       ", '${}'.format(avgAbsTotRevChange,",.2f"))
    print("Greatest Increase In Revenue:", greatIncdate, '(${})'.format(greatestInc))
    print("Greatest Decrease In Revenue:", greatDecdate, '(${})'.format(greatestDec))    
    output_file = os.path.join("PyBank.txt")
    if choice==1:
        output_file =open ("PyBank.txt", 'w')
    else:
        output_file =open ("PyBank.txt", 'a')
    stringlist = []
    stringlist.append("\n")
    stringlist.append("\n")
    stringlist.append("          Datasets          "+"\n")
    stringlist.append("1. " + datasetname[0]+"\n")
    stringlist.append("2. " + datasetname[1]+"\n")
    stringlist.append("\n")
    stringlist.append("Dataset number " + str(choice-1)+"\n")
    stringlist.append(datasetname[(choice-1)]+"\n")
    stringlist.append("\n")
    stringlist.append("Total Months                 " + str(total_months-1) +"\n")
    stringlist.append("Total Revenue                " +'${}'.format(totRev) +"\n")
    stringlist.append("Average Revenue Change       " + '${}'.format(str(avgAbsTotRevChange),",.2f") +"\n")
    stringlist.append("Greatest Increase In Revenue:" + greatIncdate + ' (${})'.format(greatestInc)+"\n")
    stringlist.append("Greatest Decrease In Revenue:"+ greatDecdate + ' (${})'.format(greatestDec)+"\n")
    output_file.writelines(stringlist)
    output_file.close
    