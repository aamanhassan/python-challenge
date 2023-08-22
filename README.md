# python-challenge
Python Challenge

import csv
import os

#files to upload and output
file_to_load = os.path.join(".","Resources","election_data.csv")
file_to_output = os.path.join(".","election_analysis.text") 


total_votes = 0

candidate_votes = {}

candidate_options = []

winning_candidates = ""

winning_count = 0

#read file to load
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #read header
    header = next(reader)
    
    for row in reader:
        
        
        #calculate total votes count
        total_votes = total_votes + 1
        
        #complete list of candidates who received votes
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            
            #adding list of candidates 
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name]= 0
            
        candidate_votes[candidate_name]= candidate_votes[candidate_name] + 1
        
    

#calculating election result   
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

winning_votes = 0
winner = ""

for candidate, votes in candidate_votes.items():
    # Calculating percentage of votes each candidate got
    percentage_votes = (votes / total_votes) * 100
    # Add the candidate's results to the output
    output += f"{candidate}: {percentage_votes:.3f}% ({votes})\n"
    
    
    #finding the winning candidate
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate
    
output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------"
)

print(output)

#write output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
       
    


