import compound
import random
import prediction

mutation_rate = 0.3
indv2 = prediction.Viability_prediction()
#individual1 = [6.0, 10.0, 7.0, 0.23404255319148934, 0.2, 0.021006350757205666, 0.5427514148889857, 0.50300869684053]

def to_mutation(individual1):

    mutate_individual = []
    range_for_individual2 = len(indv2)
    for i in range(individual1.__len__()):
        individual2 = indv2.iloc[0].values.tolist()
        if random.random() >= mutation_rate:
            mutate_individual.append(individual1[i])
        else:
            #individual = compound.transformed_input()
            mutate_individual.append(individual2[i])
    return mutate_individual

#print(to_mutation(individual1))