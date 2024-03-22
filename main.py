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
    csvpath = '/Users/stephenmarkovic/Desktop/githubdir/Challenge3/Challenge3/budget_data.csv'
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
    csvpath = '/Users/stephenmarkovic/Desktop/githubdir/Challenge3/Challenge3/election_data.csv'
    lst = []
    lst_can = []
    lst_num = 0 
    i = str
    countpl = 0 
    mydict = {}
    mylist = []
    seen = set()
    count = 0 
    with open(csvpath) as csvfile: 
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(csvfile)
        
                
        for row in csvreader:             
            countpl += 1
            lst = str(row)
            mydict = str(row)
            lst_can = (row)
            
            if row == "Raymon Anthony Doane":
                count = count +1
        print(f"Total number of votes {countpl}")
        print(lst_can)
        print(mylist)
       
                
                
                
   
sumofpl()
polsum()    
