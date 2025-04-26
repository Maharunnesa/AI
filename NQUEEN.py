import random
import numpy as np

def generate_individual(n):
    """Generate a random permutation of board positions."""
    return np.random.permutation(n).tolist()

def calculate_fitness(individual):
    """Calculate fitness based on number of non-attacking queen pairs."""
    n = len(individual)
    conflicts = 0
    
    # Check for conflicts in rows (already avoided by permutation)
    # Check for diagonal conflicts
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens are on the same diagonal
            if abs(i - j) == abs(individual[i] - individual[j]):
                conflicts += 1
    
    # Maximum possible conflicts = n choose 2
    max_conflicts = (n * (n - 1)) // 2
    # Higher fitness is better, so invert conflicts
    return max_conflicts - conflicts

def select_parents(population, fitnesses, num_parents):
    """Select parents using tournament selection."""
    selected = []
    tournament_size = 3
    
    for _ in range(num_parents):
        tournament_indices = random.sample(range(len(population)), tournament_size)
        tournament_fitnesses = [fitnesses[i] for i in tournament_indices]
        winner_idx = tournament_indices[np.argmax(tournament_fitnesses)]
        selected.append(population[winner_idx])
    
    return selected

def crossover(parent1, parent2):
    """Perform ordered crossover (OX) to maintain permutation."""
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    
    # Get slice from parent1
    child = [-1] * n
    child[start:end] = parent1[start:end]
    
    # Fill remaining positions from parent2
    parent2_idx = 0
    child_idx = 0
    while child_idx < n:
        if child_idx == start:
            child_idx = end
            continue
        if parent2[parent2_idx] not in child:
            child[child_idx] = parent2[parent2_idx]
            child_idx += 1
        parent2_idx += 1
    
    return child

def mutate(individual, mutation_rate=0.1):
    """Swap two positions with given mutation rate."""
    if random.random() < mutation_rate:
        n = len(individual)
        i, j = random.sample(range(n), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm(n, population_size=100, max_generations=1000):
    """Solve N-Queens problem using genetic algorithm."""
    # Initialize population
    population = [generate_individual(n) for _ in range(population_size)]
    best_fitness = 0
    best_solution = None
    max_fitness = (n * (n - 1)) // 2  # Maximum possible non-attacking pairs
    
    for generation in range(max_generations):
        # Calculate fitness for each individual
        fitnesses = [calculate_fitness(ind) for ind in population]
        
        # Check if solution found
        max_fitness_gen = max(fitnesses)
        if max_fitness_gen > best_fitness:
            best_fitness = max_fitness_gen
            best_solution = population[np.argmax(fitnesses)]
            
            # If perfect solution found, return it
            if best_fitness == max_fitness:
                return best_solution, best_fitness
        
        # Create new population
        new_population = []
        
        # Elitism: keep best individual
        new_population.append(best_solution)
        
        # Generate rest of population
        while len(new_population) < population_size:
            # Select parents
            parents = select_parents(population, fitnesses, 2)
            
            # Perform crossover
            child = crossover(parents[0], parents[1])
            
            # Perform mutation
            child = mutate(child)
            
            new_population.append(child)
        
        population = new_population
    
    return best_solution, best_fitness

def print_board(solution):
    """Print the chessboard with queens."""
    n = len(solution)
    for i in range(n):
        row = ['.'] * n
        row[solution[i]] = 'Q'
        print(' '.join(row))

# Example usage
if __name__ == "__main__":
    n = 8  # 8-Queens problem
    solution, fitness = genetic_algorithm(n)
    
    print(f"Best solution found with fitness {fitness}:")
    print_board(solution)
    print(f"Position array: {solution}")