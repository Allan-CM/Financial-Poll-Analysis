#Allows file path to be opened in differing OS
import os 

#Module that allow CSV to be read 
import csv

#Setting path to csv file 
csvpath = os.path.join('Resources', 'budget_data.csv')

#Initializing total months variable 
total_months = 0

#Initializing Profit List
profits = []

#Initializing Net Profit Variable
net_profit = 0

#Intializing monthly change variables
monthly_change = 0

#Initalizing monthly profit change list
monthy_change_list = []

#Initalizing a date/month list
date = []

#Telling program to read csv
with open(csvpath) as csvfile:

    # CSV reader read files with comma dictating seperate columns 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Reads the header rown first 
    csv_header = next(csvreader)

    #Print Financial Analyiss 
    print("Financial Analysis")

    print("-------------------")

    #For loop goes through every row in the csv
    for row in csvreader:
        #count the number of rows in the row to determine total number opf months since we have clean non-repetitive data
        total_months+=1
        #Takes all the profit values in the csv file and adds it to the profits list initalized earlier  
        profits.append(row[1])
        #Appends all the dates to date list iniitalized earlier 
        date.append(row[0])

    #Loops through the profits list based on the length of the list 
    for i in range(len(profits)): 
        #adds the values in list by looping through each index to determine net profit 
        net_profit += int(profits[i])
        #If statement make sure program only runs if within the lnegth of the profits list to prevent program error
        if int(i+1) < len(profits):
            #calcuale the change in profit month to month 
            change = (int(profits[i+1])) - (int(profits[i]))
            #Appending list of changes to a list called monthly changes 
            monthy_change_list.append(change)
            #Sum up the change in profit month to month 
            monthly_change += change
    #Calculating the average change and using round function to round answer to 2 decimal places 
    average_change = round((monthly_change)/(total_months-1), 2)

    #determining the greatest increase in profits from the monthly change list
    Greatest_increase = max(monthy_change_list)
    print(Greatest_increase)
    #determining the greatest decrease in profits from the monthly change list
    Greatest_decrease = min(monthy_change_list)
    print(Greatest_decrease)


        

    #Prints the total number of months included in the dataset
    print(f"Total months: {total_months}")
    #Prints the net total amount of "Profit/Losses" over the entire period
    print(f"Total: {net_profit}")
    #Prints the Average profit/loss change 
    print(f"Average Change: {average_change}")

    
    
    

    

    

    



        

    
