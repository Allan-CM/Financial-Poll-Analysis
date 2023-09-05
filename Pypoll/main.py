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
        results[candidate] = {"Percentage": 0, "Votes": (1)}
     
print(results)
#Counting Number of Ballots/Votes 
total = 0 
total = [total + 1 for i in range(len(data['BalltonID']))]

results["Charles Casper Stockham"]["Percentage"] = round((results["Charles Casper Stockham"]["Votes"] / sum(total) * 100), 3)
results["Diana DeGette"]["Percentage"] = round((results["Diana DeGette"]["Votes"] / sum(total) * 100), 3)
results["Raymon Anthony Doane"]["Percentage"] = round((results["Raymon Anthony Doane"]["Votes"] / sum(total) * 100), 3)


print(results)

#Print Election Result 
print("Election Result")

print("-------------------")

#Prints total number of votes cast 
print(f"Total months: {sum(total)}")

print("-------------------")

