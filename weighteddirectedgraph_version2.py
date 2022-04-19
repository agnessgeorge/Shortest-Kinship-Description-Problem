# Updates from version 1
# added a new parameter on the edges for the  "edge label", so every edge has four parameters (starting vertex, ....
# ending vertex, weight, label)
# .
# added a function that returns the label of the shortest weighted path
# .
# added a test at the end to check whether the obtained path is inside a defined set of strings, the set contains
# strings made from the available labels in the graph


from collections import defaultdict

# A class to represent a graph object


class Graph:

    def __init__(self, edges, n):
        self.V = n
        self.V_org = n
        self.graph = defaultdict(list)

        # A list of lists to represent an adjacency list
        self.adjList = [None] * n

        # allocate memory for the adjacency list
        for i in range(n):
            self.adjList[i] = []

        # add edges to the directed graph
        for (src, dest, weight, label) in edges:
            # allocate node in adjacency list from src to dest
            self.adjList[src].append((dest, weight))

    # function to add an edge to graph
    def add_edge(self, u, v, w, lbl):
        if w == 1:
            self.graph[u].append(v)
        else:
            # '''split all edges of weight 2 into two
            # edges of weight 1 each. The intermediate
            # vertex number is maximum vertex number + 1,
            # that is V.'''
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.V = self.V + 1

    # To print the shortest path stored in parent[]
    def print_path(self, parent, j):

        Path_len = 1
        if parent[j] == -1 and j < self.V_org:  # Base Case : If j is the source
            print(j)
            path_label.append(j)
            return 0  # when parent[-1] then path length = 0
        l = self.print_path(parent, parent[j])

        # increment path length
        Path_len = l + Path_len

        # print node only if it's less than original node length.
        # i.e. do not print any new node that has been added later
        if j < self.V_org:
            print(j)
            path_label.append(j)
        return Path_len

        # print("The label of the shortest path is ....", path_label)

    # ''' This function mainly does BFS and prints the
    # 	shortest path from src to dest. It is assumed
    # 	that weight of every edge is 1'''
    def find_shortest_path(self, so, de):

        # Mark all the vertices as not visited
        # Initialize parent[] and visited[]
        visited = [False] * self.V
        parent = [-1] * self.V

        # Create a queue for BFS
        queue = list()

        # Mark the source node as visited and enqueue it
        queue.append(so)
        visited[so] = True

        while queue:

            # Dequeue a vertex from queue
            s = queue.pop(0)

            # if s = de then print the path and return
            if s == de:
                return self.print_path(parent, s)

            # Get all adjacent vertices of the dequeued vertex s
            # If am adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = s


# Function to print adjacency list representation of a graph
def print_graph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()


def get_path_label(a_path_label):
    z = 0
    path = ""
    while z in range(0, len(a_path_label) - 1):

        a = a_path_label[z]
        b = a_path_label[z + 1]
        for (a1, a2, a3, a4) in edge:
            if (a, b) == (a1, a2):
                path += a4
            else:
                pass
        z += 1

    return path


# main.....................................................................................................

path_label = []
# Input: Edges in a weighted digraph
# Edge (x, y, w) represents an edge from `x` to `y` having weight `w`.......
edge = [(0, 1, 2, 'b'), (0, 2, 1, 'a'), (1, 2, 2, 'c'), (1, 3, 2, 'f'), (1, 4, 1, 'i'), (2, 0, 2, 'e'), (2, 1, 1, 'd'),
        (2, 3, 2, 'g'), (3, 2, 1, 'h'), (4, 5, 2, 'k'), (4, 3, 1, 'j'), (5, 4, 1, 'l')]

string_set = ["a", "aa", "ag", "aga", "aaa", "b", "bb", "bbb", "bf", "bij", "cc", "ccc", "cfg"]
another_string_set = ["a", "aa", "af", "aga", "aaa", "b", "bb", "bbb", "bf", "bij", "cc", "ccc", "cfg"]

# No. of vertices (labelled from 0 to 5)
nn = 6

h = Graph(edge, nn)
for (uu, vv, ww, ll) in edge:
    h.add_edge(uu, vv, ww, ll)

print_graph(h)

# assign values to source and destination and prints the shortest path
source1 = 0
dest1 = 3
print("\nShortest Path between %d and %d is " % (source1, dest1))

# prints the distance/ summed weight of the shortest path from source to destination

print("\nShortest Distance between %d and %d is %d \n" % (source1, dest1, h.find_shortest_path(source1, dest1)))

# print the string formed by the shortest path

print("The label of the shortest path is path is " + get_path_label(path_label))

# The tests below are just to check whether the shortest path obtained has its label in a predefined string set.
# Since for this particular case/example the label is "ag"
# The first test will pass and return "ag"
# The second test will fail and return "no solutions....."


print("\n.................................tests...........................................")
# check if the label of the shortest path is in the "string_set" list
if get_path_label(path_label) in string_set:
    print("\nThe shortest weighted path is ", get_path_label(path_label))
else:
    print("\nNo Solution i.e the path label is not in the string set")

# check if the label of the shortest path is in the "another_string_set" list
if get_path_label(path_label) in another_string_set:
    print("\nThe shortest weighted path is ", get_path_label(path_label))
else:
    print("\nNo Solution i.e the path label is not in the string set")
