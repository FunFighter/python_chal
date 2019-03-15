import numpy as np
import pandas as pd

csv_voter_data = pd.read_csv("../Resources/election_data.csv")

def Analyze_Data(voter_data):
    #total number of votes
    total_votes = len(voter_data.index)
    
    #list of candidates unique
    unique_candidates = voter_data["Candidate"].unique()
    #this goes over the percent each because it needs to be defined first to use
    #votes per candidate
    vote_count = voter_data['Candidate'].value_counts()

    #percent each candidate
    pct_count = vote_count/total_votes * 100

    #popular vote winner
    popular_vote = vote_count[:1]
    
    print(f"Total Votes: {total_votes}")
    print(f"The Candidates: {unique_candidates}")
    print(f"Total Percent: {pct_count}")
    print(f"Vote Count: {vote_count}")
    print(f"Popular Vote: {popular_vote}")
    
    with open("Output.txt", "w") as text_file:
        print(f"Total Votes: {total_votes}", file=text_file)
        print(f"The Candidates: {unique_candidates}", file=text_file)
        print(f"Total Percent: {pct_count}", file=text_file)
        print(f"Vote Count: {vote_count}", file=text_file)
        print(f"Popular Vote: {popular_vote}", file=text_file)

Analyze_Data(csv_voter_data)