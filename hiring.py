# NAME : BRYAN HOOI YU ERN
# STUDENT ID : 30221005
# TASK 1 : TALENT ACQUISITION

# (a)

jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)

candidates1 = [jess, clark, john, cindy]
project1 = ["php", "java", "c++", "lua", "go"]

tracy = (["matlab","statistics","python","tensorflow"],900)
sandy = (["marketing","sales"],450)
superman = (["python","mysql","marketing","web design","robotics"],2000)
daisy = (["mysql","marketing"],700)
matt = (["python","php","web design"],300)

candidates2 = [tracy,sandy,superman,daisy,matt]
project2 = ["python","web design","mysql","marketing"]

def cost(candidates):
    combined_daily_rates = 0                                        # assign the value 0 to the variable combined_daily_rates
    for candidate in candidates:                                    # iterate through each candidate in given list of candidates
        combined_daily_rates += candidate[1]                        # add second element of candidate to combined_daily_rates
    return combined_daily_rates                                     # return combined_daily_rates

#print(cost([john,cindy]))          # expected output : 740
#print(cost(candidates1))           # expected output : 1940
#print(cost([clark]))               # expected output : 1000
#print(cost([clark,john]))          # expected output : 1500

#print(cost([matt,tracy]))          # expected output : 1200
#print(cost(candidates2))           # expected output : 4350
#print(cost([sandy]))               # expected output : 450
#print(cost([superman,daisy]))      # expected output : 2700


def skills(candidates):
    skills_possessed = []                                       # initialise skills_possessed with an empty list
    for candidate in candidates:                                # iterate through each candidate in given list of candidates
        for skills in candidate[0]:                             # iterate through all the skills in candidate's list of skills
            if skills not in skills_possessed:                  # if the current skill is not in the skills_possessed list,
                skills_possessed += [skills]                    # append it to skills_possessed
    return skills_possessed                                     # return skills_possessed

#print(skills([clark,cindy]))       # expected output : php,c++,go,word
#print(skills(candidates1))         # expected output : php,java,c++,go,lua,word
#print(skills([john,cindy]))        # expected output : lua,php,go,word
#print(skills([jess,clark]))        # expected output : php,java,c++,go

#print(skills([tracy,sandy]))       # expected output : matlab,statistics,python,tensorflow,marketing,sales
#print(skills(candidates2))         # expected output : matlab,statistics,python,tensorflow,marketing,sales,mysql,web design,robotics,php
#print(skills([daisy,matt]))        # expected output : mysql,marketing,python,php,web design
#print(skills([superman,daisy]))    # expected output : python,mysql,marketing,web design,robotics


def uncovered(project, skills):         
    uncovered_skills = []                           # assign an empty list to the variable uncovered_skills
    for skills_required in project:                 # iterating through each element in project
        if skills_required not in skills:           # if the current element is not in skills
            uncovered_skills += [skills_required]   # append current element to uncovered_skills
    return uncovered_skills                         # return uncovered_skills

#print(uncovered(project1, skills([clark])))        # expected output : java,lua
#print(uncovered(project1, skills(candidates1)))    # expected output : []
#print(uncovered(project1, skills([jess,clark])))   # expected output : lua
#print(uncovered(project1, skills([cindy])))        # expected output : java,c++,lua

#print(uncovered(project2, skills([tracy])))        # expected output : web design, mysql, marketing
#print(uncovered(project2, skills(candidates2)))    # expected output : []
#print(uncovered(project2, skills([daisy,tracy])))  # expected output : web design
#print(uncovered(project2, skills([sandy])))        # expected output : python,web design,mysql


# (b)

def best_individual_candidate(project, candidates):
    best_candidate_index = 0                                                                                # set value of best_candidate_index to 0
    num_skills_covered = len(project) - len(uncovered(project, skills([candidates[best_candidate_index]]))) # calculate num_skills_covered by candidate at best_candidate_index of candidates
    highest_skills_covered_per_dollar = num_skills_covered/cost([candidates[best_candidate_index]])         # calculate highest_skills_covered_per_dollar by dividing num_skills_covered by the cost of that candidate

    for i in range(len(candidates)):                                                                        # iterating through every candidate in candidates
        num_skills_covered = len(project) - len(uncovered(project, skills([candidates[i]])))                # calculating num_skills_covered
        skills_covered_per_dollar = num_skills_covered/cost([candidates[i]])                                # calculating skills_covered_per_dolar
        if skills_covered_per_dollar > highest_skills_covered_per_dollar:                                   # checks if skills_covered_per_dollar is greater than highest_skills_covered_per_dollar
            highest_skills_covered_per_dollar = skills_covered_per_dollar                                   # if so, set value of highest_skills_covered_per_dollar to value of skills_covered_per_dollar
            best_candidate_index = i                                                                        # and set value of best_candidate_index to i

    return best_candidate_index                                                                             # return best_candidate_index

