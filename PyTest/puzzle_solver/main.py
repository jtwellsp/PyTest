from .utils import get_initial, display_path, goal_state
from .solver import bfs, a_star, check_puzzle

#Solves each puzzle using the user defined algorithm 
def solve_and_display(initial_state, algorithm_name, heuristic=None):
    #Prints the initial state of the puzzle
    print(f"Initial State:")
    for row in initial_state:
        print(row)

    #Prints the solution path of the puzzle using user selected function
    print(f"\n{algorithm_name} Solution Path:")
    if algorithm_name == "BFS":
        path = bfs(initial_state, goal_state)
        display_path(path)
        print(f"{algorithm_name} Path Found\n")
    else:
        path, cost = a_star(initial_state, goal_state, heuristic)
        display_path(path)
        print(f"{algorithm_name} Cost: {cost}\n")

'''
Runs the puzzle solver **IMPORTANT** this is the main function
To run the puzzle solver you will need to run the following function:

                python -m puzzle_solver.main

This will prompt the user to select which algorithm they would like to use to solve the puzzle.
Available options are BFS, A* or Both.
'''
def main():
    initial_states = get_initial(3)
    answer = input("Would you like to see BFS, A* or both? (BFS/A*/Both): ").lower()

    for i, initial_state in enumerate(initial_states):
        print(f"Initial State {i + 1}:")
        #Solve using the BFS algorithm
        if answer == "bfs":
            solve_and_display(initial_state, "BFS")
        #Solve using the A* algorithm
        elif answer == "a*":
            solve_and_display(initial_state, "A*", heuristic=check_puzzle)
        #Solve using both algorithms
        elif answer == "both":
            solve_and_display(initial_state, "BFS")
            solve_and_display(initial_state, "A*", heuristic=check_puzzle)

#Runs the main function
if __name__ == "__main__":
    main()