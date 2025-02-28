import random
import math

class LocalSearchStrategy:
    @staticmethod
    def random_restart_hill_climbing(problem, num_trials):
        best_path = None
        best_evaluation = float('-inf')
        
        for _ in range(num_trials):
            current_state = problem.get_random_state()
            current_value = problem.evaluate_state(current_state)
            path = [current_state]
            
            while True:
                neighbor = problem.get_highest_valued_successor(current_state)
                neighbor_value = problem.evaluate_state(neighbor)
                
                if neighbor_value <= current_value:
                    break
                
                current_state = neighbor
                current_value = neighbor_value
                path.append(current_state)
                
            
            if current_value > best_evaluation:
                best_evaluation = current_value
                best_path = path
        
        # Tạo danh sách mới để lưu trữ các bộ ba (x, y, z)
        xyz_list = []
        
        # Lặp qua best_path để trích xuất các bộ ba (x, y, z) và thêm vào danh sách
        for state in best_path:
            x, y = state
            xyz_list.append((x, y, problem.Z[y, x]))
        
        return xyz_list



    #Task 3:
    def simulated_annealing_search(problem, schedule):
        current_state = problem.get_initial_state()
        path = [current_state]
        
        t = 1
        while True:
            T = schedule(t)  
            if T <= 0:
                break
            
            neighbors = problem.get_successors(current_state)
            if not neighbors:
                break
            
            next_state = random.choice(neighbors)
            delta_e = problem.evaluate_state(next_state) - problem.evaluate_state(current_state)
            
            if delta_e > 0 or random.random() < math.exp(delta_e / T):
                current_state = next_state
                path.append(current_state)
            
            t += 1
        
        # Chuyển đổi đường đi thành danh sách các tuple (x, y, z)
        xyz_list = []
        for state in path:
            x, y = state
            xyz_list.append((x, y, problem.Z[y, x]))
        
        return xyz_list
    
    # Task 4:
    def local_beam_search(problem, k):
        # Generate k random initial states
        current_states = [problem.get_random_state() for _ in range(k)]
        
        while True:
            next_states = []
            
            for state in current_states:
                # Get all successors for each current state
                successors = problem.get_neighbors(state)
                next_states.extend(successors)
            
            # Randomly select k best states from the successors
            current_states = random.sample(next_states, k)
            
            # Check if any of the current states is an edge state
            edge_state = next((state for state in current_states if problem.is_edge_state(state)), None)
            if edge_state is not None:
                # Return the path to the edge state
                path = [edge_state]
                while edge_state != problem.get_initial_state():
                    edge_state = problem.get_highest_valued_successor(edge_state)
                    path.append(edge_state)
                path.reverse()
                return path