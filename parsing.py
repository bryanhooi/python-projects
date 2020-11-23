# NAME : BRYAN HOOI YU ERN
# STUDENT ID : 30221005
# TASK 2 : CALCULATOR

# (a)

from math import pow

symbols = ["+","-","*","/","^"]                         # list of all operators used
parentheses = ["(",")"]                                 # list of opening and closing parentheses
digits = ["0","1","2","3","4","5","6","7","8","9"]      # list of all possible digits

def dotCount(string1):              # function that returns number of "." in string1
    dot_count = 0
    for character in string1:
        if character == ".":
            dot_count += 1
    return dot_count

def tokenization(expr):
    expr_as_list = list(expr)                                                                       # converts given string into a list
    tokens = []                                                                                     # initialise tokens to an empty list

    i = 0
    while i < len(expr_as_list):                                                                    # ensures that iterations cover entire list
        if expr_as_list[i] in symbols or expr_as_list[i] in parentheses:                            # checks if current element is a symbol or parentheses
            tokens.append(expr_as_list[i])                                                          # if so, append element into tokens
            i += 1                                                                                  # increment i by 1
        elif expr_as_list[i] in digits:                                                             # checks if current element is a digit
            float_number = ""                                                                       # if so, create an empty string assigned to float_number
            j = i                                                                                   # set value of j to value of i
            while j < len(expr_as_list) and (expr_as_list[j] in digits or expr_as_list[j] == "."):  # checks if current element is either a digit or a "." and makes sure j doenst go out of bounds
                if expr_as_list[j] == ".":              
                    if dotCount(float_number) < 1:                                                  # checks if current element is a "." and number of "." in float_number is < 1
                        float_number += expr_as_list[j]                                             # if so, concatenate float_number with current element
                        j += 1                                                                      # increment j by 1
                    else:                                                                           
                        j += 1                                                                      # if not, increment j by 1
                else:                                                                               # if current element is a digit
                    float_number += expr_as_list[j]                                                 # concatenate float_number with current element
                    j += 1                                                                          # increment j by 1
            float_number = float(float_number)                                                      # after while loop, convert float_number to a float
            tokens.append(float_number)                                                             # append float_number to tokens
            i = j                                                                                   # set value of i to value of j
        else:
            i += 1                                                                                  # if not any of the above, increment i by 1

    return tokens                                                                                   # return tokens

#print(tokenization("(3.1 + 6*2^2) * (2 - 1)"))             # expected output : [(,3.1,+,6.0,*,2.0,^,2.0,),*,(,2.0,-,1.0,)]
#print(tokenization("12.63*(25.243^8 + (32.12-2^2))"))      # expected output : [12.63,*,(,25,243,^,8.0,+,(,32.12,-,2.0,^,2.0,),)]
#print(tokenization("(3.1+12.56) * (2.01-11.23^(2-12))"))   # expected output : [(,3.1,+,12.56,),*,(,2.01,-,11.23,^,(,2.0,-,12.0,),)]


# (b)

def has_precedence(op1, op2):
    high_operators = ["^"]                                                              # list of operators with highest precedence
    middle_operators = ["*","/"]
    low_operators = ["+","-"]

    if op1 == op2:                                                                      # checks if both operators are the same
        return False
    elif op1 in high_operators and op2 in high_operators:                               # checks if both operators are in the same precedence class
        return False
    elif op1 in middle_operators and op2 in middle_operators:
        return False
    elif op1 in low_operators and op2 in low_operators:
        return False
    elif op1 in high_operators and (op2 in middle_operators or op2 in low_operators):   # checks if op1 is in a higher precedence class than op2
        return True
    elif op1 in middle_operators and op2 in low_operators:                              # checks if op1 is in a higher precedence class than op2
        return True
    else:
        return False

#print(has_precedence("*","+"))      # expected output : True
#print(has_precedence("^","+"))      # expected output : True
#print(has_precedence("*","^"))      # expected output : False
#print(has_precedence("*","/"))      # expected output : False

     
def simple_evaluation(tokens):
    copy_of_tokens = tokens[:]                                                                  # assign a copy of tokens to copy_of_tokens
    
    a = 0                                                                                       # set value of a to 0
    while "^" in copy_of_tokens:                                                                # loop repeatedly executes as long as ^ is in copy_of_tokens
        if copy_of_tokens[a] == "^":                                                            # checks if current element is ^
            evaluated_value = pow(copy_of_tokens[a-1], copy_of_tokens[a+1])                     # if so, calculate value of element to the left raised to the power of the element to the right
            copy_of_tokens = copy_of_tokens[:a-1] + [evaluated_value] + copy_of_tokens[a+2:]    # reset copy_of_tokens to have the 3 evaluated elements replaced by the evaluated_value
            a = 0                                                                               # set value of a back to 0
        else:                                                                                   
            a += 1                                                                              # if current element is not ^, increment a by 1

    b = 0
    while "*" in copy_of_tokens or "/" in copy_of_tokens:                                       # same process as above but now for * and /
        if copy_of_tokens[b] == "*":
            evaluated_value = copy_of_tokens[b-1] * copy_of_tokens[b+1]
            copy_of_tokens = copy_of_tokens[:b-1] + [evaluated_value] + copy_of_tokens[b+2:]
            b = 0
        elif copy_of_tokens[b] == "/":
            evaluated_value = copy_of_tokens[b-1] / copy_of_tokens[b+1]
            copy_of_tokens = copy_of_tokens[:b-1] + [evaluated_value] + copy_of_tokens[b+2:]
            b = 0
        else:
            b += 1

    c = 0
    while "+" in copy_of_tokens or "-" in copy_of_tokens:                                       # same process as above but now for + and -
        if copy_of_tokens[c] == "+":
            evaluated_value = copy_of_tokens[c-1] + copy_of_tokens[c+1]
            copy_of_tokens = copy_of_tokens[:c-1] + [evaluated_value] + copy_of_tokens[c+2:]
            c = 0
        elif copy_of_tokens[c] == "-":
            evaluated_value = copy_of_tokens[c-1] - copy_of_tokens[c+1]
            copy_of_tokens = copy_of_tokens[:c-1] + [evaluated_value] + copy_of_tokens[c+2:]
            c = 0
        else:
            c += 1

    return float(copy_of_tokens[0])                                                             # return the first element of copy_of_tokens as a float

