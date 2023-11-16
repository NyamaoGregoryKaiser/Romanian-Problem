class node:
    def __init__(self, name):
        self.explored = 0
        self.name = name
        self.neighbours = {}

nodes = {}
start = 'Arad'
goal = 'Bucharest'
explored = []
frontier = []
path = []
f = open(r"C:\Users\cosym\OneDrive\Desktop\3.1\AI\input.txt", "r")
for line in f:
    line = line.strip()
    node1, node2, distance = line.split(",")
    if node1 not in nodes:
        nodes[node1] = node(node1)
    if node2 not in nodes:
        nodes[node2] = node(node2)
    nodes[node1].neighbours[node2] = distance
    nodes[node2].neighbours[node1] = distance

def initFrontier():
    frontier.append(start)
    nodes[start].parent = ''

def choosenode():
    node = frontier.pop()
    if testgoal(node):
        print(goal)
        pathcost = calpath(goal)
        print("path cost is {}".format(pathcost))
        print("path selected is {}".format(path))
        exit()
    return node

def calpath(cnode):
    path.append(cnode)
    if nodes[cnode].parent == '':
        return 0
    else:
        cparent = nodes[cnode].parent
        pathcost = calpath(cparent)+int(nodes[cnode].neighbours[cparent])
        return pathcost

def testgoal(curnode):
    if curnode == goal:
        return True
    return False

def graphsearch():
    if not frontier:
        print("failure")
        exit()
    curnode = choosenode()
    nodes[curnode].explored = 1
    explored.append(curnode)
    for neighbour in nodes[curnode].neighbours.keys():
        if neighbour in frontier:
            continue
        if neighbour in explored:
            continue
        frontier.append(neighbour)
        nodes[neighbour].parent = curnode

initFrontier()
while True:
    graphsearch()
    print(frontier)