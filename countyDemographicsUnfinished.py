import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))
def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return first
def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    C =counties[0]["County"]
    S =counties[0]["State"]
    highest =counties[0]["Age"]["Percent Under 18 Years"]
    for a in counties:
        if a["Age"]["Percent Under 18 Years"] > highest:
            highest = a["Age"]["Percent Under 18 Years"]
            C = a["County"]
            S = a["State"]
    return C +"," + S
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highest =counties[0]["Age"]["Percent Under 18 Years"]
    for age in counties:
        if age["Age"]["Percent Under 18 Years"] > highest:
            highest = age["Age"]["Percent Under 18 Years"]
        return highest
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    C =counties[0]["County"]
    S =counties[0]["State"]
    highest =counties[0]["Age"]["Percent Under 18 Years"]
    for a in counties:
        if a["Age"]["Percent Under 18 Years"] > highest:
            highest = a["Age"]["Percent Under 18 Years"]
            C = a["County"]
            S = a["State"]
    return [C,S,highest]
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    dict=[]
    count = 0
    curState = counties[0]["State"]
    for i in counties:
   		if i['State'] == curState:
   			count= count + 1 
   			curState = i['State']
   		else:
   			count = count + 1
   			curState = i['State']
   			dict = count
   			count = 0
    return curState
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #Find the state in the dictionary with the most counties
    
    #Return the state with the most counties
    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    first = counties[0]["County"]
    fact = counties[0]["Income"]["Median Houseold Income"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
    return [fact,first]
if __name__ == '__main__':
    main()
