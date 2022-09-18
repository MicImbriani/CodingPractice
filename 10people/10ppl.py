def get_children(r1, c1, symbol):
    children = []

    if r1 != 0:
        if Map[r1-1][c1] == symbol: children.append((r1-1, c1))
    if r1 != len(Map)-1:
        if Map[r1+1][c1] == symbol: children.append((r1+1, c1))
    if c1 != 0:
        if Map[r1][c1-1] == symbol: children.append((r1, c1-1))
    if c1 != len(Map[r1])-1:
        if Map[r1][c1+1] == symbol: children.append((r1, c1+1))
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



Map = []
r, c = map(int, input().split())
for x in range(r):
    Map.append(list(input()))
num = int(input())
for x in range(num):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    symbol = Map[r1][c1]
    goal = (r2, c2)
    result = search(r1, c1, symbol, goal)
    if result is True:
        print("binary") if symbol == 0 else print("decimal")
    else:
        print("neither")
