


#inmport dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#create variable/accumulator to count the votes
total_votes = 0

#create a base list for candidate options
candidate_options = []

#create empty dictionary to hold each candidate
candidate_votes = {}

#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # read and analyze some data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    ##Print the hearder row
    headers = next(file_reader)
    

    #Print each row in csv file.
    for row in file_reader:
        #print(row)
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]
        
        #Add the name from each row
        #candidate_options.append(candidate_name)

        #if candidate does not match andy exissting candidate...
        if candidate_name not in candidate_options:

                #add it to the list of candidates
                candidate_options.append(candidate_name)

                #begin tracking candidate's vote count
                candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #we need the votes, so using the key
    # get the value from each dictionary
    #and calculate their percentage
    for candidate in candidate_votes:

        #returns the value of the dictionary or number of votes
        votes = candidate_votes[candidate]

        #calculate a percentage of the total votes
        vote_percentage = (int(votes)/int(total_votes)) * 100


        #Print out each candidate's name, vote count and percentage

        #Determine winning vote count and candidate
        #Determine if votes is greate than current winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set current vote as winning vote and current vote percentage as winning percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #set winning canadate
            winning_candidate = candidate

        #format and print the results out
        print(f"{candidate}: received {vote_percentage:.1f}% of the vote.")

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------"
    )

print(winning_candidate_summary)
#print(candidate_votes)








            


















