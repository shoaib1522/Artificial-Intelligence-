import random

def initialize_population(pop_size, string_length):
    population = []
    for _ in range(pop_size):
        individual = ""
        for _ in range(string_length):
            individual += random.choice("01")
        population.append(individual)
    return population

def calculate_fitness(individual):
    fitness = 0
    for bit in individual:
        if bit == '1':
            fitness += 1
    return fitness

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    parent1 = None
    parent2 = None

    for i in range(len(population)):
        if random.uniform(0, total_fitness) <= fitness_scores[i]:
            parent1 = population[i]
            break

    for i in range(len(population)):
        if random.uniform(0, total_fitness) <= fitness_scores[i]:
            parent2 = population[i]
            break

    if parent1 is None or parent2 is None:
        parent1, parent2 = random.sample(population, 2)

    return parent1, parent2

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    offspring = parent1[:point] + parent2[point:]
    return offspring

def mutate(individual, mutation_rate):
    mutated = ""
    for bit in individual:
        if random.random() < mutation_rate:
            mutated += '1' if bit == '0' else '0'
        else:
            mutated += bit
    return mutated

def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    for generation in range(num_generations):
        fitness_scores = []
        for individual in population:
            fitness = calculate_fitness(individual)
            fitness_scores.append(fitness)

        new_population = []
        for _ in range(pop_size):
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, mutation_rate)
            new_population.append(offspring)

        population = new_population

    best_individual = max(population, key=calculate_fitness)
    return best_individual

def main():
    string_lengths = [10, 20, 50]
    pop_sizes = [20, 50, 100]
    mutation_rates = [0.01, 0.05, 0.1]
    num_generations = 50

    for string_length in string_lengths:
        for pop_size in pop_sizes:
            for mutation_rate in mutation_rates:
                print(f"Testing with String Length: {string_length}, Population Size: {pop_size}, Mutation Rate: {mutation_rate}")
                best_solution = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
                print("Best Solution:", best_solution)
                print("Number of Ones:", calculate_fitness(best_solution))
                print("-" * 50)

if __name__ == "__main__":
    main()