#print(best_individual_candidate(project1, candidates1))            # expected output : 0 
#print(best_individual_candidate(project1, [cindy,jess]))           # expected output : 1
#print(best_individual_candidate(project1, [john,clark]))           # expected output : 1
#print(best_individual_candidate(project1, [jess]))                 # expected output : 0

#print(best_individual_candidate(project2, candidates2))            # expected output : 4 
#print(best_individual_candidate(project2, [daisy,superman]))       # expected output : 0
#print(best_individual_candidate(project2, [tracy,sandy]))          # expected output : 1
#print(best_individual_candidate(project2, [matt]))                 # expected output : 0


# Additional functions

def teams_generator(team_size):                         # function to generate all possible bitlists of length team_size in lexicographic order
    first = [0]*team_size                               # function obtained from Lecture 11(Brute Force) slides from Week 6 on Moodle
    last = [1]*team_size                                # slide 26
    all_teams = [first]

    while all_teams[-1] != last:
        next_team = next_team_generator(all_teams[-1])
        all_teams += [next_team]

    return all_teams

def next_team_generator(given_team):
    next_team = given_team[:]                       # generate a copy of given_team and assign it to next_team

    for i in range(len(next_team)-1, -1, -1):       # iterating from the last element to the first
        if next_team[i] < 1:                        # checks if current element is lesser than 1
            next_team[i] += 1                       # if so, increment the current element by 1
            for j in range(i+1, len(next_team)):    # then iterate to the end of next_team starting from the element to the right of current element
                next_team[j] = 0                    # and set the values of those elements to 0
            return next_team                        # return next_team

    return next_team                                # return next_team

def valid_teams(project, given_teams, candidates): 
    valid_teams = []                                            # initialise the variable valid_teams with an empty list

    for team in given_teams:                                    # iterating through every element in given_teams
        actual_team = []                                        # create a new variable actual_team and assign an empty list to it
        for i in range(len(team)):                              # iterating through every element in team itself
            if team[i] == 1:                                    # checks if current element is 1
                actual_team.append(candidates[i])               # if so, append the element at index i in candidates to actual_team
        if len(uncovered(project, skills(actual_team))) == 0:   # checks if number of uncovered skills for that actual team is 0
            valid_teams.append(actual_team)                     # if so, append the actual team to valid_teams

    return valid_teams                                          # return valid_teams


# (c)

def team_of_best_individuals(project, candidates):
    team = []                                                                                   # create an empty list assign to variable team
    remaining_candidates = candidates[:]                                                        # generate a copy of candidates and assign it to remaining_candidates
    
    while len(uncovered(project,skills(team))) > 0:                                             # loop executes as long as there are skills from the project still uncovered
        skills_still_needed = uncovered(project, skills(team))                                  # obtain the skills still required by the project
        best_candidate = best_individual_candidate(skills_still_needed, remaining_candidates)   # choose the best candidate out of the remaining candidates list for the required skills
        chosen_candidate = remaining_candidates[best_candidate]                                 # set the chosen candidate
        team.append(chosen_candidate)                                                           # append the chosen candidate to the team
        remaining_candidates.pop(best_candidate)                                                # remove that candidate from remaining_candidates

    return team                                                                                 # return team

#print(team_of_best_individuals(project1, candidates1))                                     # expected output : [jess,cindy,john,clark]
#print(team_of_best_individuals(["php","java","c++", "lua"], candidates1))                  # expected output : [jess,john,clark]
#print(team_of_best_individuals(["php","java","c++"], candidates1))                         # expected output : [jess,clark]
#print(team_of_best_individuals(["php","java", "c++", "go"], candidates1))                  # expected output : [jess,cindy,clark]

#print(team_of_best_individuals(project2, candidates2))                                     # expected output : [matt,daisy]
#print(team_of_best_individuals(["php","python","marketing"], candidates2))                 # expected output : [matt,daisy]
#print(team_of_best_individuals(["php","python","marketing","robotics"], candidates2))      # expected output : [matt,daisy,superman]
#print(team_of_best_individuals(["python","sales","marketing"], candidates2))               # expected output : [sandy,matt]
        

def best_team(project, candidates):

    all_possible_teams = teams_generator(len(candidates))                   # generate all_possible_teams as bitlists using teams_generator

    all_valid_teams = valid_teams(project, all_possible_teams, candidates)  # filter out all_valid_teams from all_possible_teams as appropriate lists of tuples

    best_team = all_valid_teams[0]                                          # set the first element of all_valid_teams as the best_team

    for valid_team in all_valid_teams:                                      # iterating through every element in all_valid_teams
        if cost(valid_team) <= cost(best_team):                             # checks if cost of valid_team is lesser than or equal to cost of best_team
            best_team = valid_team                                          # if so, set valid_team as the best_team

    return best_team                                                        # return best_team

#print(best_team(project1,candidates1))    # expected output : [jess,clark,john]
#print(best_team(project2,candidates2))    # expected output : [daisy,matt]










