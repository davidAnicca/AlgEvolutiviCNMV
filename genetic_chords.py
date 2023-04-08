import random
from play import play_chord

pop = []


def gen_chords(population=500, generations=100, mutation_rate=0.2):
    global pop
    global fitness
    gen_first_population(population)
    play_chord(pop[0])
    play_chord(pop[1])
    play_chord(pop[2])

    gen = 0
    while gen < generations:
        gen += 1
        elites = roulette_selection(0.8 * population)
        print("generatia: ", gen)
        # pregătim următoarea populatie
        children = 0
        while children < population:
            mom = random.choice(elites)
            dad = random.choice(elites)
            child1, child2 = crossover(mom, dad)

            # aplicăm mutații

            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)

            pop.append(child1)
            pop.append(child2)

            children += 2

        pop = sorted(pop, key=lambda individual: fitness(individual), reverse=True)
        pop = pop[:population]

    return pop[0]


def gen_first_population(population):
    for _ in range(population):
        individual = [
            random.uniform(110, 880),
            random.uniform(110, 880),
            random.uniform(110, 880),
            random.uniform(110, 880),
        ]
        pop.append(individual)


def roulette_selection(elite_size):
    fitness_sum = sum([fitness(individual) for individual in pop])
    elite = []
    while len(elite) < elite_size:
        r = random.uniform(0, fitness_sum)
        acc_fitness = 0
        for individual in pop:
            acc_fitness += fitness(individual)
            if acc_fitness > r:
                elite.append(individual)
                break
    return elite


def crossover(mom, dad):
    crossover_point = random.randint(0, len(mom) - 1)
    child1 = mom[:crossover_point] + dad[crossover_point:]
    child2 = mom[crossover_point:] + dad[:crossover_point]
    return child1, child2


def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.uniform(110, 880)
    return individual


def f1(individual):
    score = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            ratio = max(individual[i], individual[j]) / min(individual[i], individual[j])
            score += sc(ratio, abs(individual[i] - individual[j]))

    return score


def almost_equal(x, y):
    return abs(x - y) < 0.001


def sc(ratio, dif):
    score = 0
    if almost_equal(ratio, 2):
        score += 500
    elif almost_equal(ratio, 3 / 2):
        score += 300
    elif almost_equal(ratio, 4 / 3):
        score += 100
    elif almost_equal(ratio, 6 / 5):
        score += 200
    elif almost_equal(ratio, 1):
        score -= 300
    elif ratio > 5:
        score -= 1000
    elif dif < 20:
        score -= 2000
    return score


fitness = f1
