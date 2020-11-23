# NAME : BRYAN HOOI YU ERN
# STUDENT ID : 30221005
# TASK 1 : RACE TO PI


# (a)
from math import pi
from math import sqrt


def basel(precision):                                           #function header. Takes in 1 argument "precision"
    approximation = 0                                           #sets the value assigned to the variable approximation to 0
    num_terms = 0                                               #sets the value assigned to the variable num_terms to 0          
    numerator = 1                                               #sets the value assigned to the variable numerator to 1
    denominator = 1                                             #sets the value assigned to the variable denominator to 1
    term = (numerator/denominator)                              #sets the value assigned to the variable term to the result of (numerator/denominator)
    while abs(pi - approximation) > precision:                  #code below repeatedly executes as long as value of difference is greater than precision
        approximation = sqrt(6*term)                            #sets the value assigned to the variable approximation to be the result of sqrt(6*term)
        denominator += 1                                        #increment denominator by 1
        term += (numerator/(denominator**2))                    #increment term by (numerator/(denominator**2))
        num_terms += 1                                          #increment num_terms by 1
    return (approximation, num_terms)                           #returns the values of approximation and num_terms as a tuple
print(basel(0.1))



def taylor(precision):                                          #function header. Takes in 1 argument "precision"
    approximation = 0                                           #sets the value assigned to the variable approximation to 0
    num_terms = 0                                               #sets the value assigned to the variable num_terms to 0
    numerator = 1                                               #sets the value assigned to the variable numerator to 1
    denominator = 1                                             #sets the value assigned to the variable denominator to 1
    term = (numerator/denominator)                              #sets the value assigned to the variable term to the result of (numerator/denominator)
    next_state = "Subtraction"                                  #sets the value assigned to the variable next_state to a string "Subtraction"
    while abs(pi - approximation) > precision:                  #code below repeatedly executes as long as value of difference is greater than precision
        approximation = (4*term)                                #sets the value assigned to the variable approximation to be the result of 4*term
        denominator += 2                                        #increment denominator by 2
        if next_state == "Subtraction":                         #execute indented block if value of next_state is "Subtraction", else jump to else block
            term += (-(numerator/denominator))                  #increment term by -(numerator/denominator)
            num_terms += 1                                      #increment num_terms by 1
            next_state = "Addition"                             #change value of next_state to "Addition"  
        else:                                                   #else block executes if condition at if block is not True
            term += (numerator/denominator)                     #increment term by (numerator/denominator)
            num_terms += 1                                      #increment num_terms by 1
            next_state = "Subtraction"                          #change value of next_state to "Subtraction"            
    return (approximation, num_terms)                           #returns the values of approximation and num_terms as a tuple
print(taylor(0.2))



def wallis(precision):                                          #function header. Takes in 1 argument "precision"
    approximation = 0                                           #sets the value assigned to the variable approximation to 0
    num_terms = 0                                               #sets the value assigned to the variable num_terms to 0
    numerator = 2                                               #sets the value assigned to the variable numerator to 2
    denom_left = 1                                              #sets the value assigned to the variable denom_left to 1
    denom_right = 3                                             #sets the value assigned to the variable denom_right to 3
    denominator = (denom_left*denom_right)                      #sets the value assigned to the variable denominator to the result of (denom_left*denom_right)
    term = ((numerator*numerator)/(denominator))                #sets the value assigned to the variable term to the result of ((numerator*numerator)/(denominator))
    while abs(pi - approximation) > precision:                  #code below repeatedly executes as long as value of difference is greater than value of precision
        approximation = (2*term)                                #sets the value assigned to the variable approximation to be the result of 2*term
        numerator += 2                                          #increments value of numerator by 2
        denom_left = denom_right                                #sets value of denom_left to the current value of denom_right
        denom_right += 2                                        #increments value of denom_right by 2
        denominator = (denom_left*denom_right)                  #updates the value of denominator with the new values of denom_left and denom_right
        term *= ((numerator*numerator)/(denominator))           #increments the value of term by multiplication of ((numerator*numerator)/(denominator))
        num_terms += 1                                          #increments value of num_terms by 1
    return (approximation, num_terms)                           #returns values of approximation and num_terms as a tuple
print(wallis(0.2))



def spigot(precision):                                          #function header. Takes in 1 argument "precision"
    approximation = 0                                           #sets the value assigned to the variable approximation to 0
    num_terms = 0                                               #sets the value assigned to the variable num_terms to 0
    initial_value = 0.0                                         #sets the value assigned to the variable initial_value to 0
    current_value = 1.0                                         #sets the value assigned to the variable current_value to 1
    numerator = current_value                                   #sets the value assigned to the variable numerator to value of current_value
    denominator = 1.0                                           #sets the value assigned to the variable denominator to 1
    overall_term = (numerator/denominator)                      #sets the value assigned to the variable overall_term to the result of (numerator/denominator)
    current_term = (numerator/denominator)                      #sets the value assigned to the variable current_term to the result of (numerator/denominator)
    while abs(pi - approximation) > precision:                  #code below executes as long as value of difference is greater than value of precision
        approximation = (2*overall_term)                        #sets the value assigned to the variable approximation to be the result of 2*overall_term
        temp_value = initial_value                              #sets the value assigned to the variable temp_value to the value of initial_value
        initial_value = current_value                           #resets the value of initial_value to the value of current_value
        current_value += temp_value                             #increments current_value by temp_value
        numerator = current_value                               #updates the value of numerator with the new value of current_value
        denominator += 2                                        #increments value of denominator by 2
        next_term = current_term*(numerator/denominator)        #sets the value assigned to the variable next_term to the result of (current_term*(numerator/denominator))
        overall_term += next_term                               #increments the value of overall term by next_term
        current_term = next_term                                #updates the value of current_term with the value of next_term
        num_terms += 1                                          #increments the value of num_terms by 1
    return (approximation, num_terms)                           #returns values of approximation and num_terms as a tuple
print(spigot(0.1))



# (b)
def tuple_second_element(tuple):                                                                #function header. Takes in one argument "tuple"
    return tuple[1]                                                                             #returns the second element in "tuple"

def race(precision, algorithms):                                                                #function header. Takes in 2 arguments "precision" and "algorithms"
    output_list = []                                                                            #generates an empty list called output_list
    for item in range(len(algorithms)):                                                         #iterates from 0 to len(algorithms)-1
        result = algorithms[item](precision)                                                    #assigns the result of calling the function at index item with argument precision in algorithms
        output_list.append((item+1, result[1]))                                                 #inserts a tuple containing item+1 and the second element of result into output_list
    return sorted(output_list, key = tuple_second_element)                                      #sorts the updated output_list based on each tuple's second element. The key used is the first function above which returns the second element of a tuple
print(race(0.01, [taylor, wallis, basel])) 



# (c)
def print_results(race_list):                                                                   #function header. Takes in 1 argument "race_list"
    for item in race_list:                                                                      #iterating through each item in race_list (which would be tuples)
        print("Algorithm " + str(item[0]) + " finished in " + str(item[1]) + " steps")          #prints a human-readable statement containing the first and second elements of item
race_list1 = race(0.01, [taylor, wallis, basel])
print_results(race_list1)                                                                       #calling the print_results function and passing in race_list1 as the argument


# Comment for SPIGOT
# Due to my numerator sequence being the Fibonacci series, the sequence becomes divergent after a certain number of terms
# So any value of precision below 0.016 will result in a infinite loop as the loop condition doesnt become false.
# During code testing, precision values for spigot should be equal to or greater than 0.016 to produce the correct output
