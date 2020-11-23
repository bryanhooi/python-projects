"""
Student Name : Bryan Hooi Yu Ern
Student ID : 30221005
Student Email : bhoo0006@student.monash.edu
Assignment 4 - GRAPHS
"""


from math import inf
# TASK 1 - SETUP

class Vertex:
    """
    Class to represent vertices in the graph object to be created. Each vertex holds necessary information in the form of
    its variables such that they assist in facilitating tasks 2 and 3. As part of the adjacency list representation of
    the graph, each Vertex will have a list called edges that will contain 0 or more Edge objects that represent any vertices
    that the Vertex is adjacent to (there exists an edge between them). The only information required to be passed in during
    Vertex creation is the unique id for the Vertex and this id ranges from 0 to n-1 whereby n is the total number of
    vertices to be made part of the graph.
    """

    def __init__(self, id):
        """
        Constructor for the Vertex class. Accepts an integer id that uniquely identifies the Vertex to be created in the
        graph. Also appropriately initializes all of the Vertex's necessary variables.
        :param id: an integer in the range 0 to n-1 to represent the Vertex.
        @time complexity : O(1) - each variable's declaration and initialization requires O(1) running time.
        @space complexity : Total - O(1) as the input parameter and auxiliary space taken up by the variables is O(1).
                            Auxiliary - O(1).
        """

        # unique identifier for the Vertex
        self.id = id

        # set of adjacent vertices to this Vertex in the form of a list of Edges
        self.edges = []

        # following variables are in some shape or form required by the breadth-first search or Dijkstra's algorithm in
        # tasks 2 and 3
        self.discovered = False
        self.visited = False
        self.edges_from_source = 0
        self.distance_from_source = inf
        self.predecessor = None
        self.is_ice = False
        self.is_ice_cream = False

    def add_edge(self, v, weight):
        """
        Function to add an edge between this Vertex and the Vertex specified by the id v with the given weight. Takes in
        two integer parameters, v which is the id of the Vertex for which an Edge will now be formed between the two with
        weight as the weight of this Edge.
        :param v: an integer to represent the id of the adjacent Vertex
        :param weight: an integer to represent the weight/distance of the Edge added.
        :return: None
        @time complexity : O(1) amortized. Creation of the Edge object is O(1) and appending to the edges list is amortized
                           O(1).
        @space complexity : Total - O(1) since the input parameters occupy O(1) space and the new Edge object created occupies
                                    O(1) auxiliary space.
                            Auxiliary - O(1)
        """

        # creation of an Edge object with this Vertex's id passed in along with the function's input parameters followed
        # by the addition of the Edge into this Vertex's edges list.
        edge = Edge(self.id, v, weight)
        self.edges.append(edge)

class Edge:
    """
    A class to represent an edge between two vertices. Each Edge object has three variables to represent the id's of the
    two vertices for which this Edge exists between along with the weight of this Edge.
    """

    def __init__(self, u, v, w):
        """
        Constructor for the Edge class. Takes in three input parameters and initializes its variables according to these
        inputs.
        :param u: an integer representing the vertex id of one of the vertices.
        :param v: an integer representing the vertex id of the other Vertex.
        :param w: an integer to represent the weight of this Edge between vertices with id u and v.
        @time complexity : O(1) as all operations performed are assignment operations.
        @space complexity : Total - O(1). Input and internal variables all occupy O(1) space.
                            Auxiliary - O(1).
        """

        self.u = u
        self.v = v
        self.w = w

