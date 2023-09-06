#Allows file path to be opened in differing OS
import os 

#Module that allow CSV to be read 
import csv

#Setting path to csv file 
csvpath = os.path.join('Resources', 'election_data.csv')

#Initializing Dictonry with Lists
data = {
        "BallotID": [],
        "County": [],
        "Candidate": []
        }

#Initiailzing Empty dictonary
results ={}

#Initializing Variable to count number of votes
vote = 0
#Initializing variable to determin maximum number of votes 
max_votes = 0

#Telling program to read csv
with open(csvpath) as csvfile:

    # CSV reader read files with comma dictating seperate columns 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Reads the header rown first 
    csv_header = next(csvreader)

    #Loops through each row in csv file 
    for row in csvreader:
        #appends Ballot ID data to data dictonary under the BalltonID key
        data["BallotID"].append(row[0])
        #appends cadidate data to data dictonary under the candidate key
        data["Candidate"].append(row[2])

#Initalizing total vote variable 
total = 0 
#List comprehension to calculate the total number of votes 
total = [total + 1 for i in range(len(data['BallotID']))]

#Loops through each candidate from the data dictonary list
for candidate in data["Candidate"]:
    #If candidate is already part of our results dictonary list initalized earlier add plus 1 vote
    if candidate in results:
        results[candidate]["Votes"] += 1
    #If candidate is not part of our results dictonary list initalized earlier then...
    elif candidate not in results: 
        #....add candidate name to the list and initialize the percentage as 0 and vote count to 1
        results[candidate] = {"Percentage": 0, "Votes": 1}
     
#Counting Number of Ballots/Votes 
total = 0 
#Loops through the total number of BallotID entries to determine total number of words 
total = [total + 1 for i in range(len(data['BallotID']))]

#Loops through each key in the results dictonary list initalized earlier
for key in results:
    #calculate the percentage of votes for each candidate and updates the percentage key for that candidate
    results[key]["Percentage"] = round((results[key]["Votes"] / sum(total) * 100), 3)

#Loops through each key and value in the results dictonary list initalized earlier
for key, value in results.items():
    #if the max_votes is greater than the votes receieved by a canddiate max votes remains the same
    if max_votes > results[key]["Votes"]: 
        max_votes = max_votes
    #IF the max_votes is less than the votes receieved by a candidate then new max vote is now the current votes 
    elif max_votes < results[key]["Votes"]: 
        max_votes = results[key]["Votes"]

#Loops through each key and value in the results dictonary list initalized earlier
for key, value in results.items():
    #If candidate total vote matches the max votes then it retreive that candidate's name
    if results[key]["Votes"] == max_votes:  
        winner = key
    
#Print Election Result 
print("Election Result")

print("-------------------")

#Prints total number of votes cast 
print(f"Total Votes: {sum(total)}")

print("-------------------")

#Loops through each key and value in the results dictonary list initalized earlier
for key,value in results.items():
    #Goes through the loop to print candidate name, vote percentage, and total votes 
    print(f"{key}: {results[key]['Percentage']}% ({results[key]['Votes']})")

print("-------------------")

#Prints the winning candidates name 
print(f"Winner: {winner}")

#Setting output file path
file_output_path = os.path.join('Analysis', 'election_results.txt')

#Output Summary 
output = (
    f"Election Result\n"
    f"-------------------\n"
    f"Total Votes: {sum(total)}\n"
    f"-------------------\n"
    )

#Loops through each key and value in the results dictonary list initalized earlier
for key, value in results.items():
    #Goes through the loop to print candidate name, vote percentage, and total votes 
    output += (f"{key}: {results[key]['Percentage']}% ({results[key]['Votes']})\n")

#adds the winner name as a sepearte output in the same file 
output += (
    f"-------------------\n"
    f"Winner: {winner}"      
    )

#Export text file 
with open(file_output_path, "w") as txt_file:
    txt_file.write(output)