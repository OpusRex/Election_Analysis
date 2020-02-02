#testing
"""counties = ["Arapahoe","Denver","Jefferson"]
print(counties)

temperature = int(input("What is the temperature outside?"))

if temperature >80:
    print("Turn on the AC>")
else:
    print("Open the windows>")
"""

"""#What is the score?
score = int(input("What is your test score?"))

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >=80:
        print('Your grade is a B.')
    else:
"""

"""candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the elections? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of Votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

"""

counties_dict = {"Arapahoe":422829, "Denver": 463353, "Jefferson":432438}
#print(counties_dict)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

#print(voting_data)

#for  votes in voting_data:
#for county in counties_dict.keys():
        #print(county)

#for votes in counties_dict.values():
    #print(votes)

#for counties_dict in voting_data:
    #for county, value in counties_dict.items():
        #print(f"{county} county has {value} registered voters.")
        #print(county + str(value))
        #print(value)
        #print(counties_dict['county'])

#for county, value in counties_dict.items():
    #print(f"{county} county has {value} registered voters. ")


#for counties_dict in voting_data:
    #for county, value in counties_dict.items():
            #print(county,value)

           


# The data we need to retrieve
#1.Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#inmport dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Open the election results and read the file.
with open(file_to_load) as election_data:

    # read and analyze some data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    ##Print the hearder row
    headers = next(file_reader)
    print(headers)

    #Print each row in csv file.
    #for row in file_reader:
     #   print(row)




"""
#Open the election results and read the file.
#with open(file_to_load) as election_data:
#election_data = open(file_to_load,"r")

#To do: perform analysis
    #print(election_data)
#Close the file not needed when using WITH statement to open the file
#except the following code bitches when there isn't an indented line
 #   election_data.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
 """







            


















