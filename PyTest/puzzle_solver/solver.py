from heapq import heappush, heappop
from collections import deque
from .utils import goal_state, get_numbers, check_puzzle, fix_path
'''
Breadth-First Search (BFS) is an algorithm that traverses a graph in a breadthward motion and uses a queue to keep track of the nodes to visit next.

For my implementation of BFS, I used both a queue and a set to keep track of the visited states. 
The queue is initialized with the initial state, and the visited set is initialized with the initial state as well. 
The came_from dictionary is used to keep track of the path taken to reach a state.

I orginally started with a path cost but soon realized that the assignment did not require it for BFS
'''
def bfs(initial_state, goal_state):
    #Initializes the queue with the initial state 
    queue = deque([initial_state])
    #Keeps track of the vissited states 
    visited = {tuple(map(tuple, initial_state))}
    #Keeps track of the path taken to reach a state
    came_from = {tuple(map(tuple, initial_state)): None}

    #orginal path cost implementation later used in A*
    #path_cost = {tuple(map(tuple, initial_state)): 0}

    while queue:
        #uses a queue to keep track of the nodes to visit next
        state = queue.popleft()

        #check if the goal state is reached each iteration
        if state == goal_state:
            return fix_path(came_from, state)

        #iterates through the possible states
        for numbers in get_numbers(state):
            numbers_tuple = tuple(map(tuple, numbers))
            #tentative_cost = current_cost + 1


            #checks if the state has been visited
            if numbers_tuple not in visited:
                visited.add(numbers_tuple)
                came_from[numbers_tuple] = state
                #path_cost[numbers_tuple] = tentative_cost
                queue.append(numbers)

    return None
'''
A* is a search algorithm that uses a heuristic to estimate the cost of the cheapest path from the initial state to the goal state.

For my implementation of A*, I used a priority queue to keep track of the states to visit next. 
I feel like this might be wrong because during testing this implementation, I was getting very simliar results to BFS, which is not what I expected.
I decided after testing to use tuples to keep track of the states and the path taken to reach a state.

Path cost is added to this one.
'''
def a_star(initial_state, goal_state, heuristic):
    #Very similiar to the BFS implementation
    queue = [(0, 0, initial_state)]
    visited = {tuple(map(tuple, initial_state))}
    came_from = {tuple(map(tuple, initial_state)): None}
    #Keeps track of the path cost
    path_cost = {tuple(map(tuple, initial_state)): 0}

    while queue:
        _, current_cost, state = heappop(queue)

        if state == goal_state:
            return fix_path(came_from, state), current_cost

        #get all possible next states as well as the cost
        for numbers in get_numbers(state):
            numbers_tuple = tuple(map(tuple, numbers))
            tentative_cost = current_cost + 1

            #If the state has not been visited or if their is a cheaper path found, add it to the queue and update the path cost
            if numbers_tuple not in visited or tentative_cost < path_cost.get(numbers_tuple, float('inf')):
                visited.add(numbers_tuple)
                came_from[numbers_tuple] = state
                path_cost[numbers_tuple] = tentative_cost
                final_cost = tentative_cost + heuristic(numbers)
                heappush(queue, (final_cost, tentative_cost, numbers))

    return None, 0