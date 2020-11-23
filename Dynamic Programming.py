"""
Student Name : Bryan Hooi Yu Ern
Student ID   : 30221005
Student Email : bhoo0006@student.monash.edu
Assignment 2
"""


# TASK 1 : OSCILLATIONS

def longest_oscillation(L):
    """
    This function accepts as input a list of integers and outputs a tuple containing the length of the longest oscillation
    in the input list along with a list of indices of those elements that make up the longest oscillation.
    :param L: a list containing 0 or more integers
    :return: a tuple containing the length of the longest oscillation in the input list and a list of indices of those
             elements that make up the longest oscillation.
    @time complexity : O(N) whereby N is the length of the input list
    @space complexity : Total :O(N) whereby N is the length of the input list.
                        Auxiliary : O(N) space required by the memo array.
    @OPTIMAL/SUB-OPTIMAL SOLUTION: OPTIMAL SOLUTION
    """
    # sets up a variable to hold the length of the longest oscillation found in the input list (longest) and another
    # variable assigned with a list containing the indices of the elements in the input list that make up the longest
    # oscillation (indices). Declaration of these variables requires O(1) time and takes up O(1) space although size of
    # indices may increase up to N whereby N is the size of the input list.
    longest = 0
    indices = []

    # base case 1 : if empty list is passed in, then longest oscillation is always 0 and indices (solution) is empty.
    # time complexity of len() is O(1) and O(1) auxiliary space required since indices is empty when return statement is executed.
    if len(L) == 0:
        return (longest,indices)

    # base case 2 : if every element in the given list is the same, then longest oscillation is always 1 with indices containing
    # one element which can be any index of the elements from the given list. Here, the first index (0) is always selected. There
    # will a loop to go through the input list to determine if there are only duplicates within which takes at most N - 1 iterations
    # which gives this process a running time of O(N) with O(1) auxiliary space required for the variables.
    all_duplicates = True
    for i in range(len(L) - 1):
        if L[i] != L[i+1]:
            all_duplicates = False
            break

    if all_duplicates:
        longest = 1
        indices.append(0)
        return (longest,indices)


    # creating a memoization array of length N whereby N is the length of the input list. memo occupies O(N) auxiliary space
    # base case 3 : an list containing 1 element has a longest oscillation length of 1 which is why the first element in the
    # memo table is set to 1 (memo[i] refers to the length of the longest oscillation in L[:i+1])
    # also creating a variable to hold the current status of the longest oscillation involving elements in L[:i+1]. Can be neutral,
    # increasing, or decreasing.
    memo = [0] * len(L)
    memo[0] = 1
    oscillation_status = "Neutral"

    # iterating from the second to the last element of the memo array. Requires O(N) time.
    for i in range(1, len(memo)):
        # looking at current element L[i] and given the current oscillation status is either neutral, increasing, or decreasing,
        # determine whether element L[i] can contribute itself to the oscillation sequence or not and determine the
        # new oscillation status. Entire if-elif-else block requires O(1) time to execute at every iteration.
        if oscillation_status == "Neutral":
            if L[i] > L[i-1]:
                memo[i] = 1 + memo[i-1]
                oscillation_status = "Increasing"
            elif L[i] < L[i-1]:
                memo[i] = 1 + memo[i-1]
                oscillation_status = "Decreasing"
            else:
                memo[i] = memo[i-1]
        elif oscillation_status == "Increasing":
            if L[i] < L[i-1]:
                memo[i] = 1 + memo[i-1]
                oscillation_status = "Decreasing"
            else:
                memo[i] = memo[i-1]
        else:
            if L[i] > L[i-1]:
                memo[i] = 1 + memo[i-1]
                oscillation_status = "Increasing"
            else:
                memo[i] = memo[i-1]

    # process of backtracking to determine the indices of the elements that make up the longest oscillation. Total iterations
    # in the worst possible case is N which makes the time cost of backtracking O(N).
    i = len(memo) - 1
    while i >= 0:
        # take the current element if length of longest oscillation did change from previous position to current position
        # in the memo list. At every iteration, i is decremented by at least 1 so maximum number of iterations is N which
        # gives the time complexity of O(N) for this loop. O(1) auxiliary space is required for the variables within.
        if memo[i] != memo[i-1]:
            indices.append(i)
            i -= 1
        else:
            # if length of longest oscillation did not change, then take the current element and reduce i until it reaches
            # position of memo that shows a change in length, or exit loop if no further changes occur.
            indices.append(i)
            memo_value = memo[i]
            i -= 2

            if i >= 0:
                while memo[i] == memo_value and i >= 0:
                    i -= 1

                if i == 0:
                    indices.append(i)
                    i -= 1

    # reversing the indices list. Knowing that the elements will always be sorted in descending order, it is possible to
    # reverse the list by swapping the first and last elements, then the second and second last elements, and so on for
    # N//2 times. So time complexity here is O(N) and no auxiliary space is required.
    for i in range(len(indices)//2):
        indices[i], indices[len(indices) - (i+1)] = indices[len(indices) - (i+1)], indices[i]


    # the length of the longest oscillation in the input list is stored at the last position in the memo list.
    longest = memo[-1]

    return (longest, indices)

########################################################################################################################

# TASK 2 : INCREASING WALK

def longest_walk(M):
    """
    This function takes as input a two-dimensional matrix M of integers and returns the length of the longest walk through
    those elements along with a list of positions for those elements involved in the longest walk.
    :param M: a matrix with N rows of size M each, containing integers only
    :return: a tuple containing the length of the longest walk in the matrix along with the list of positions of those elements
             that are involved in that walk.
    @time complexity : O(NM) whereby N is the number of rows in the input and M is the length of each row
    @space complexity : Total : O(NM) whereby N is the number of rows in the input and M is the length of each row
                        Auxiliary : O(NM) which is taken up by the memoization table
    OPTIMAL/SUB-OPTIMAL SOLUTION : OPTIMAL SOLUTION
    """

    # initialize two variables to hold the length of the longest walk and the set of tuples that represent the path consisting
    # of elements in that walk.
    longest = 0
    solution = []

    # base case : if M is empty or each inner list is of size 0, then longest is 0 and the solution is an empty list
    if len(M) == 0 or len(M[0]) == 0:
        return (longest,solution)

    # a list containing all 8 possible position offsets of adjacent positions in the matrix for any particular position. This
    # list is always the same size regardless of the input matrix so O(1) auxiliary space required here
    directions = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

    # creating a memo table of exactly the same dimensions as the input matrix with each element in the memo table initialized
    # to None. This requires O(NM) running time whereby N is the number of rows and M is the length of each row in the matrix.
    # The memo table itself occupies O(NM) auxiliary space.
    num_rows = len(M)
    col_width = len(M[0])
    memo = [None] * num_rows
    for i in range(num_rows):
        memo[i] = [None] * col_width

    # starting_row and starting_col are variables that will hold the row and col indexes of the memo table whose element
    # will be the length of the longest walk in the entire matrix after all the iterations end. prev_longest will just be a
    # variable that will determine if the starting_row and starting_col updates after each iteration.
    starting_row, starting_col = 0, 0
    prev_longest = longest

    # here, memo[i][j] will hold the length of the longest walk whereby the starting element is element at M[i][j]. For each
    # position memo[i][j] that is initially None, its value will be determined by 1 + the maximum of its adjacent cells provided
    # the corresponding element from the matrix at those cells are greater than the one at M[i][j] ( this means it can form a walk
    # with the element in its adjacent cell, but it selects the cell which would give it the longest walk at that moment).
    for i in range(num_rows):
        for j in range(col_width):
            # if memo[i][j] is already filled (not None), then just update the longest, starting_row, and starting_col
            # values accordingly. For these iterations, amount of time required is O(1) and space occupied by auxiliary
            # variables is O(1) as well.
            if memo[i][j] is None:
                valid_directions = []
                # iterate through every tuple in directions and determine the positions of adjacent elements to the current
                # position such that they are valid positions and the element at M[new_row][new_col] is greater than element
                # at M[i][j]. For these valid positions, append the row and col values to valid_directions. This loop requires
                # O(1) running time and valid_directions will occupy O(1) auxiliary space
                for row,col in directions:
                    new_row, new_col = i+row, j+col
                    if (0 <= new_row < num_rows) and (0 <= new_col < col_width) and (M[i][j] < M[new_row][new_col]):
                        valid_directions.append((row,col))

                # if an element has no valid adjacent positions, then set memo[i][j] to 1. If it does have them, then determine
                # the length of the longest walk for elements in those positions via a recursive call into longest_walk_aux.
                # Every recursive call to an element at position i,j will populate memo[i][j] with a value. So total number of
                # recursive calls to fill the entire memo table is NM which is why the running time overall is O(NM) since
                # an element will never be called twice. The reference to the memo table and directions list is passed into
                # the auxiliary function so that total auxiliary space required by the recursive call stack is always maintained
                # at O(NM).
                if len(valid_directions) != 0:
                    memo[i][j] = 1
                    for row,col in valid_directions:
                        new_row, new_col = i+row, j+col
                        # No need to perform a recursive call if there already is an element at memo[new_row][new_col],
                        # just requires an O(1) operation to update value at memo[i][j]. Else, perform the recursive call
                        # to obtain the value at memo[new_row][new_col].
                        if memo[new_row][new_col] is None:
                            memo[i][j] = max(memo[i][j], 1 + longest_walk_aux(M, memo, new_row, new_col, directions))
                        else:
                            memo[i][j] = max(memo[i][j], 1 + memo[new_row][new_col])
                else:
                    memo[i][j] = 1

            # at the end of each iteration, update longest to be the larger value between itself and the value at memo[i][j].
            # The prev_longest variable helps determine if the starting_row and starting_col has to be changed.
            prev_longest = longest
            longest = max(longest, memo[i][j])
            if longest != prev_longest:
                starting_row, starting_col = i, j

    # backtracking process to determine the set of elements involved in the longest walk. Start at the position in memo that
    # holds the largest value, then select the element at the current position before moving on. The next position to move
    # to will be the one that holds the value such that it is one lesser than the previous value. Do this until the element
    # at the current position is 1. Maximum number of iterations that can happen is NM which gives this process a time
    # complexity of O(NM) and only requires O(1) auxiliary space.
    current_row = starting_row
    current_col = starting_col
    solution.append((current_row,current_col))
    while memo[current_row][current_col] != 1:
        found = False
        for row,col in directions:
            new_row, new_col = current_row + row, current_col + col
            if (0 <= new_row < num_rows) and (0 <= new_col < col_width):
                if memo[current_row][current_col] - memo[new_row][new_col] == 1:
                    found = True
                    solution.append((new_row,new_col))
                    current_row = new_row
                    current_col = new_col

            if found:
                break

    return (longest,solution)

def longest_walk_aux(M,memo,i,j,directions):
    """
    This function serves as an auxiliary function for longest_walk as its recursive component to determine and return the length
    of the longest walk starting from the position in the memo table that this function was called for.
    :param M: a matrix with N rows of size M each, containing integers only
    :param memo: a list of lists that is of dimensions NxM, memo[i][j] holds the length of the longest walk starting with
                 the element at M[i][j]
    :param i: an integer to represent the row coordinate
    :param j: an integer to represent the column coordinate
    :param directions: a list containing all 8 possible position offsets of adjacent positions in the matrix for any particular position.
    :return: the value at memo[i][j]
    """

    # obtain the number of rows and length of each row from the input matrix M
    num_rows = len(memo)
    col_width = len(memo[0])

    # iterate through every tuple in directions and determine the positions of adjacent elements to the current
    # position such that they are valid positions and the element at M[new_row][new_col] is greater than element
    # at M[i][j]. For these valid positions, append the row and col values to valid_directions. This loop requires
    # O(1) running time and valid_directions will occupy O(1) auxiliary space
    valid_directions = []
    for row, col in directions:
        new_row, new_col = i + row, j + col
        if (0 <= new_row < num_rows) and (0 <= new_col < col_width) and (M[i][j] < M[new_row][new_col]):
            valid_directions.append((row, col))

    # if an element has no valid adjacent positions, then set memo[i][j] to 1. If it does have them, then determine
    # the length of the longest walk for elements in those positions via a recursive call into longest_walk_aux.
    # Every recursive call to an element at position i,j will populate memo[i][j] with a value. So total number of
    # recursive calls to fill the entire memo table is NM which is why the running time overall is O(NM) since
    # an element will never be called twice. The reference to the memo table and directions list is passed into
    # the auxiliary function so that total auxiliary space required by the recursive call stack is always maintained
    # at O(NM).
    if len(valid_directions) != 0:
        memo[i][j] = 1
        for row, col in valid_directions:
            new_row, new_col = i + row, j + col
            if memo[new_row][new_col] is None:
                memo[i][j] = max(memo[i][j], 1 + longest_walk_aux(M, memo, new_row, new_col, directions))
            else:
                memo[i][j] = max(memo[i][j], 1 + memo[new_row][new_col])
    else:
        memo[i][j] = 1

    return memo[i][j]

