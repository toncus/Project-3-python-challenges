# -*- coding: utf-8 -*-
"""
This has some probs in DOB conversion and SSmasking. This is my best attempt with output.
This produced spreadheet submitted. 
This shows my attempt to try to do more, the problems I faced, and attempts to rectify.
Output file is the employee_data_3
@author: Toncus
"""
import os
import csv
from datetime import datetime
rnbr=[]
empid=[]
fname=[]
lname=[]
DOB=[]
SSN=[]
state=[]
year=0
month=0
day=0
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
rownum=0
whole_name=""
first_name=""
last_name=""
ss=""
datasetnames=["employee_data1.csv", "employee_data2.csv"]
for dataset in datasetnames:
    print()
    print()
    csvpath = os.path.join(dataset)
    with open(csvpath, newline='') as csv_file:
        print(dataset)
        csvreader=csv.reader(csv_file, delimiter=",")
        for row in csvreader:
            #skip a row
            rownum=rownum+1
            if rownum>1:
                #Emp ID field
                empid.append(row[0])
                #name field conversion 
                whole_name = row[1]
                first_name=whole_name.split(" ")[0] 
                last_name=whole_name.split(" ")[-1]
                #First Name Field
                fname.append(first_name)
                #Last Name Field
                lname.append(last_name)
                #DOB coversion attempt and DOB Field
                #dob=str(row[2])
                #dob.split('[]')
                #year=(dob[0:4])
                #month=(dob[6:7])
                #day=(dob[9:10])
                #dt=datetime(year, month, day)
                #dateofbirth=datetime.strptime(dt, "%d-%m-%Y")
                #DOB.append((dateofbirth))
        #DOB Field -know this isn't right but did to get some output
                DOB.append(row[2])
                # SS number mask-think it loses actual number
                ss=("XXXXX" + str(row[3][-4:])+"     ")
                SSN.append(ss)
                #State abbreviation to two digits
                for key, value in us_state_abbrev.items():
                    if key==str(row[4]):
                        state.append(value)
    #Out put rows field
    new_csv=zip(empid, fname, lname, DOB, SSN, state)
output_file= os.path.join("employee_data3.csv")        
with open(output_file,'w',newline="") as datafile:
    writer =csv.writer(datafile)
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN','State'])
    writer.writerows(new_csv)