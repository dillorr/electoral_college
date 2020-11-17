import pandas as pd
import numpy as np


# STATE ABBREVIATIONS
ec_votes_per_state = {
    'Alabama':'AL',
    'Alaska':'AK',
    'Arizona': 'AZ',
    'Arkansas':'AR',
    'California':'CA',
    'Colorado':'CO',
    'Connecticut':'CT',
    'Delaware':'DE',
    'District of Columbia': '-',
    'Florida':'FL',
    'Georgia':'GA',
    'Hawaii':'HI',
    'Idaho':'ID',
    'Illinois':'IL',
    'Indiana':'IN',
    'Iowa':'IA',
    'Kansas':'KS',
    'Kentucky':'KY',
    'Louisiana':'LA',
    'Maine': 'ME',
    'Maine - 1st Congressional District': 'ME',
    'Maine - 2nd Congressional District': 'ME',
    'Maryland':'MD',
    'Massachusetts':'MA',
    'Michigan':'MI',
    'Minnesota':'MN',
    'Mississippi':'MS',
    'Missouri':'MO',
    'Montana':'MT',
    'Nebraska':'NE',
    'Nebraska - 1st Congressional District': 'NE',
    'Nebraska - 2nd Congressional District': 'NE',
    'Nebraska - 3rd Congressional District': 'NE',
    'Nevada':'NV',
    'New Hampshire':'NH',
    'New Jersey':'NJ',
    'New Mexico':'NM',
    'New York':'NY',
    'North Carolina':'NC',
    'North Dakota':'ND',
    'Ohio':'OH',
    'Oklahoma':'OK',
    'Oregon':'OR',
    'Pennsylvania':'PA',
    'Rhode Island':'RI',
    'South Carolina':'SC',
    'South Dakota':'SD',
    'Tennessee':'TN',
    'Texas':'TX',
    'Utah':'UT',
    'Vermont':'VT',
    'Virginia':'VA',
    'Washington':'WA',
    'West Virginia':'WV',
    'Wisconsin':'WI',
    'Wyoming':'WY'
}

# create df with dictionary values 
ec_votes_per_state_df = pd.DataFrame(list(ec_votes_per_state.items()), columns = ['State', 'Abbreviation'])

# ELECTORAL COLLEGE VOTES PER STATE 2020 
ec_votes_per_state = {
    'Alabama':9,
    'Alaska':3,
    'Arizona': 11,
    'Arkansas':6,
    'California':55,
    'Colorado':9,
    'Connecticut':7,
    'Delaware':3,
    'District of Columbia':3,
    'Florida':29,
    'Georgia':16,
    'Hawaii':4,
    'Idaho':4,
    'Illinois':20,
    'Indiana':11,
    'Iowa':6,
    'Kansas':6,
    'Kentucky':8,
    'Louisiana':8,
    'Maine': 2,
    'Maine - 1st Congressional District': 1,
    'Maine - 2nd Congressional District': 1,
    'Maryland':10,
    'Massachusetts':11,
    'Michigan':16,
    'Minnesota':10,
    'Mississippi':6,
    'Missouri':10,
    'Montana':3,
    'Nebraska':2,
    'Nebraska - 1st Congressional District': 1,
    'Nebraska - 2nd Congressional District': 1,
    'Nebraska - 3rd Congressional District': 1,
    'Nevada':6,
    'New Hampshire':4,
    'New Jersey':14,
    'New Mexico':5,
    'New York':29,
    'North Carolina':15,
    'North Dakota':3,
    'Ohio':18,
    'Oklahoma':7,
    'Oregon':7,
    'Pennsylvania':20,
    'Rhode Island':4,
    'South Carolina':9,
    'South Dakota':3,
    'Tennessee':11,
    'Texas':38,
    'Utah':6,
    'Vermont':3,
    'Virginia':13,
    'Washington':12,
    'West Virginia':5,
    'Wisconsin':10,
    'Wyoming':3
}

