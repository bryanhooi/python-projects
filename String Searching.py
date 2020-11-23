"""
Student Name : Bryan Hooi Yu Ern
Student ID : 30221005
Student Email : bhoo0006@student.monash.edu
Assignment 3 - TRIES
"""

# TASK 1 - TRIE

class Node:
    """
    Class to represent the insertion of each "character" into the Trie. Note that the Node object does not actually hold
    information regarding the actual characters being inserted. It instead stores an array of size 27(number of lowercase
    English alphabets plus a terminating character) that holds information regarding the possible edges that link to other
    Nodes as part of a branch in the Trie. Each node also stores information about the number of occurrences of the character
    represented by the Node as a prefix as well as the number of times the exact string ending with the Node has been inserted.
    In addition, it also takes in an integer word_index (None by default) that represents the index of the string from the
    original input list of strings passed into the Trie.

    Note that all terminating Nodes have a prefix_count of 0, a string_count of at least 1, and word_index that isn't None.
    Note that all non-terminating Nodes have a string_count of 0 and a prefix_count of at least 1.
    """

    def __init__(self, prefix_count, string_count, word_index=None):
        """
        Constructor method for the Node class. Initializes the necessary variables that every Node possesses.
        :param prefix_count: an integer representing the number of words that have the character represented by this Node as a prefix
        :param string_count: an integer representing the number of words inserted whose last character is the character represented by this
                             Node.
        :param word_index: an integer (None by default or if no argument given) that represents the index of the sring from the
                           original input list of strings passed into the Trie to be inserted.
        :return : a reference to the instantiated Node object.
        @time complexity : O(1) - creating the links array takes O(27) but is constant regardless of the inputs so therefore it is O(1)
        @space complexity : Total : O(1) - input parameters occupy O(1) space and variables within also occupy O(1) space
                            Auxiliary : O(1) - variables all occupy O(1) extra space
        """
        self.links = [None] * 27
        self.prefix_count = prefix_count
        self.string_count = string_count
        self.word_index = word_index

