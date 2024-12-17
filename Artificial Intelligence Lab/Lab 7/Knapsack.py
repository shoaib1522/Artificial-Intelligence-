import random

items = [
    {'weight': 2, 'value': 3},
    {'weight': 3, 'value': 4},
    {'weight': 4, 'value': 8},
    {'weight': 5, 'value': 8},
    {'weight': 9, 'value': 10}
]

knapsack_capacity = 10
population_size = 10
mutation_rate = 0.1
generations = 100

def fitness_knapsack(chromosome):
    total_weight = total_value = 0
    for i, gene in enumerate(chromosome):
        if gene == 1:
            total_weight += items[i]['weight']
            total_value += items[i]['value']
    if total_weight > knapsack_capacity:
        return 0
    else:
        return total_value

def create_population_knapsack():
    return [[random.choice([0, 1]) for _ in range(len(items))] for _ in range(population_size)]

def selection_knapsack(population):
    fitness_values = [fitness_knapsack(ch) for ch in population]
    total_fitness = sum(fitness_values)
    if total_fitness == 0:
        return random.choice(population), random.choice(population)
    selection_probs = [f / total_fitness for f in fitness_values]
    return random.choices(population, weights=selection_probs, k=2)

def crossover_knapsack(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate_knapsack(chromosome):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

def genetic_algorithm_knapsack():
    population = create_population_knapsack()
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection_knapsack(population)
            child1, child2 = crossover_knapsack(parent1, parent2)
            mutate_knapsack(child1)
            mutate_knapsack(child2)
            new_population.extend([child1, child2])
        population = sorted(new_population, key=lambda ch: fitness_knapsack(ch), reverse=True)[:population_size]
    best_solution = max(population, key=lambda ch: fitness_knapsack(ch))
    best_value = fitness_knapsack(best_solution)
    return best_solution, best_value

best_solution, best_value = genetic_algorithm_knapsack()
print("Best Solution:", best_solution)
print("Best Value:", best_value)
