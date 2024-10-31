# given graph(from the class slides)
# each node is a key and its value is list of neibghbours and their distance.
graph = {
    "Oradea": [["Zerind", 71], ["Sibiu", 151]],
    "Zerind": [["Oradea", 71], ["Arad", 75]],
    "Arad": [["Zerind", 75], ["Timisoara", 118], ["Sibiu", 140]],
    "Timisoara": [["Arad", 118], ["Lugoj", 111]],
    "Lugoj": [["Timisoara", 111], ["Mehadia", 70]],
    "Mehadia": [["Lugoj", 70], ["Drobeta", 75]],
    "Drobeta": [["Mehadia", 75], ["Craiova", 120]],
    "Craiova": [["Drobeta", 120], ["Rimnicu Vilcea", 146], ["Pitesti", 138]],
    "Rimnicu Vilcea": [["Craiova", 146], ["Sibiu", 80], ["Pitesti", 97]],
    "Sibiu": [["Oradea", 151], ["Arad", 140], ["Fagaras", 99], ["Rimnicu Vilcea", 80]],
    "Fagaras": [["Sibiu", 99], ["Bucharest", 211]],
    "Pitesti": [["Rimnicu Vilcea", 97], ["Craiova", 138], ["Bucharest", 101]],
    "Bucharest": [["Fagaras", 211], ["Pitesti", 101], ["Giurgiu", 90], ["Urziceni", 85]],
    "Giurgiu": [["Bucharest", 90]],
    "Urziceni": [["Bucharest", 85], ["Hirsova", 98], ["Vaslui", 142]],
    "Hirsova": [["Urziceni", 98], ["Eforie", 86]],
    "Eforie": [["Hirsova", 86]],
    "Vaslui": [["Urziceni", 142], ["Iasi", 92]],
    "Iasi": [["Vaslui", 92], ["Neamt", 87]],
    "Neamt": [["Iasi", 87]]
}


# distance table from every city to Bucharest
city_distances = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

def Astar(given_graph, distance_table, start_node, end_node, path_list=None):
    if path_list is None:
        path_list = [start_node]
    min_straight_dist = 100000          #just an upper limit 
    best_neighbour = None
    for i in given_graph[start_node]:
        distance_to_neighbour = i[1]
        total_cost = distance_to_neighbour + distance_table[i[0]]
        if total_cost < min_straight_dist:
            min_straight_dist = total_cost
            best_neighbour = i[0]
    if best_neighbour == end_node:
        path_list.append(end_node)
        return path_list
  
    path_list.append(best_neighbour)
    return Astar(given_graph, distance_table, best_neighbour, end_node, path_list)


y = Astar(graph, city_distances, "Arad", "Bucharest")
print(y)