class Queue:
    """
    A class to represent a queue with an array-based implementation. Objects of this type will be useful in task 2 as it
    requires a breadth-first search. The Queue class provides some important operations such as adding and serving data to
    and from the Queue along with a function to check if the Queue is currently empty or not. With its array-based implementation
    pointers to the front and rear of the Queue are required to facilitate the append and serve operations.
    """

    def __init__(self, capacity):
        """
        Constructor for the Queue class. Takes in an integer capacity which allocates the fixed size for its underlying array.
        Also initializes the pointers to the front and rear of the Queue appropriately.
        :param capacity: an integer to represent the size of the underlying array of the Queue which will be fixed.
        @time complexity : O(capacity) from creation of a Python list with capacity number of elements initialized to None.
                           During usage, capacity will be equal to V whereby V is the total number of vertices in the graph
                           so the appropriate running time would be O(V).
        @space complexity : Total - O(V) as the input takes up O(1) space but the underlying array takes up O(V) space.
                            Auxiliary - O(V).
        """

        # initializing the underlying array to a fixed size capacity
        self.underlying_array = [None] * capacity

        # sets the front and rear pointer to initially point at position 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        """
        Function that returns True if the Queue is empty and False otherwise.
        :return: True if Queue is empty, False otherwise.
        @time complexity : O(1).
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # if the front and rear pointer are at the same position, then it means that the Queue is empty.
        return self.front == self.rear

    def append(self, item):
        """
        Function to add an item to the Queue.
        :param item: a variable of any type representing the item to be added into the Queue.
        :return: None
        @time comeplexity : O(1)
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # sets the element at the position pointed by rear to the input item
        self.underlying_array[self.rear] = item

        # increment rear pointer by 1 to set it to the next available position for an append.
        self.rear += 1

    def serve(self):
        """
        Function that removes and returns the item at the front of the Queue.
        :return: item at position indicated by the front pointer.
        @time complexity : O(1).
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # retrieves the item at the front of the Queue
        item = self.underlying_array[self.front]

        # increment the front pointer by 1 to simulate the removal of an item at the front of the Queue
        self.front += 1
        return item

