import random

#define the goal state for the puzzle 
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#finds the possible states the zero tile can move to
def get_numbers(state):
    #find the position of the zero tile
    row, col = next((i, row.index(0)) for i, row in enumerate(state) if 0 in row)
    #define the possible directions the zero tile can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    zero = []
    #iteration through the possible directions and how the zero tile can move
    for x, y in directions:
        rowx, coly = row + x, col + y
        if 0 <= rowx < 3 and 0 <= coly < 3:
            new_state = [list(row) for row in state]
            new_state[row][col], new_state[rowx][coly] = new_state[rowx][coly], new_state[row][col]
            zero.append(new_state)
    return zero

#Estimates the cost from current state to goal state
def check_puzzle(state):
    return sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3) if state[i][j] != 0)

#checks if the puzzle is solvable
def if_possible(state):
    #flattens and removes the zero tile from the state
    flat_state = [tile for row in state for tile in row if tile != 0]
    #counts the number of inversions in the state
    inversions = sum(1 for i in range(len(flat_state)) for j in range(i + 1, len(flat_state)) if flat_state[i] > flat_state[j])
    #solvablity check if number of inversions is even 
    return inversions % 2 == 0

#generates a list of solvable states
def get_initial(n):
    initial_states = []
    while len(initial_states) < n:
        #random puzzle generator
        state = random.sample(range(9), 9)
        state = [state[:3], state[3:6], state[6:]]
        #checks if the state is solvable, if not it will send it back 
        if if_possible(state):
            initial_states.append(state)
    return initial_states

#reconstructs the path from the initial state to the goal state
def fix_path(came_from, current):
    path = []
    while current:
        path.append(current)
        if current:
            #move the parent state to the current state
            current = came_from.get(tuple(map(tuple, current)))
        else:
            break
    return path[::-1]

#iterates through to show the path it took to reach the solution
def display_path(path):
    count = 0
    for step in path:
        #shows each step taken to reach the goal state
        print("Step " + str(count) + ":")
        count = count + 1
        for row in step:
            print(row)
        print()