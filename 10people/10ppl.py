def get_children(r1, c1, symbol):
    children = []

    if r1 != 0:
        if map[r1-1][c1] == symbol: children.append((r1-1, c1))
    if r1 != len(map)-1:
        if map[r1+1][c1] == symbol: children.append((r1+1, c1))
    if c1 != 0:
        if map[r1][c1-1] == symbol: children.append((r1, c1-1))
    if c1 != len(map[r1])-1:
        if map[r1][c1+1] == symbol: children.append((r1, c1+1))
    return children


def search(r1, c1, symbol, goal):
    queue = []
    expanded = []
    
    root = (r1, c1)
    queue.append(root)

    while True:
        # Stop condition: no more nodes to search
        if len(queue) == 0:
            return False
        
        # Else, get the next node in line from the queue
        current_node = queue.pop(0)

        
        # Add the current node to the expanded list
        expanded.append(current_node)

        # Expand children nodes and add to the queue
        children = get_children(current_node[0], current_node[1], symbol)
        for child in children:
            if not (child in expanded or child in queue):
                queue.append(child)
        
        # Check for goal in nodes
        if goal in queue or goal in expanded:
            return True


# ##############################


file = open("sample-01.in", 'r')

lines = file.readlines()
lines = [x.strip("\n") for x in lines]

linesNum = [int(x) for x in lines[0].split(" ")]
charNum, linesNum = linesNum[1], linesNum[0]
map = [x for x in lines[1:linesNum+1]]
testsNum = lines[linesNum+1]
tests = [x.split(" ") for x in lines[linesNum+2:]]

for test in tests:
    r1, c1, r2, c2 = [int(x)-1 for x in test]
    symbol = map[r1][c1]
    goal = (r2, c2)
    result = search(r1, c1, symbol, goal)
    if result is True:
        print("binary") if symbol == 0 else print("decimal")
    else:
        print("neither")