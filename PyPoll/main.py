import os
import csv

election_csv = os.path.join('election_data.csv')

with open(election_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    candidate_one = "Khan"
    candidate_two = "Correy"
    candidate_three = "Li"
    candidate_four = "O'Tooley"
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    total_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == 'Khan':
            khan_count = khan_count + 1
        if row[2] == 'Correy':
            correy_count = correy_count + 1
        if row[2] == 'Li':
            li_count = li_count + 1
        if row[2] == "O'Tooley":
            otooley_count = otooley_count + 1
        khan_percentage = khan_count/total_votes*100
        correy_percentage = correy_count/total_votes*100
        li_percentage = li_count/total_votes*100
        otooley_percentage = otooley_count/total_votes*100
       

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print(str(candidate_one) + ": " + str(khan_percentage) + "%" + " (" + str(khan_count) + ")")
    print(str(candidate_two) + ": " + str(correy_percentage) + "%" + " (" + str(correy_count) + ")")
    print(str(candidate_three) + ": " + str(li_percentage) + "%" + " (" + str(li_count) + ")")
    print(str(candidate_four) + ": " + str(otooley_percentage) + "%" + " (" + str(otooley_count) + ")")
    print("-------------------------")

        if khan_percentage > 50:
            print("Winner: " + str(candidate_one))
        if correy_percentage > 50:
            print("Winner: " + str(candidate_two))
        if li_percentage > 50:
            print("Winner: " + str(candidate_three))
        if otooley_percentage > 50:
            print("Winner: " + str(candidate_four))

    
    