# create df with dictionary values 
ec_votes_per_state_df['EC Votes'] = list(ec_votes_per_state.values())

# 2020 STATE WINNERS 
state_winner = {
    'Alabama':'Trump',
    'Alaska':'Trump',
    'Arizona':'Biden',
    'Arkansas':'Trump',
    'California':'Biden',
    'Colorado':'Biden',
    'Connecticut':'Biden',
    'Delaware':'Biden',
    'District of Columbia':'Biden',
    'Florida':'Trump',
    'Georgia':'-',
    'Hawaii':'Biden',
    'Idaho':'Trump',
    'Illinois':'Biden',
    'Indiana':'Trump',
    'Iowa':'Trump',
    'Kansas':'Trump',
    'Kentucky':'Trump',
    'Louisiana':'Trump',
    'Maine': 'Biden',
    'Maine - 1st Congressional District': 'Biden',
    'Maine - 2nd Congressional District': 'Trump',
    'Maryland':'Biden',
    'Massachusetts':'Biden',
    'Michigan':'Biden',
    'Minnesota':'Biden',
    'Mississippi':'Trump',
    'Missouri':'Trump',
    'Montana':'Trump',
    'Nebraska':'Trump',
    'Nebraska - 1st Congressional District': 'Trump',
    'Nebraska - 2nd Congressional District': 'Biden',
    'Nebraska - 3rd Congressional District': 'Trump',
    'Nevada':'Biden',
    'New Hampshire':'Biden',
    'New Jersey':'Biden',
    'New Mexico':'Biden',
    'New York':'Biden',
    'North Carolina':'Trump',
    'North Dakota':'Trump',
    'Ohio':'Trump',
    'Oklahoma':'Trump',
    'Oregon':'Biden',
    'Pennsylvania':'Biden',
    'Rhode Island':'Biden',
    'South Carolina':'Trump',
    'South Dakota':'Trump',
    'Tennessee':'Trump',
    'Texas':'Trump',
    'Utah':'Trump',
    'Vermont':'Biden',
    'Virginia':'Biden',
    'Washington':'Biden',
    'West Virginia':'Trump',
    'Wisconsin':'Biden',
    'Wyoming':'Trump'
}

# add list of winners to df
ec_votes_per_state_df['Winner'] = list(state_winner.values())

# VOTE TALLY
total_tally = ec_votes_per_state_df['EC Votes'].sum()
biden_tally = ec_votes_per_state_df['EC Votes'].loc[ec_votes_per_state_df['Winner'] == 'Biden'].sum()
trump_tally = ec_votes_per_state_df['EC Votes'].loc[ec_votes_per_state_df['Winner'] == 'Trump'].sum()
remaining_tally = ec_votes_per_state_df['EC Votes'].loc[ec_votes_per_state_df['Winner'] == '-'].sum()

# PARTY AFFILIATION
ec_votes_per_state_df.loc[ec_votes_per_state_df['Winner'] == 'Biden', 'Party'] = 'D'
ec_votes_per_state_df.loc[ec_votes_per_state_df['Winner'] == 'Trump', 'Party'] = 'R'
ec_votes_per_state_df.loc[ec_votes_per_state_df['Winner'] == '-', 'Party'] = '-'

print('\n')
print('2020 Election Results by State')
print('------------------------------')
print(ec_votes_per_state_df)
print('\n')
print('Results')
print('-------')
print('Total Electoral College Votes:         ' ,total_tally)
print('Electoral College Votes for Biden (D): ', biden_tally)
print('Electoral College Votes for Trump (R): ', trump_tally)




print('\n')
print('States Remaining:')
print('-----------------')
remaining_states = ec_votes_per_state_df[['State','EC Votes']].loc[ec_votes_per_state_df['Winner'] == '-']
print(remaining_states.to_string(index=False))
print('\n')

print('Total Remaining Electoral College Votes: ', remaining_tally)
print('\n') 