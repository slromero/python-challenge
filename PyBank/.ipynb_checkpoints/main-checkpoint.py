# Dependencies
import csv
import os

# Set variables
budgetfile = 'Resources/budget_data.csv'
output_file = 'Analysis/financial_analysis_results.txt'

rowcnt = 0
firstamt = 0
lastamt = 0
currentamt = 0
maxchg = 0
minchg = 0
maxmonth = 0
minmonth = 0
net = 0

# Open the file in "read" mode ('r') 
with open(budgetfile,'r') as csvfile:
    
    output_file = open(output_file, 'a')
    
    # Read csvfile contents
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Read each row of data
    for row in csvreader:
        currentamt = int(row[1])
        
        if(rowcnt == 0):
            firstamt = int(row[1])
            lastamt = int(row[1])
        
        if(currentamt - lastamt > maxchg):
            maxchg = currentamt - lastamt
            maxmonth = row[0]
        
        if(currentamt - lastamt < minchg):
            minchg = currentamt - lastamt
            minmonth = row[0]
        
        lastamt = currentamt
        rowcnt += 1
        net += currentamt
            
    chgoverperiod = int(lastamt) - int(firstamt)
    avgamt = round(chgoverperiod/(rowcnt-1),2)
    
    print("\nFinancial Analysis")
    print("__________________________\n")
    print("Total Months: " + str(rowcnt))
    print("\nTotal: $" + str(net))
    print("\nChange: $" + str(chgoverperiod))
    print("\nAverage Change: " + str(avgamt))
    print("\nGreatest Increase in Profits: " + maxmonth + "($" + str(maxchg) + ")")
    print("\nGreatest Decrease in Profits: " + minmonth + "($" + str(minchg) + ")")
    
    output_file.writelines("\nFinancial Analysis\n")
    output_file.writelines("__________________________\n\n")
    output_file.writelines("\nTotal Months: " + str(rowcnt) + "\n")
    output_file.writelines("\nTotal: $" + str(net) + "\n")
    output_file.writelines("\nChange: $" + str(chgoverperiod) + "\n")
    output_file.writelines("\nAverage Change: " + str(avgamt) + "\n")
    output_file.writelines("\nGreatest Increase in Profits: " + maxmonth + " ($" + str(maxchg) + ")\n")
    output_file.writelines("\nGreatest Decrease in Profits: " + minmonth + " ($" + str(minchg) + ")")
    output_file.close()

    
    