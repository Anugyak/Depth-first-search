
#Input Graph
graph = {
    "S": ["A", "B", "C"], "A": ["S", "D", "E"], "B": ["S", "D", "F"],
    "C": ["S", "E", "F"], "D": ["A", "B"], "E": ["A", "G", "H"],
    "F": ["B", "C", "G", "H"], "G": ["E", "F"], "H": ["E", "F"] }
#Initializing a Empty List Named Visited
visited = []
def dfs(graph, node):
    """ This Function Takes Graph and Starting Node as Input and Outputs The Traversing Order According to Depth First Search"""
    #Making Visited List as Global
    global visited
    #If node not in visited, add it to visited
    if node not in visited:
        visited.append(node)
         #Finding All Neighboring Nodes
        for n in graph[node]:
            #Considering each node as Starting Node
            dfs(graph, n)

#Calling Dfs Function with Input Graph and Starting Node as 'S'
dfs(graph,"S")
print("\nUsing dfs: ")
print(visited)