class PriorityQueue:
    """
    A class to represent a Min-Heap data structure with an underlying array implementation to be used in Dijkstra's
    algorithm in task 3. The PriorityQueue object is created with a integer passed in to indicate the maximum possible
    items to be present within the Min-Heap structure. It also stores a list containing the locations (by index) of each
    item in the Min-Heap. The class also contains several useful Min-Heap operations such as adding an item, removing the
    item with the minimum value and also checking if the Min-Heap is empty.
    """

    def __init__(self, capacity):
        """
        Constructor for the PriorityQueue class. Accepts as input an integer to determine the size of the underlying array
        that acts as the Min-Heap structure. Also uses that integer to create an array of that size such that each index
        represents the id of the inserted Vertex and the element at each index represents the position of that Vertex in
        the underlying array currently. Along with that, it sets a variable which will point to the index of the last element
        in the Min-Heap to 0 initially. Note that the element at index 0 in the Min-Heap is permanently set to None and will
        not be accessed to facilitate the class's other functions so if V vertices are to be inserted, then capacity should
        be V + 1 to account for this.
        :param capacity: an integer to decide the capacity of the Min-Heap.
        @time complexity : O(capacity) or O(V) whereby V is the total number of vertices in the graph. Declaring and initializing
                           the Min-Heap and vertex_positions lists require time depending on the capacity input.
        @space complexity : Total - O(V) as the input parameters only occupy O(1) space but the Min-Heap and vertex_positions
                                    lists occupy O(V) auxiliary space.
                            Auxiliary - O(V).
        """

        # list to represent the Min-Heap data structure
        self.min_heap = [None] * capacity

        # list to hold the positions of each Vertex in the Min-Heap
        self.vertex_positions = [None] * capacity

        # pointer to the last element in the Min-Heap. Set to 0 initially or when Min-Heap is empty
        self.end_of_heap = 0

    def is_empty(self):
        """
        Function to determine if the Min-Heap is empty or not.
        :return: True if value of end_of_heap is 0, False otherwise.
        @time complexity : O(1).
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        return self.end_of_heap == 0

    def add(self, vertex):
        """
        Function to insert a new item/Vertex into the Min-Heap.
        :param vertex: the Vertex object to be inserted into the Min-Heap.
        :return: None
        @time complexity : Best Case - O(1) when rise() function takes O(1) due to Vertex distance value being greater than
                                       the first parent Vertex's distance value or if the Vertex added is the first element
                                       added to the Min-Heap.
                           Worst Case - O(log V) whereby V is the total number of vertices in the graph or capacity of the
                                        Min-Heap. This is completely dependent on the running time of rise().
        @space complexity : Total - O(1) as the input Vertex occupies a constant amount of space.
                            Auxiliary - O(1) as the local variables all occupy constant amount of space.
        """

        # the vertices in the Min-Heap will be arranged based on their distance_from_source values
        data = vertex.distance_from_source

        # a tuple containing the input Vertex along with their corresponding distance is stored in the Min-Heap
        self.min_heap[self.end_of_heap + 1] = (vertex, data)

        # setting the position of the added Vertex in the heap using the Vertex's id as the index. The +1 here is to
        # accommodate the fact that the element at position 0 is off-limits. So a Vertex with id 0 is stored at index
        # 1 and so on.
        self.end_of_heap += 1
        self.vertex_positions[vertex.id + 1] = self.end_of_heap

        # perform a rise on the new Vertex added.
        self.rise(self.end_of_heap)

    def rise(self, k):
        """
        Function that will be called after an addition of an item into the Min-Heap. It shifts the newly inserted item up
        the Min-Heap depending on its value so that the property of the Min_Heap is maintained.
        :param k: the current index of the newly added item.
        :return: None
        @time complexity : Best Case - O(1) which occurs either if its the first item to be inserted into the Min-Heap for
                                       which rising is unnecessary or when the item inserted has value larger than its parent
                                       item in the Min-Heap.
                           Worst Case - O(log V) whereby V is the total number of items in the Min-Heap. Due to its binary tree
                                        structure, the maximum height of the Min-Heap (which is also the maximum number of times
                                        an item can be swapped with its parent) is log V.
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # loop is executed if the current index is not 1 (root element) or if the parent element is larger than the current
        # element
        while k > 1 and self.min_heap[k][1] < self.min_heap[k//2][1]:
            current_vertex_id = self.min_heap[k][0].id + 1
            parent_vertex_id = self.min_heap[k//2][0].id + 1

            # swaps the parent and current elements in the Min-Heap and also their positions in the vertex_positions list.
            self.min_heap[k], self.min_heap[k//2] = self.min_heap[k//2], self.min_heap[k]
            self.vertex_positions[current_vertex_id], self.vertex_positions[parent_vertex_id] = self.vertex_positions[parent_vertex_id], self.vertex_positions[current_vertex_id]

            # move up one layer in the binary tree.
            k = k//2

    def smallest_child(self, k):
        """
        Function that returns the index of the smallest child of a given element in the Min-Heap.
        :param k: the index of the item/element for which the index of its smallest child will be determined and returned.
        :return: index of the element at position k's smallest child.
        @time complexity : O(1).
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # if the element at index k only has a left child or if the left child's value is less than the right child's value
        # then the index of the left child is returned. Else, the right child's index is returned. 2*k and 2*k + 1 represents
        # the indices of the left and right child respectively due to the Min-Heap's binary tree structure.
        if 2*k == self.end_of_heap or self.min_heap[2*k][1] < self.min_heap[2*k + 1][1]:
            return 2*k
        else:
            return 2*k + 1

    def sink(self, k):
        """
        Function that will be called whenever pop_min() is called so that the elements in the Min-Heap are rearranged so
        as to maintain its Min-Heap property. It involves an element being shifted/swapped down a layer or several layers
        along the Min-Heap.
        :param k: the index of the element for which the sink operation is carried out on.
        :return: None
        @time complexity : Best Case - O(1) when the all of the smallest child's value is already greater than the current
                                       element's value or if the current element has no children.
                           Worst Case - O(log V) when every consecutive child element has value smaller than the current
                                        element's value which causes it to be shifted all the way down to the last level
                                        of the Min-Heap which in the worst case involves moving through log V levels.
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # loop executes as long as the current element has a child
        while 2 * k <= self.end_of_heap:
            child = self.smallest_child(k)

            # breaks out of the loop if the child element has value greater than the current element
            if self.min_heap[k][1] <= self.min_heap[child][1]:
                break
            current_vertex_id = self.min_heap[k][0].id + 1
            child_vertex_id = self.min_heap[child][0].id + 1

            # swaps the current element with the child element in the Min-Heap as well as updating their new positions
            self.min_heap[k], self.min_heap[child] = self.min_heap[child], self.min_heap[k]
            self.vertex_positions[current_vertex_id], self.vertex_positions[child_vertex_id] = self.vertex_positions[child_vertex_id], self.vertex_positions[current_vertex_id]
            k = child

    def pop_min(self):
        """
        Function that returns the minimum element in the Min-Heap (always the element at the top of the Min-Heap).
        :return: the Vertex with the minimum distance_from_source value among those present in the Min-Heap.
        @time complexity : Best Case - O(1) if sink() is O(1).
                           Worst Case - O(log V). Also dependent on sink().
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # obtain the Vertex to be returned and its corresponding id
        return_vertex = self.min_heap[1][0]
        return_vertex_id = return_vertex.id + 1

        # id of the last Vertex in the Min-Heap
        last_vertex_id = self.min_heap[self.end_of_heap][0].id + 1

        # swaps the Vertex to be returned with the last Vertex in the Min-Heap and updates their positions. The position
        # of the Vertex to be returned is set to None as it will no longer be regarded as present within the Min-Heap.
        self.min_heap[1], self.min_heap[self.end_of_heap] = self.min_heap[self.end_of_heap], self.min_heap[1]
        self.vertex_positions[return_vertex_id], self.vertex_positions[last_vertex_id] = self.vertex_positions[last_vertex_id], self.vertex_positions[return_vertex_id]
        self.vertex_positions[return_vertex_id] = None
        self.end_of_heap -= 1

        # perform a sink on the current first Vertex (which was formerly the last Vertex in the Min-Heap)
        self.sink(1)
        return return_vertex

    def decrease_key(self, vertex, new_data):
        """
        Function to change the distance_from_source value of a Vertex currently present within the Min-Heap and updates
        its position in the Min-Heap.
        :param vertex: the Vertex in the Min-Heap for which the data change is to be applied to.
        :param new_data: the new distance_from_source value for that Vertex which will always be lesser than its old value.
        :return: None
        @time complexity : Best Case - O(1) whereby the Vertex's new distance value does not alter its position in the Min-Heap.
                           Worst Case - O(log V) whereby V is the total number of vertices or capacity of the Min-Heap and log V
                                        is the running time of rise().
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """

        # obtain the position of the input vertex in the Min-heap based on its id
        heap_position = self.vertex_positions[vertex.id + 1]

        # set the element at that position in the Min-Heap to be a new tuple containing the Vertex with its updated value
        # and perform a rise.
        self.min_heap[heap_position] = (vertex, new_data)
        self.rise(heap_position)

class Graph:
    """
    Class to represent a connected, undirected, and simple graph. It the vertices and edges in the form of an adjacency
    matrix and receives its graph information in the form of a text file containing information regarding the number of
    vertices in the graph along with each line representing an edge present within.
    """

    def __init__(self, gfile):
        """
        Constructor for the Graph class. Saves the input filename to a variable for use later on and calls process_file()
        to convert the information in the input text file into an adjacency list representation of the graph.
        :param gfile: a text file containing necessary information regarding the graph to be formed.
        @time complexity : Best Case - O(1).
                           Worst Case - O(V^2) dependent on process_file().
        @space complexity : Total - O(V + E).
                            Auxiliary - O(V + E) occupied by the adjacency list.
        """
        self.filename = gfile
        self.graph = self.process_file(self.filename)

    def process_file(self, gfile):
        """
        Function that reads and processes the information within the input text file into an adjacency list representing
        the graph. Time complexity of reading and processing the text within the file will not be taken into consideration
        as they are trivial to the overall complexity of the function.
        :param gfile: a text file containing information regarding the graph to be built.
        :return: an adjacency list representing the graph formed from the text file information.
        @time complexity : O(E) whereby E is the total number of edges or lines indicated in the text file. For a dense
                           graph, the number of edges is O(V^2) whereby V is the number of vertices in the graph so the
                           running time here can be written as O(V^2).
        @space complexity : Total - O(V + E). The adjacency list has O(V) number of elements and each element represents a Vertex
                                    that holds a set of possible edges depending on the information in the text file. All of the
                                    edges total to O(E) which is the space occupied by all of the edges in the graph.
                            Auxiliary - O(V + E) taken up by the adjacency list.
        """

        # opens the file in read mode and converts each line into a string in a list
        file = open(gfile, "r")
        text = file.readlines()

        # creates an empty list to represent the adjacency list
        adjacency_list = []

        # iterating through every line in the text file. O(E) running time required here
        for i in range(len(text)):
            line = text[i].strip("\n")

            # first line of the text file contains the number of vertices in the graph which is used to initialize the
            # adjacency list. O(V) running time here whereby V is the value given in the line.
            if i == 0:
                num_vertices = int(line)
                adjacency_list = [None] * num_vertices

                # if the graph only has one Vertex, then inserts a Vertex with id 0 into the adjacency list
                if num_vertices == 1:
                    adjacency_list[0] = Vertex(0)
            else:
                # for each edge represented in the subsequent lines, the Vertex ids and weights are retrieved such that
                # a new Vertex is added into the adjacency list if the Vertex not present prior. If a Vertex already exists,
                # then the corresponding Edge is added.
                edge = line.split()
                vertex_u_id, vertex_v_id, weight_w = int(edge[0]), int(edge[1]), int(edge[2])
                if adjacency_list[vertex_u_id] is None:
                    adjacency_list[vertex_u_id] = Vertex(vertex_u_id)
                    adjacency_list[vertex_u_id].add_edge(vertex_v_id, weight_w)
                else:
                    adjacency_list[vertex_u_id].add_edge(vertex_v_id, weight_w)

                # case for undirected graphs, an Edge between Vertex u and v is bi-directional and has to be added a second
                # time in the adjacency list to from Vertex v to u as well.
                if adjacency_list[vertex_v_id] is None:
                    adjacency_list[vertex_v_id] = Vertex(vertex_v_id)
                    adjacency_list[vertex_v_id].add_edge(vertex_u_id, weight_w)
                else:
                    adjacency_list[vertex_v_id].add_edge(vertex_u_id, weight_w)

        # closing the file and returning the adjacency list
        file.close()
        return adjacency_list

    # TASK 2 - SHALLOWEST SPANNING TREE

    def shallowest_spanning_tree(self):
        """
        Function that find the shallowest spanning tree that can be formed from the graph and returns a tuple containing
        the root Vertex of that spanning tree and its corresponding depth (number of edges from root to the deepest leaf)
        which is minimized each spanning tree found with each Vertex as the root.
        :return: tuple containing Vertex id of the root of the shallowest spanning tree and the corresponding depth of that
                 spanning tree.
        @time complexity : Best Case - O(V) for a one Vertex graph whereby the breadth-first search function only takes O(V)
                                       time to create the Queue and performs no further action.
                           Worst Case - O(V^3) whereby V is the total number of vertices in the graph and occurs for graphs
                                        with more than one Vertex.
        @space complexity : Total - O(V) for the Queue in the BFS.
                            Auxiliary - O(V).
        """

        # initialize the least_depth to positive infinity
        least_depth = inf

        # perform breadth-first search for each vertex in the graph and update the least_depth value so that it is
        # minimized over every spanning tree. Running time here is O(V * (V + E)) which simplifies to O(V * (V + V^2)) for
        # dense graphs. So it can be written as O(V^3). Space required here is dependent on the space required by the
        # breadth-first search function which is O(V)
        for vertex in self.graph:
            depth = self.breadth_first_search(vertex)
            if depth < least_depth:
                least_depth = depth
                answer = (vertex.id, depth)

            # resets all the internal variables of each Vertex to their default values so that the next breadth-first
            # search will not be affected
            self.reset_all_vertices()
        return answer

    def breadth_first_search(self, root):
        """
        Function that implements the breadth-first search algorithm that will be utilized to obtain a spanning tree of the
        graph that is rooted at a given source Vertex.
        :param root: the source Vertex of the spanning tree to be found.
        :return: the longest distance (number of edges) between the source Vertex and a leaf Vertex in the spanning tree.
        @time complexity : O(V + E) whereby V is the total number of vertices in the graph and E is the total number of edges
                           in the graph.
        @space complexity : Total - O(V) whereby the Queue occupies that amount of auxiliary space.
                            Auxiliary - O(V).
        """

        # creates a Queue with capacity equal to V to store discovered vertices.
        queue = Queue(len(self.graph))

        # adds the root Vertex into the Queue and makes the root a discovered Vertex.
        queue.append(root)
        root.discovered = True

        # a counter to record the current maximum depth of the spanning tree being built
        max_depth = 0

        # loop executes as long as the Queue is not empty. Queue can contain up to V discovered vertices
        # and it serves one every iteration so number of iterations is capped at O(V).
        while not queue.is_empty():
            # serves a Vertex from the Queue and mark it as a visited Vertex.
            u = queue.serve()
            u.visited = True

            # for each of its corresponding edges, discover the Vertex on the other end of that edge and update its
            # number of edges from the source. Total work done here over the entire while loop is O(E) for every edge
            # in the graph.
            for edge in u.edges:
                id_v = edge.v
                v = self.graph[id_v]

                # only consider vertices that have not been discovered or visited
                if not (v.discovered or v.visited):
                    v.discovered = True
                    v.edges_from_source = u.edges_from_source + 1

                    # updated max_depth if the current depth of the spanning tree has increased
                    max_depth = max(max_depth, v.edges_from_source)
                    queue.append(v)

        return max_depth

    def reset_all_vertices(self):
        """
        Function that resets the internal variable values of every Vertex in the graph to their default values which
        is useful for the task 2 function above.
        :return: None
        @time complexity : Best Case - O(1) for single Vertex graphs
                           Worst Case - O(V) whereby V is the number of vertices in the graph for a graph with 2 or more
                                        vertices.
        @space complexity : Total - O(1).
                            Auxiliary - O(1).
        """
        for vertex in self.graph:
            vertex.discovered = False
            vertex.visited = False
            vertex.edges_from_source = 0
            vertex.distance_from_source = inf
            vertex.predecessor = None
            vertex.is_ice = False
            vertex.is_ice_cream = False

    # TASK 3 - SHORTEST ERRANDS

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        """
        Function that calls modify_graph() and find_shortest_walk() in order to obtain the shortest path between the home
        and destination vertices such that it passes through an ice Vertex before an ice cream Vertex.
        :param home: the Vertex id of the source Vertex.
        :param destination: the Vertex id of the target Vertex.
        :param ice_locs: a list containing the Vertex ids of vertices that have ice.
        :param ice_cream_locs: a list containing the Vertex ids of vertices that have ice cream.
        :return: a tuple containing the length of the shortest walk/path between the home and destination vertices following
                 the given criteria, and the distance of that shortest walk/path.
        @time complexity : O(E log V) whereby V is the number of vertices in the original unmodified graph and E is the
                           total number of edges in the original unmodified graph.
        @space complexity : Total - O(V + E). The input lists ice_locs and ice_cream_locs may encompass every single Vertex
                                    in the original graph which takes up O(V) space. The two new graphs added by modify_graph()
                                    occupy O(V + E) auxiliary space.
                            Auxiliary - O(V + E).
        """

        # obtain the original number of vertices in the graph prior to graph modification
        original_num_vertices = len(self.graph)

        # call modify_graph to change the stucture of the graph to accommodate find_shortest_walk() which takes O(V + E) time.
        self.modify_graph(ice_locs, ice_cream_locs, original_num_vertices)

        # obtain the true destination considering the graph has been extended
        modified_destination = destination + (2 * original_num_vertices)

        # calling find_shortest_walk() to obtain the shortest walk length along with the walk itself as a list which requires
        # O(E log V) time.
        shortest_walk_length, walk = self.find_shortest_walk(home, modified_destination, original_num_vertices)

        # reprocess the graph so as to remove the excess vertices and reset everything by using process_file from task
        # 1 earlier which takes O(V^2) time.
        self.graph = self.process_file(self.filename)
        return shortest_walk_length, walk

    def modify_graph(self, ice_locs, ice_cream_locs, ori_num_vertices):
        """
        Function to add 2V vertices to the current graph to facilitate find_shortest_walk() later on. Each new Vertex added
        has its own unique id but they model the same original graph so essentially this function creates two copies of the
        original graph with the ice vertices connecting the original graph with the second graph and ice cream vertices
        connecting the second graph with the third graph.
        :param ice_locs: a list containing the vertex ids of vertices that contain ice.
        :param ice_cream_locs: a list containing the vertex ids of vertices that contain ice cream.
        :param ori_num_vertices: the number of vertices in the original unmodified graph.
        :return: None
        @time complexity : O(V + E) whereby V is the number of vertices in the original unmodified graph and E is the
                           total number of edges in the original unmodified graph.
        @space complexity : Total - O(V + E). The input lists ice_locs and ice_cream_locs may encompass every single Vertex
                                    in the original graph which takes up O(V) space. The two new graphs added occupy O(V + E)
                                    auxiliary space.
                            Auxiliary - O(V + E).
        """
        multiplier = 1

        # adds 2V new vertices into the current graph which takes O(V) time and extends the space occupied by O(V) as well
        for i in range(2 * ori_num_vertices):
            current_vertex_id = i % ori_num_vertices
            new_vertex = Vertex(current_vertex_id + (multiplier * ori_num_vertices))
            self.graph.append(new_vertex)
            if i == ori_num_vertices - 1:
                multiplier = 2

        multiplier = 1

        # iterate through the original V vertices in the graph twice to add all the necessary edges to the 2V new vertices
        # which takes O(V + E) time as every original Vertex and its corresponding edges are considered twice.
        for i in range(2 * ori_num_vertices):
            current_vertex_id = i % ori_num_vertices
            current_vertex = self.graph[current_vertex_id]
            corresponding_vertex = self.graph[current_vertex_id + (multiplier * ori_num_vertices)]
            for edge in current_vertex.edges:
                corresponding_target = edge.v + (multiplier * ori_num_vertices)
                corresponding_weight = edge.w
                corresponding_vertex.add_edge(corresponding_target, corresponding_weight)

            if i == ori_num_vertices - 1:
                multiplier = 2

        # for each Vertex id specified in ice_locs, sets thoses vertices is_ice value to be True along with their
        # corresponding vertices in the 2V vertices added as well which takes O(len(ice_locs)) running time. The
        # length of ice_locs is upper-bounded by V.
        for id in ice_locs:
            self.graph[id].add_edge(id + ori_num_vertices, 0)
            self.graph[id].is_ice = True
            self.graph[id + ori_num_vertices].is_ice = True
            self.graph[id + (2 * ori_num_vertices)].is_ice = True

        # for each Vertex id specified in ice_locs, sets thoses vertices is_ice_cream value to be True along with their
        # corresponding vertices in the 2V vertices added as well which takes O(len(ice_cream_locs)) running time. The
        # length of ice_cream_locs is upper-bounded by V.
        for id in ice_cream_locs:
            self.graph[id + ori_num_vertices].add_edge(id + (2 * ori_num_vertices), 0)
            self.graph[id].is_ice_cream = True
            self.graph[id + ori_num_vertices].is_ice_cream = True
            self.graph[id + (2*ori_num_vertices)].is_ice_cream = True

    def find_shortest_walk(self, home, destination, ori_num_vertices):
        """
        Function that implements Dijkstra's algorithm to find the distance of the shortest paths between every Vertex and
        the source/home Vertex. Specifically in this function, Dijkstra's algorithm is utilized such that the shortest path
        and distance of the path between the home and destination vertices is returned.
        :param home: the Vertex id of the source Vertex.
        :param destination: the Vertex id of the target Vertex.
        :param ori_num_vertices: the number of vertices in the graph prior to modification by modify_graph().
        :return: a tuple containing the shortest distance along the path between the home and destination vertices, and
                 a list containing the Vertex ids of the vertices visited along that shortest path.
        @time complexity : O(E log V) whereby V is the number of vertices in the original unmodified graph and E is the
                           total number of edges in the original unmodified graph.
        @space complexity : Total - O(V) whereby V is the number of vertices in the original unmodified graph. The PriorityQueue
                                    occupies O(V) auxiliary space and the space occupied by the inputs ice_locs and ice_cream_locs also
                                    occupy O(V) space in the worst case.
                            Auxiliary - O(V)
        """

        # retrieve the source Vertex using home as the Vertex id
        source = self.graph[home]

        # sets up a PriorityQueue(Min-Heap) of size one more than the number of vertices currently present in the graph
        # which is already modified at this point (contains 3V vertices). This requires O(V) running time whereby V is the
        # number of vertices in the original graph along with the PriorityQueue occupying O(V) auxiliary space.
        pq = PriorityQueue(len(self.graph) + 1)

        # sets the source Vertex's distance to 0 and adds the source Vertex into the PriorityQueue
        source.distance_from_source = 0
        pq.add(source)

        # loop executes as long as the PriorityQueue is not empty. In the worst case, every Vertex in the graph is removed
        # from the PriorityQueue which costs O(V log V) time and every edge is relaxed which costs O(E log V). For dense
        # graphs, E ~ V^2 which means E log V dominates V log V so the time complexity can be written as O(E log V).
        while not pq.is_empty():
            u = pq.pop_min()

            # every Vertex removed from the PriorityQueue is regarded as visited and will not be considered again
            u.visited = True
            for edge in u.edges:
                v = self.graph[edge.v]
                if not v.visited:
                    if v.discovered:
                        # edge relaxation which updates the distances of the vertices accordingly. O(log V) time here.
                        if u.distance_from_source + edge.w < v.distance_from_source:
                            new_distance = u.distance_from_source + edge.w
                            v.distance_from_source = new_distance
                            v.predecessor = u.id
                            pq.decrease_key(v, new_distance)
                    # newly discovered vertices have their distances updated and are added into the PriorityQueue which
                    # also takes O(log V) time.
                    else:
                        v.distance_from_source = u.distance_from_source + edge.w
                        v.predecessor = u.id
                        v.discovered = True
                        pq.add(v)

        # reconstructing the shortest path between home and destination by each Vertex's predecessor Vertex id to determine
        # which vertices were visited. The maximum length of the path taken is upper bounded by O(V).
        path_taken = []
        current_vertex = destination
        path_taken.append(current_vertex)
        while current_vertex != home:
            predecessor = self.graph[current_vertex].predecessor

            # if the current Vertex and its predecessor form a link between two graphs then they must have traversed through
            # a zero weight edge and thus the predecessor will not be considered along the path
            if not (predecessor == current_vertex - ori_num_vertices):
                path_taken.append(predecessor)
            current_vertex = predecessor

        # iterating through the Vertex ids and converting them to the ids belonging to the original unmodified graph to
        # obtain the true path. Again, this process requires O(V) running time in the worst case
        for i in range(len(path_taken)):
            if ori_num_vertices <= path_taken[i] <= (2*ori_num_vertices - 1):
                path_taken[i] = path_taken[i] - ori_num_vertices
            elif 2*ori_num_vertices <= path_taken[i] <= (3*ori_num_vertices - 1):
                path_taken[i] = path_taken[i] - (2*ori_num_vertices)

        # reversing the elements in the path_taken list which takes O(V//2) -> O(V) time as well
        for i in range(len(path_taken)//2):
            path_taken[i], path_taken[len(path_taken)-i-1] = path_taken[len(path_taken)-i-1], path_taken[i]

        return self.graph[destination].distance_from_source, path_taken
