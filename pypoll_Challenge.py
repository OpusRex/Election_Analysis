


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

#create list of counties
county_options = []

#create empty dictionary to hold each candidate
candidate_votes = {}

#create county totals
county_votes = {}

#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#create variables for county calculations
top_county = ""
top_countycount = 0
top_countypercentage = 0

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

        #print the county name from each row
        county_name = row[1]

        #if candidate does not match andy exissting candidate...
        if candidate_name not in candidate_options:

                #add it to the list of candidates
                candidate_options.append(candidate_name)

                #begin tracking candidate's vote count
                candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #check for this county existing in county list
        if county_name not in county_options:
            
                #Add county if not already in listing
                county_options.append(county_name)

                #begin county count
                county_votes[county_name] = 0
        #add a vote to the county total
        county_votes[county_name] += 1

    #set reference to text file we are creating
    with open(file_to_save,"w") as txt_file:

        #create total votes listing
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")

        #print total count to terminal
        print(election_results, end="")

        #write total count to file
        txt_file.write(election_results)

        #print county header to terminal
        print("County Votes: \n")

        #print county header to file
        txt_file.write("County Votes: \n")

        #Get the votes for each county
        for county in county_votes:

            #return the vote count
            cvotes = county_votes[county]

            #Calculate a percentage of total votes
            county_percentage = (int(cvotes)/int(total_votes)) * 100


            #Determine county with largest turnout
            if (cvotes > top_countycount) and county_percentage > top_countypercentage:

                #track the county with the highest turnout
                top_county = county
                #track the votes for county with highest tourout
                top_countycount = county_votes[county]
                #track percentge of total votes for highest county
                top_countypercentage =  county_percentage


            #format and print the results out for each county
            county_result = (f"{county}: {county_percentage:.1f}% ({cvotes:,})\n")
            #write to terminal
            print(county_result)
            #write to text file
            txt_file.write(county_result)


        #format top county labels
        county_LCT = (
            f"-------------------------\n"
            f"Largest County Turnout: {top_county}\n"
            f"-------------------------\n"
            )
        #print top county to terminal            
        print(county_LCT)
        #print top county to text file
        txt_file.write(county_LCT)

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
            candidate_result = (f"{candidate}: {vote_percentage:.1f}% {votes:,}\n")
            print(f"{candidate}: {vote_percentage:.1f}")
            txt_file.write(candidate_result)
            

        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------"
            )
        print(winning_candidate_summary)
        #Save the winning candidate's results to text file
        txt_file.write(winning_candidate_summary)









            


