#print(simple_evaluation([2,"+",3,"*",4,"^",2,"+",1]))                               # expected output : 51.0
#print(simple_evaluation([3,"*",4,"*",5,"+",2,"^",2,"-",6]))                         # expected output : 58.0
#print(simple_evaluation([2,"^",2,"^",2,"^",2]))                                     # expected output : 256.0
#print(simple_evaluation([2,"^",2,"*",2,"^",2]))                                     # expected output : 16.0
#print(simple_evaluation([1.5,"*",8,"^",2,"+",6,"-",5,"/",2.5,"*",3,"^",2,"+",9]))   # expected output : 93.0
#print(simple_evaluation([10,"-",5,"*",4,"^",2,"+",100,"/",4]))                      # expected output : -45.0


# Additional Function

def open_count(lst):                    # function to return the number of open parentheses in given lst
    openCount = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            openCount += 1
    return openCount


# (c)

def complex_evaluation(tokens):
    copy_of_tokens = tokens[:]                                                                      # assign a copy of tokens to copy_of_tokens

    i = 0                                                                                           # set value of i to 0
    while open_count(copy_of_tokens) > 0:                                                           # loop repeatedly executes as long as there are opening parentheses inside copy_of_tokens
        if copy_of_tokens[i] == "(":                                                                # checks if current element is an (
            start = i                                                                               # if so, set value of start to current value of i
            i += 1                                                                                  # increment i by 1
        elif copy_of_tokens[i] == ")":                                                              # checks if current element is a )
            end = i                                                                                 # set value of end to current value of i
            evaluated_value = simple_evaluation(copy_of_tokens[start+1:end])                        
            copy_of_tokens = copy_of_tokens[:start] + [evaluated_value] + copy_of_tokens[end+1:]
            i = 0
        else:
            i += 1                                                                                  # if not ( or ), increment i by 1

    return simple_evaluation(copy_of_tokens)                                                        # perform simple_evaluation on copy_of_tokens, and return the output

#print(complex_evaluation(["(",2,"-",7,")","*",4,"^","(",2,"+",1,")"]))              # expected output : -320.0
#print(complex_evaluation(["(","(",2,"-",7,")","*",4,"^","(",2,"+",1,")",")"]))      # expected output : -320.0
#print(complex_evaluation(["(",0,")"]))                                              # expected output : 0.0
#print(complex_evaluation(["(","(",10,"-",5,")","*",4,"^",2,"+",100,")","/",4]))     # expected output : 45.0


def evaluation(string):
    result_tokens = tokenization(string)                # convert the given string into a token using tokenization
    return complex_evaluation(result_tokens)            # perform complex evaluation on the tokens and return the output

#print(evaluation("(2-7) * 4^(2+1)"))                        # expected output : -320.0
#print(evaluation("2+3*(4^2)"))                              # expected output : 50.0
#print(evaluation("(8*2)/(3^2)*(1+2)+(3-1)"))                # expected output : 7.33333
#print(evaluation("(3*2/3 + (4^1) - 8)"))                    # expected output : -2.0
#print(evaluation("(3+2)"))                                  # expected output : 5.0
#print(evaluation("(5+(5+(5+5)))"))                          # expected output : 20.0
#print(evaluation("5^(2^2)"))                                # expected output : 625.0
#print(evaluation("(0)"))                                    # expected output : 0.0
#print(evaluation("1+2*3/7^(2^2)"))                          # expected output : 1.0024989
#print(evaluation("(9*9) + (3*2^(1+2*(8-3*(1^0))*2)/2)"))    # expected output : 3145809.0
#print(evaluation("(((((1)))))"))                            # expected output : 1.0
#print(evaluation("1.23*(8.27/6.42^(2.2*1.74))"))            # expected output : 0.00824454
#print(evaluation("12.34*13.456"))                           # expected output : 166.04703999
#print(evaluation("(5)"))                                    # expected output : 5.0
#print(evaluation("4^3^2"))                                  # expected output : 4096.0
