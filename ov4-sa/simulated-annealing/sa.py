__author__ = 'paulpm / Paul Philip Mitchell'

import random
import math


def simulated_annealing(node, temp):
    current_node = node
    max_evaluated_ever = 0
    temperature = temp

    while True:
        evaluation_of_current = current_node.evaluate()

        if evaluation_of_current >= 1:
            return current_node

        neighbors = current_node.create_neighbors()
        max_evaluated = 0
        next_node = None

        # Sets the neighbor with highest evaluation as the next node
        for node in neighbors:
            temp = node.evaluate()
            if temp > max_evaluated:
                max_evaluated = temp
                next_node = node

        # To account for Zero Division errors
        if evaluation_of_current <= 0.0001:
            evaluation_of_current = 0.01

        # Simulated Annealing-specific functions for either exploring or exploiting
        #print("Evaluation: %s" % evaluation_of_current)
        q = ((max_evaluated - evaluation_of_current) / evaluation_of_current)
        p = min(0.9, math.exp((-q) / temperature))
        x = random.random()

        if max_evaluated_ever < max_evaluated:
            max_evaluated_ever = max_evaluated
        if max_evaluated_ever == 1:
            print(current_node)

        # If our random 0-1 variable x is bigger than p, we exploit
        if x > p:
            current_node = next_node
        # If not, we explore
        else:
            current_node = neighbors[random.randint(0, len(neighbors)-1)]

        if temperature <= 0:
            break
        temperature -= 0.1

    return current_node, current_node.evaluate(), max_evaluated_ever