class Trie:
    """
    Class that represents a Trie data structure. Trie objects contain Nodes grouped together upon instantiation in a multi-way
    tree structure. Each Node is created and inserted into the Trie during its creation via an input list of non-empty strings.
    The Trie class contains a set of methods that allows for querying certain properties of the input list of strings such as
    the number of occurrences of a given string, the number of strings that have a particular prefix, and providing a list of
    lexicographically arranged strings such that each of them have a particular wildcard prefix.
    """

    def __init__(self, text):
        """
        Constructor for the Trie class that initializes the root of the Trie to a Node object. The root Node represents the
        empty string (the root is a prefix for every string stored in the Trie). It accepts a list of strings as input and
        constructs the Trie with the build_trie method.
        :param text: a list of non-empty strings containing only lowercase English alphabets.
        @time complexity : Best Case - O(1) when the input list of strings is empty
                           Worst Case - O(T) whereby T is the total number of characters over all strings in the input list
                                        and occurs when the input list is not empty.
        @space complexity : Total - O(T) for the space occupied by the input list of strings as well as the auxiliary space
                                    required from the creation and insertion of Nodes to represent each character.
                            Auxiliary - O(T) for each Node inserted.
        """

        # sets the root to a Node
        self.root = Node(0, 0)

        # assigns a variable to the input list of strings. text occupies O(T) space whereby T is the total number of characters
        # over all strings in the list.
        self.text = text

        # builds the Trie using build_trie and passing text in
        self.build_trie(text)

    def build_trie(self, words):
        """
        Method to insert Nodes to represent each character of each string of the given input list of strings as part of
        building the Trie.
        :param words: a list of non-empty strings to be inserted into the Trie via the insert method
        :return: None
        @time complexity : O(T) whereby T is the total number of characters over every string in the input list
        @space complexity : Total : O(T) - worst case when list contains all unique strings. Best case O(t) involving list
                                           containing all duplicates and t is the length of any of the strings within.
                            Auxiliary : O(T) - number of new Nodes(each representing the character) inserted
        """

        # calling insert for every string in the input list of strings. Requires O(T) running time whereby T is the total
        # number of characters over every string in the input list. Also creates O(T) new Nodes (not exactly T as duplicate
        # words don't involve new Node insertions occupies O(T) space.
        for i in range(len(words)):
            # prefix_count of the root Node represents the number of strings inserted.
            self.root.prefix_count += 1
            # inserting each string into the Trie. O(q) running time here whereby q is the length of the current string
            # being inserted.
            self.insert(words[i], i)

    def insert(self, word, word_index):
        """
        Method to insert a string into the Trie and setting the index of the string inserted (from the input list of strings)
        in the word_index variable of the terminating Node.
        :param word: a non-empty string representing the word to be inserted into the Trie
        :param word_index: an non-negative integer representing the index of the string in the input list of strings that is currently
                           being inserted into the Trie.
        :return: None
        @time complexity : O(q) whereby q is the length of the input string.
        @space complexity : Total - O(q) whereby q is the length of the input string in the worst case
                            Auxiliary - O(q) for each new Node added in the worst case (new Node needs to be inserted
                                        for each character)
        """

        # every insertion begins from the root Node.
        current_node = self.root

        # iterating through every character in the input string and determines the next Node to visit based on
        # the index of the character. If there isn't a Node at the next location, then a Node is inserted before
        # the new Node is set as the current Node, else no new Node is inserted before changing the current Node.
        # loop runs in O(q) whereby q is the length of the input string. If the input string is not present in the Trie,
        # then O(q) space is occupied by the new Nodes created in the worst case.
        for char in word:
            index_of_char = ord(char) - 96
            # if the character is not found in the links array of the current Node.
            if current_node.links[index_of_char] is None:
                # insertion of a new Node in the links array of the current Node.
                current_node.links[index_of_char] = Node(1, 0)
                # setting the current Node to that newly inserted Node.
                current_node = current_node.links[index_of_char]
            else:
                # if the character already exists, increment the prefix_count of the Node representing the character by 1
                # before setting the current Node to that Node.
                current_node.links[index_of_char].prefix_count += 1
                current_node = current_node.links[index_of_char]

        # after handling every character, add a terminating Node to the element at index 0 of the links array if there isn't
        # one right there and pass the word_index as a parameter to the terminating Node.
        if current_node.links[0] is None:
            current_node.links[0] = Node(0, 1, word_index)
        else:
            # if there is one, increment the Node's string_count by 1 to indicate a duplicate string has been inserted.
            current_node.links[0].string_count += 1

    # TASK 2 - STRING FREQUENCY

    def string_freq(self, query_str):
        """
        Method that returns the number of words in the Trie that exactly match query_str. Returns 0 if there are no words
        in the Trie that exactly match query_str.
        :param query_str: a non-empty string containing only lowercase English alphabets.
        :return: number of strings in the Trie that exactly match query_str
        @time complexity : Best Case - O(1) if the first character of query_str is not found in the Trie from the root Node
                           Worst Case - O(q) whereby q is the length of query_str and query_str is present within the Trie
        @space complexity : Total - O(q)
                            Auxiliary - O(1)
        """

        # search begins from the root Node
        current_node = self.root

        # search through Trie for each character in query_str. Next node to go to is determined by the element at index(char)
        # of the links list of the current Node. If at any point during the loop that no Node is found at index(char), then
        # it indicates there is no string that matches query_str and 0 is returned. This loop runs O(q) times whereby q is the
        # length of query_str and O(1) space is occupied by the internal variables.
        for char in query_str:
            index_of_char = ord(char) - 96
            if current_node.links[index_of_char] is not None:
                current_node = current_node.links[index_of_char]
            else:
                return 0

        # answer is stored in the terminating Node's(if there is one) string_count or 0 if there isn't a terminating Node.
        if current_node.links[0] is not None:
            return current_node.links[0].string_count
        else:
            return 0

    # TASK 3 - PREFIX FREQUENCY

    def prefix_freq(self, query_str):
        """
        Method that returns the number of strings in the Trie that have query_str as a prefix.
        :param query_str: a possibly empty string containing only lowercase English alphabets.
        :return: the number of strings in the Trie that have query_str as a prefix.
        @time complexity : Best Case - O(1) when the first character of query_str is already not found from the root Node.
                           Worst Case - O(q) whereby q is the length of query_str and query_str exists as a prefix in the Trie.
        @space complexity : Total - O(q)
                            Auxiliary - O(1)
        """

        # search begins from the root Node
        current_node = self.root

        # an empty string is a prefix of all strings which means an empty input string will produce the total number of words
        # from the original input list of strings. This value is stored in the root Node's prefix_count.
        if len(query_str) == 0:
            return current_node.prefix_count

        # search through the Trie for each character in query_str. Similar process as string_freq above. This requires O(q)
        # running time whereby q is the length of query_str and O(1) extra space for local variables.
        for char in query_str:
            index_of_char = ord(char) - 96
            if current_node.links[index_of_char] is not None:
                current_node = current_node.links[index_of_char]
            else:
                return 0

        # if the prefix is found(return 0 not executed throughout for-loop execution), then the current_node's prefix_count
        # holds the number of strings from the original input list that have query_str as a prefix.
        return current_node.prefix_count

    # TASK 4 - WILDCARD PREFIX SEARCH

    def wildcard_prefix_freq(self, query_str):
        """
        Method that returns a list of all strings in the original input list that have query_str, which contains a single
        wildcard, as a prefix.
        :param query_str: a non-empty string that contains a single wildcard character and only lowercase English alphabets.
        :return: a list that contains every string in the original list of strings, arranged in lexicographical order,
                 that have query_str as a prefix.
        @time complexity : Best Case - O(1) when the first character in query_str is found in the Trie from the root Node.
                           Worst Case - O(q + S) whereby q is the length of query_str and S is the total number of characters
                                        over all strings (including duplicates) in the original input list of strings that have
                                        query_str as the prefix.
        @space complexity : Total - O(q + S)
                            Auxiliary - O(S) whereby S is also the total number of recursive calls made by the subsequent
                                        find_all_strings method to search through and visit every Node in the sub-Tries that
                                        have all the different possible prefixes of query_str as the root.
        """

        # the search for query_str in the Trie begins at the root Node
        current_node = self.root

        # list for which every string found with query_str as a prefix is appended to. O(1) time required to generate
        # and may possibly occupie O(L) space for each element whereby L is the number of strings in the entire Trie.
        result_words = []

        # iterate through every index of query_str in search for it as a prefix in the Trie. Will run O(q) amount of times
        # whereby q is the length of query_str. Total work done is O(q + S). The q component comes from searching the Trie
        # for the query_str and S is defined below.
        for i in range(len(query_str)):
            current_char = query_str[i]
            current_char_index = ord(current_char) - 96

            # once the wildcard character is found, another loop is initiated which searches through the current Node's
            # links array for Nodes that represents a character that can replace the wildcard character. For each Node found,
            # finish_query_search is called which run up to O(27) times but the total number of work done depends on the number
            # of Nodes visited from here onwards. The finish_query_search method will take O(R) time whereby R is the total number
            # of Nodes visited until a terminating Node is found in the sub-Trie. This is done for each link found. So the total
            # time complexity of this operation is O(S) whereby S is the total number of characters of all strings in the
            # input list(duplicates included) which have the prefix matching query_str. This is also the total number of Nodes
            # visited as a result of this entire process.
            if current_char == "?":
                for j in range(1, len(current_node.links)):
                    if current_node.links[j] is not None:
                        next_node = current_node.links[j]
                        self.finish_query_search(next_node, query_str, i+1, result_words)
                break
            else:
                # if current character is not a wildcard character, then resume the query_str search in the Trie as usual.
                if current_node.links[current_char_index] is not None:
                    current_node = current_node.links[current_char_index]
                else:
                    return result_words

        return result_words

    def finish_query_search(self, current_node, query_str, next_index, result_words):
        """
        Method that considers every existing character that can replace the wildcard character in query_str and for each
        selected character, finishes the search for the rest of query_str (if any characters after the wildcard) and obtains
        all strings/words that exists with the given wildcard-replaced query_str as a prefix.
        :param current_node: a reference to the current Node (represents any character exists to replace the wildcard) being analyzed.
        :param query_str: a non-empty string representing the prefix of every word to be searched and obtained.
        :param next_index: an integer representing the next index of query_str to continue the search from.
        :param result_words: a possibly empty list that will store every string found with query_str as a prefix in lexicographical
                             order
        :return: None
        @time complexity : Best Case - O(1) when the current Node does not have a link to the current character being looked at in
                                       query_str.
                           Worst Case - O(R) whereby R is the total number of Nodes visited in the sub-Trie rooted at the
                                        current Node in the subsequent find_all_strings calls. This occurs when the query_str
                                        with this Node's character representation replacing the wildcard is found in the Trie.
        @space complexity : Total - O(M) from number of recursive calls in the call stack as a result of find_all_strings whereby
                                    M is the length of the deepest path taken in the recursive calls to reach a terminating Node.
                            Auxiliary - O(M).
        """

        # completes the search for the query_str in the Trie with the current character being a character that replaces the
        # wildcard. Requires O(len(query_str) - next_index) amount of time to run. All inner operations run in O(1) time and
        # only requires O(1) auxiliary space for the loop variables. Immediately returns None and exits the method if current
        # Node does not have a link to the current character of the query_str (indicating the prefix doesn't exist in the Trie).
        for i in range(next_index, len(query_str)):
            current_char = query_str[i]
            current_char_index = ord(current_char) - 96
            if current_node.links[current_char_index] is not None:
                current_node = current_node.links[current_char_index]
            else:
                return None

        # if execution reaches here, it means that query_str with the wildcard character replaced by the character represented
        # by the current Node exists in the Trie. With this query_str as a prefix, the for loop iterates through and searches
        # for all existing links to this Node. For each link, it calls find_all_strings which will search for and obtain the strings
        # in every terminating Node of the sub-Trie rooted at the linked Node found (next_node here). The running time of this
        # operating depends on the total number of Nodes visited in the sub-Trie rooted by the current Node which can be denoted
        # as O(R). No insertion of Nodes or operations that require more than O(1) space complexity is required here.
        for i in range(len(current_node.links)):
            if current_node.links[i] is not None:
                next_node = current_node.links[i]
                self.find_all_strings(next_node, result_words)

    def find_all_strings(self, current_node, result_words):
        """
        Recursive method that traverses through sub-Trie rooted at current_node for terminating Nodes. Once a terminating
        Node is found, the word_index of that Node is used to obtain the original string from the input list of strings to
        be appended to result_words.
        :param current_node: reference to the current Node being analyzed
        :param result_words: a reference to a list containing all strings collected during the traversal
        :return: None
        @time complexity : Best Case - O(string_count) when the current Node is a terminating Node and string_count is the
                                       number of occurrences of the string obtained by the word_index of the terminating Node.
                           Worst Case - O(N) whereby N is the total number of Nodes in the sub-Trie rooted at the current
                                        Node and occurs when the current Node isn't a terminating Node. This represents the total
                                        number of recursive calls made in order to find every terminating Node from the sub-Trie
        @space complexity : Total - O(M) whereby M the length of the deepest path taken in the recursive calls to reach a
                                    terminating Node. M can also be the length of the longest string with prefix up to the
                                    character represented by the current Node.
                            Auxiliary - O(M)
        """

        # once a terminating Node is reached(determined by checking if the current Node's prefix_count is 0), then the
        # current Node's word_index is obtained and used to determine which string in the input list of strings is to be
        # accessed and appended to result_words. To handle duplicates, the current Node's string_count determines the number
        # of times the string obtained by word_index is to be appended. This runs in O(string_count) time and only requires
        # O(1) auxiliary space for loop variables.
        if current_node.prefix_count == 0:
            for i in range(current_node.string_count):
                index_of_word = current_node.word_index
                result_words.append(self.text[index_of_word])
        else:
            # if current Node isn't a terminating Node, then traversal continues to all its linked Nodes that are not None by
            # recursively calling itself with the next Node to visit as determined by the links found on the current Node. This will
            # search and find all terminating Nodes that stem from the current Node which takes O(N) time whereby N is the
            # number of Nodes in the sub-Trie rooted at the current Node.
            for i in range(len(current_node.links)):
                if current_node.links[i] is not None:
                    # obtaining a reference to the next Node to visit based on the current Node's links array.
                    next_node = current_node.links[i]
                    self.find_all_strings(next_node, result_words)
