import random

distance_matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

population_size = 10
mutation_rate = 0.1
generations = 100

def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]
    return total_distance

def fitness(tour):
    return 1 / calculate_distance(tour)

def create_population():
    population = []
    for _ in range(population_size):
        tour = list(range(len(distance_matrix)))
        random.shuffle(tour)
        population.append(tour)
    return population

def selection(population):
    selected = random.choices(population, weights=[fitness(t) for t in population], k=2)
    return selected[0], selected[1]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    ptr = end
    for gene in parent2:
        if gene not in child:
            if ptr >= size:
                ptr = 0
            child[ptr] = gene
            ptr += 1
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    population = create_population()
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = sorted(new_population, key=lambda t: calculate_distance(t))[:population_size]
    best_tour = min(population, key=lambda t: calculate_distance(t))
    return best_tour, calculate_distance(best_tour)

best_tour, best_distance = genetic_algorithm()
print("Best Tour:", best_tour)
print("Best Distance:", best_distance)
