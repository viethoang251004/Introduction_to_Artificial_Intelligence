from problem import Problem
from search import LocalSearchStrategy

def main():
    n = 800
    # Create an instance of the Problem class
    problem = Problem('monalisa.jpg')
    # Perform random restart hill climbing with n trials
    p = LocalSearchStrategy.random_restart_hill_climbing(problem, n)
    # Visualize the state space and the path found by random restart hill climbing
    print(p)
    problem.draw_path(p)
    # Perform local beam search with k = 5
    k = 100
    path = LocalSearchStrategy.local_beam_search(problem, k)
    # Visualize the state space and the path found by local beam search
    problem.draw_path(path)
    # path = LocalSearchStrategy.local_beam_search(problem, k=10)
    # # Print the path
    # print(path)


if __name__ == "__main__":
    main()