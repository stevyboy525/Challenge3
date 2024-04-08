#PyBank Instructions
#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#Your analysis should align with the following results:"
#def sumofpl(csvreader): 

import os
import csv
import string 
from collections import Counter
#import pandas as pd 

def sumofpl(): 
    last_value = 0 
    csvpath = '/Users/stephenmarkovic/desktop/archive/githubdir/challenge3/challenge3/budget_data.csv'
    maxnum = 0 
    countpl = 0 
    sumpl = 0 
    average = 0 
    lst = []
    lst2 = []   
    with open(csvpath) as csvfile: 
            csvreader = csv.reader(csvfile)
            csvwriter = csv.writer(csvfile)
            #print(csvreader)
            csv_header = next(csvreader)
            row2list = []
            location = []
            greatest_number = 0
            lowest_number = 0 
            for row in csvreader:             
                lst = str(row[0])
                cell_count = csvreader.line_num               
                pls = int(row[1])
                pli = lst
                countpl += 1                 
                sumpl = sumpl + pls 
                average = sumpl / countpl                    
                if pls > greatest_number: 
                    greatest_number = pls
                if pls < lowest_number: 
                    lowest_number = pls
                
            print(lst)
            print('Field names are: ' + ', '.join(field for field in csv_header))
            print(f"This is the sum of column 2 {sumpl}")
            print(f"Total count of values in column 1: {countpl}")
            print(f"Average of values in column 2: {average}")    
            print(f"Largest number in data set {greatest_number}")
            print(f"Largest number in data set {lowest_number}")

#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

            
def polsum(): 
    csvpath = '/Users/stephenmarkovic/desktop/archive/githubdir/challenge3/challenge3/election_data.csv'
    lst = []
    lst_can = []
    lst_num = 0 
    i = str
    countpl = 0 
    mydict = {}
    mylist = []
    seen = set()
    winner = ""
    winner_votes = 0
    total_votes = 0 
    candidate_votes = {}
    with open(csvpath) as csvfile: 
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(csvfile)
        
        header = next(csvreader)
        
                        
        for row in csvreader:             
            total_votes += 1 
            candidate_name = row[2]
            #print(candidate_name)
            if candidate_name in candidate_votes: 
               candidate_votes[candidate_name] +=1 
               
            else:
                candidate_votes[candidate_name] =1
            #count = count +1
            #if row == "Raymon Anthony Doane":
        for key, value in candidate_votes.items():
            #print(key)
            #print(value)
            if value > winner_votes:
                winner_votes = value
                winner = key 
                              
        print(f"Total number of votes {total_votes}")
        print(candidate_votes)
        print(mylist)
        print(winner)
        print(winner_votes)
        
        with open("output.txt", "w") as txtfile:
             #txtfile.write(str(candidate_votes))
            for key, value in candidate_votes.items():
                txtfile.write(f"{key} {value/total_votes} {value}")
                
                
                
   
sumofpl()
polsum()    
