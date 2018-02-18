# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
candidateTotalUp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
list_of_candidates=[]
list_of_rows = []
votes_cast = 0
index=0
row_count=1
winner=""
winner_total=0
datasetnames=["election_data_1.csv","election_data_2.csv"]
#        for loop to move through datasets
for dataset in datasetnames:
    csvpath = os.path.join('Resources', dataset)

    # Method 2: Improved Reading using CSV module
    import csv
    with open(csvpath, newline='') as csvfile:
        print(dataset)
    # CSV reader specifies delimiter and variable that holds contents
        csvreader=csv.reader(csvfile, delimiter=',')

    #  Each row is read as a row-build my list of lists
        for row in csvreader:
            list_of_rows.append(row)
            list_of_candidates.append(row[2])
            row_count = row_count + 1
    # get unique list of candidates and sort it alphabetically
my_set_cand=set(list_of_candidates)
uniqueListofCandidates = list(my_set_cand)
uniqueListofCandidates.remove("Candidate")
uniqueListofCandidates.sort()
    # tally votes for each candidate and overll
for i in range(1,row_count-1):
    for candidate in uniqueListofCandidates:
        if candidate==list_of_rows[i][2]:
            index = uniqueListofCandidates.index(candidate)
            candidateTotalUp[index] = candidateTotalUp[index]+1
            votes_cast=votes_cast+1
    # produce my table with winner candidate percentage calculations and all numberformatting
print()
print("    Election  Results    ")
print("-------------------------")
print("Total Votes:   " + str(votes_cast))
print("-------------------------")
for i in range(len(uniqueListofCandidates)):
    uniqueListofCandidates[i]=uniqueListofCandidates[i]+":"
    while len(uniqueListofCandidates[i])<12:
        uniqueListofCandidates[i]=uniqueListofCandidates[i]+" "
    if candidateTotalUp[i]> winner_total:
        winner_total=candidateTotalUp[i]
        winner=(uniqueListofCandidates[i][:-1])
    if (candidateTotalUp[i]/votes_cast*100)<10:
        print(uniqueListofCandidates[i] + " " + str(round(candidateTotalUp[i]/votes_cast*100,1))+" %     ( " + str(candidateTotalUp[i]) + " )")
    else:
        print(uniqueListofCandidates[i] + str(round(candidateTotalUp[i]/votes_cast*100,1))+" %    ( " + str(candidateTotalUp[i]) + " )")

print("-------------------------")

print("Winner:    " + winner.replace(":",""))

# output to txt file by building string and sending it to txt file

output_file = os.path.join("PyPoll.txt")
output_file =open ("PyPoll.txt", 'w')
stringlist = []
stringlist.append("\n")
stringlist.append("\n")
stringlist.append("    Election  Results    "+"\n")
stringlist.append("-------------------------"+"\n")
stringlist.append("Total Votes:   " + str(votes_cast)+"\n")
stringlist.append("-------------------------"+"\n")
for i in range(len(uniqueListofCandidates)):
    if (candidateTotalUp[i]/votes_cast*100)<10:
        stringlist.append(uniqueListofCandidates[i] + " " + str(round(candidateTotalUp[i]/votes_cast*100,1))+" %     ( " + str(candidateTotalUp[i]) + " )"+"\n")
    else:
        stringlist.append(uniqueListofCandidates[i] + str(round(candidateTotalUp[i]/votes_cast*100,1))+" %    ( " + str(candidateTotalUp[i]) + " )"+"\n")

stringlist.append("-------------------------"+"\n")
stringlist.append("Winner:    " + winner.replace(":",""))

output_file.writelines(stringlist)
output_file.close