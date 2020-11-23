# NAME : BRYAN HOOI YU ERN
# ID : 30221005
# EMAIL : bhoo0006@student.monash.edu
# ASSIGNMENT 1

########################################################################################################################
# TASK 1 : SORTING WITH RADIX SORT

def create_count_array(base):
    """
    This function returns an list of size base and having an empty list as each element in the list.
    :param base: an integer to determine the size of the returned list
    :return: a list of size base containing empty lists as each element
    @time complexity : O(b) whereby b is the value of base. The for loop performs base number of iterations
                       and appending an empty list to the generated empty list in each iteration. It is assumed
                       that appending would require O(1) time.
    @space complexity : Total - O(b) whereby b represents the memory space required to generate a list of size base.
                                The input base would always occupy a constant amount of space since it's an integer so
                                the space required by the input is O(1).
                        Auxiliary - O(b) since the outArray would take up an extra b amount of space in memory.
    """
    outArray = []
    for i in range(base):
        outArray.append([])
    return outArray

def radix_sort(num_list,b):
    """
    This function uses a stable counting sort algorithm as an inner subroutine to sort the given input list of integers
    in ascending order. It sorts the numbers based on their representation in the given base b.
    :param num_list: a list containing positive integers up to and including 2**64 - 1
    :param b: an integer whose value is at least 2
    :return: a list containing every element in num_list sorted in ascending order
    @time complexity : O(N) + O(M) + O(M) + O(b) + O(N) + O(M(N+N+b)) --> O(2N) + O(2M) + O(b) + O((2N+b)M)
                       --> O(N) + O(M) + O(b) + O((N+b)M) --> O((N+b)M + N + M + b) --> O((N+b)M). Here, N
                       represents the number of elements in the given input list, b is the value of the given
                       base, and M is the number of digits of the largest number in the input list, when represented
                       in base b.

    @space complexity : Total - O(N+b) whereby N is the number of elements in the given input list and b is the
                                value of the given base.
                        Auxiliary - O(N+b). It would not take O(M(N+b)) amount of extra space since Python's garbage
                                    collector will clear out the de-referenced count_array each time the counting
                                    sort subroutine is completed for that column.
    """

    # empty lists will be immediately returned
    # time complexity : len() operation is O(1) so O(1)
    if len(num_list) == 0:
        return num_list

    # finding maximum value in num_list
    # this requires traversing through the entire list which would require O(N) time
    # whereby N is the number of elements in the given list
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num

    # obtaining number of digits required to represent max_value in base b
    # number of integer divisions depends on the actual value of the given integer
    # which would take O(M) time whereby M is the number of digits of the maximum value when represented in base b
    num_digits = 0
    while max_value != 0:
        max_value = max_value // b
        num_digits += 1

    # creating an empty count array to tabulate occurrences of values in base b from 0 up to b-1
    # this would take O(b) amount of time for execution
    count_array = create_count_array(b)

    # copying every element from num_list into another array
    # iterating through every element in the input list so running time is O(N). It is also assumed that
    # appending to another list costs O(1) time.
    resultList = []
    for element in num_list:
        resultList.append(element)

    # performing counting sort on the values in the original list represented in base b at column i for each element in the list whereby
    # i ranges from 0 to num_digits - 1

    # outer for loop determines the number of times the counting sort subroutine is performed. This is dependent
    # on the number of digits of the largest number in the input list when represented in base b so there are
    # O(M) iterations required.
    for col in range(num_digits):

        # obtaining the respective value for the current column in base b representation for each element in
        # resultList. Number of iterations is O(N) since number of elements in resultList is N. The mathematical
        # operations within the loop along with the appending actions all require O(1) time.
        for element in resultList:
            value_in_base_b = (element//b**col) % b
            count_array[value_in_base_b].append(element)

        # traversing every inner list in the count_array and placing every element found into the resultList
        # at the right positions. Total number of actions required would be O(N) since the total number of elements
        # within each inner list in the count_array is equal to the total number of elements from the input list.
        index = 0
        for inner_list in count_array:
            for value in inner_list:
                resultList[index] = value
                index += 1

        # recreating a new count_array for the next column values. O(b) time required here.
        count_array = create_count_array(b)

    return resultList

########################################################################################################################
# TASK 2 : ANALYSIS

def time_radix_sort():
    from random import randint
    from timeit import default_timer

    # generating a list of size 100000 that contains integer from the range 1 - 2**64 - 1
    test_data = [randint(1, (2**64) - 1) for _ in range(100000)]
    output = []

    # timing each radix sort process and appending the results as a tuple to the output list
    b = [2,4,10,25,50,75,100,1000,10000,50000,100000,500000,1000000]
    for base in b:
        start_time = default_timer()
        radix_sort(test_data,base)
        time_taken = default_timer() - start_time
        output.append((base,time_taken))
    return output

########################################################################################################################
# TASK 3 : FINDING ROTATIONS

def rotate_string(inString, p):
    """
    This function shifts the first/last p elements of inString to the left/right depending on the value of p.
    :param inString: a string containing only lowercase letters
    :param p: an integer
    :return: inString which is the original string after shifting based on p
    @time complexity : O(M) whereby M is the length(number of characters) of inString. This occurs when inString is at least 1
                       character or more.
    @space complexity : Total - O(M) whereby M is the size of the input string since O(M) space is required for
                                the input string and another O(M) as auxiliary space.
                        Auxiliary - O(M) whereby M is size/length of the input string. Slicing requires the creation of
                                    copies of the input string of size p and M-p so the total auxiliary space is O(M).
    """
    stringLength = len(inString)  # O(1) time

    if stringLength == 0 or p % stringLength == 0:    # special cases whereby the result would be the same as the input
        return inString

    normalized_p = p % stringLength     # ensure p fits within a range from 0 to stringLength - 1

    inString = inString[normalized_p:] + inString[:normalized_p]

    return inString

def left_pad(inString, pad_char, max_length):
    """
    This function returns a string with max_length determined amount of pad_char's added to the end of inString.
    :param inString: a string containing lower-case alphabets
    :param pad_char: a single character
    :param max_length: an integer
    :return: a string with max_length - len(inString) number of pad_char concatenated to inString
    @time complexity : O(M) whereby M is max_length. The building of the extra_padding string requires O(M) number of
                       iterations.
    @space complexity : Total - O(L + M) whereby L is the number of characters in inString and M is max_length.
                        Auxiliary - O(M) whereby M is max_length. An additional string of size M may be created in the worst
                                    case (when the input string is an empty string).
    """
    num_pads_required = max_length - len(inString)
    extra_padding = ""
    for _ in range(num_pads_required):
        extra_padding += pad_char
    inString = inString + extra_padding
    return inString

def string_radix_sort(lst,max_chars):
    """
    This function utilizes a stable counting sort as a subroutine to sort the input list of strings in lexicographic order
    :param lst: a list containing strings of which every letter in the string is a lower-case alphabet or a padding character
    :param max_chars: an integer representing the length of the longest string in the input list
    :return: None
    @time complexity : O(NM) whereby N represents the number of elements in the input list and M is the length of the longest
                       string in the input list which determines the number of counting sorts to be performed. Each counting
                       sort requires O(N) amount of work to be done.
    @space complexity : Total - O(N) whereby N is the amount of space occupied by the input lst.
                        Auxiliary - O(N). The actual extra space occupied is O(N+b) but since b is constant no matter the
                                    input the space occupied is actually just O(N) which involves N amount of extra memory
                                    spaces in the count array to store the input elements.
    """

    # creating an empty count array to tabulate occurrences of values from 0 up to b-1
    # this would take O(b) amount of time for execution but since b is always constant no matter the input therefore
    # this can be regarded as O(1) time required.
    count_array = create_count_array(27)

    # performing counting sort on each letter for every element in lst with the letter converted into its ASCII value
    # and normalized to be within the range 0 to b-1
    for c in range(max_chars-1, -1, -1):
        for element in lst:
            current_char_ascii = ord(element[c]) - 96
            count_array[current_char_ascii].append(element)

        index = 0
        for inner_list in count_array:
            for value in inner_list:
                lst[index] = value
                index += 1

        # recreating a new count_array for the next set of letters. O(b) time required here.
        count_array = create_count_array(27)

def find_dup(lst):
    """
    This function separates the unique and duplicate values from a given list of comparable elements and returns the
    index at which the duplicate elements start appearing.
    :param lst: a list of comparable elements
    :return: j+1 <--- an integer representing the index of the first duplicate element from the input list
    @time complexity : O(N) whereby N is the number of elements in the input list. The algorithm involves going through
                       the first N-1 elements of the input list and performing some O(1) operations for each element.
    @space complexity : Total - O(N) whereby N is the amount of space occupied by the input
                        Auxiliary - O(1). Constant additional space required for variables i and j.
    """
    i, j = 0,0
    while i < len(lst) - 1:
        if lst[i+1] == lst[j]:
            i += 1
        else:
            lst[i+1], lst[j+1] = lst[j+1], lst[i+1]
            i += 1
            j += 1
    return j+1

def remove_left_pad(inString, pad_char):
    """
    This function returns a string with all the pad_char's removed from the input string.
    :param inString: a string
    :param pad_char: a single letter string
    :return: the input string with all the pad_char's removed
    @time complexity : Best Case - O(1). This occurs when the first letter of the input string is a pad_char and the for
                                   loop breaks after 1 iteration
                       Worst Case - O(N) whereby N is the length of the input string. This occurs when the pad_char does not
                                    appear as the first element in the string. Returning a slice of the input string up to
                                    index i also requires O(N) time
    @space complexity : Total - O(N) whereby N is the amount of space occupied by the input string.
                        Auxiliary - O(N) whereby N is the amount of space required to create a slice of the input string
    """
    found = False
    for i in range(len(inString)):
        if inString[i] == pad_char:
            found = True
            break

    if found:
        return inString[:i]
    else:
        return inString

def find_rotations(string_list, p):
    """
    This function returns a list containing all the strings whose p-rotations also appear in the original list.
    :param string_list: a list containing strings whereby each character is a lower-case alphabet
    :param p: an integer to represent the number of left/right rotations for the strings
    :return: a list containing all the strings whose p-rotations also appear in the original list
    @time complexity : O(NM) whereby N is the number of strings in the input list and M is the length of the longest string
                       in the input list.
    @space complexity : Total - O(N+M) whereby N is the amount of space occupied by the input list and M is the space occupied
                                by the longest string in the input list.
                        Auxiliary - O(N+M).
    """

    # creating a list to store each element of string_list after p-rotations. This would require O(NM) time as every string
    # from the input list is taken and rotated by p. Each rotation costs O(M) time whereby M is the length of the longest
    # string among the list of strings.
    rotated_elements = []
    for element in string_list:
        rotated_element = rotate_string(element, p)
        rotated_elements.append(rotated_element)

    # creating a list that contains the original strings along with their rotated counterparts. This would cost O(2N) -> O(N)
    # time as every element from both lists are moved into the new list
    all_elements = string_list + rotated_elements

    # obtaining the longest string in the all_elements list. This would require iterating through every element in all_elements
    # which would take O(N) time followed by some constant operations during each iteration so complexity is O(N).
    longest = all_elements[0]
    for i in range(1, len(all_elements)):
        if len(all_elements[i]) > len(longest):
            longest = all_elements[i]

    # left padding every string in all_elements with len(longest)- len(string) characters which have ASCII value 96.
    # This would cost O(NM) time whereby M is the length of the longest string in the input list and every string in
    # all_elements has to undergo left padding.
    padding_char = chr(96)  # since "a" is 97, character with ASCII value 96 is used to represent 0 value character
    max_length = len(longest)
    for i in range(len(all_elements)):
        padded_string = left_pad(all_elements[i], padding_char, max_length)
        all_elements[i] = padded_string

    # sorting the elements in lexicographic order using a modified version of radix sort with base 27 to represent all
    # possible alphabets in the given strings including the padding character. This would take O(2NM)-> O(NM) time whereby N is
    # the number of elements in the input list and M is the length of the longest string in the input list.
    string_radix_sort(all_elements,max_length)

    # moving all the duplicates that appear in the sorted list to the back and obtaining a slice of all_elements that only
    # contains all the duplicates within. The time complexity here is O(N) since find_dup() requires going through each element
    # except the last in the given list and obtaining a slice of all_elements starting from starting_index is also O(N).
    starting_index = find_dup(all_elements)
    duplicates = all_elements[starting_index:]

    # removing the extra padding characters from each element in duplicates. This would take O(NM) time as the number of
    # duplicates may equal the number of initial strings given in the input list in the worst case. N here is the number
    # of duplicates there are and M represents the length of the longest string in the duplicates which equals the length
    # of the longest string in the original input list.
    for i in range(len(duplicates)):
        removed_padding = remove_left_pad(duplicates[i], padding_char)
        duplicates[i] = removed_padding

    # performing reverse p-rotations on each element in the duplicates list in order to obtain a list of the original
    # strings whose p-rotated versions also exist in the input list. This would required O(NM) time whereby N is the
    # number of duplicates there are and M represents the length of the longest string in the duplicates list.
    for i in range(len(duplicates)):
        reverse_rotated_version = rotate_string(duplicates[i], -p)
        duplicates[i] = reverse_rotated_version

    return duplicates