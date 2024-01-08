# Dependencies
import csv

# Set variables
electionfile = 'Resources/election_data.csv'
output_file = 'Analysis/election_analysis_results.txt'

candidates = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
votes = [0, 0, 0]
totalvotes = 0
maxvotes = 0

# Open the file in "read" mode ('r') 
with open(electionfile,'r') as csvfile:
    
    output_file = open(output_file, 'a')
    
    # Read csvfile contents
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Read each row of data
    for row in csvreader:
        for name in candidates:
            if(name == row[2]):
                pos = int(candidates.index(name))
                candidate = candidates.index(name)
                votes[pos] += 1
        totalvotes +=1
    
    print("\nElection Results\n")
    print("__________________________\n")
    print("Total votes: " + str(totalvotes) +"\n")
    print("__________________________\n")
    for i in range(len(candidates)):
        print(candidates[i] + ": " + str(round(float(votes[i]/totalvotes) * 100,3)) + "% (" + str(votes[i]) + ")\n")
        if(votes[i] > maxvotes):
            maxvotes = votes[i]
            maxindex = i
    print("__________________________\n")        
    print("Winner: " + candidates[maxindex] + "\n")
    print("__________________________\n")
    
    
    
    output_file.writelines("Election Results\n")
    output_file.writelines("__________________________\n")
    output_file.writelines("\nTotal votes: " + str(totalvotes) + "\n")
    output_file.writelines("__________________________\n")
    for i in range(len(candidates)):
        output_file.writelines("\n" + candidates[i] + ": " + str(round(float(votes[i]/totalvotes) * 100,3)) + "%  (" + str(votes[i]) + ")\n")
        if(votes[i] > maxvotes):
            maxvotes = votes[i]
            maxindex = i
    output_file.writelines("__________________________\n")
    output_file.writelines("\nWinner: " + candidates[maxindex] + "\n")
    output_file.writelines("__________________________\n") 