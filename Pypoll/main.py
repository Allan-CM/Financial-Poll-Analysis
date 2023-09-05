#Allows file path to be opened in differing OS
import os 

#Module that allow CSV to be read 
import csv

#Setting path to csv file 
csvpath = os.path.join('Resources', 'election_data.csv')

#Initializing Dictonry with Lists
data = {
        "BalltonID": [],
        "County": [],
        "Candidate": []
        }

#Initiailzing Empty dictonary
results ={}

vote = 0
max_votes = 0

#Telling program to read csv
with open(csvpath) as csvfile:

    # CSV reader read files with comma dictating seperate columns 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Reads the header rown first 
    csv_header = next(csvreader)

    for row in csvreader:
        data["BalltonID"].append(row[0])
        data["County"].append(row[1])
        data["Candidate"].append(row[2])

total = 0 
total = [total + 1 for i in range(len(data['BalltonID']))]

for candidate in data["Candidate"]:
    if candidate in results:
        results[candidate]["Votes"] += 1
    elif candidate not in results: 
        results[candidate] = {"Percentage": 0, "Votes": 1}
     
#Counting Number of Ballots/Votes 
total = 0 
total = [total + 1 for i in range(len(data['BalltonID']))]

for key in results:
    results[key]["Percentage"] = round((results[key]["Votes"] / sum(total) * 100), 3)

for key, value in results.items():
    if max_votes > results[key]["Votes"]: 
        max_votes = max_votes
    elif max_votes < results[key]["Votes"]: 
        max_votes = results[key]["Votes"]

for key, value in results.items():
    if results[key]["Votes"] == max_votes:  
        winner = key
    
#Print Election Result 
print("Election Result")

print("-------------------")

#Prints total number of votes cast 
print(f"Total Votes: {sum(total)}")

print("-------------------")

for key,value in results.items():
    print(f"{key}: {results[key]['Percentage']}% ({results[key]['Votes']})")

print("-------------------")

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

for key, value in results.items():
    # Write the formatted output to the file
    output += (f"{key}: {results[key]['Percentage']}% ({results[key]['Votes']})\n")

output += (
    f"-------------------\n"
    f"Winner: {winner}"      
    )

#Export text file 
with open(file_output_path, "w") as txt_file:
    txt_file.write(output)