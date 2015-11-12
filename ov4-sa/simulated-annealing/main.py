__author__ = 'paulpm / Paul Philip Mitchell'

from simulated_annealing.node import Node
from simulated_annealing.sa import simulated_annealing


def main():
    size = 8
    k = 1

    node = Node({
        "columns": size,
        "rows": size,
        "k": k
    })
    node.set_start_node()

    result, score, max_evaluated_ever = simulated_annealing(node, 100)
    print("Result:\n%s" % result)
    print("Score: %s" % score)
    print("Max evaluation: %s" % max_evaluated_ever)

if __name__ == "__main__":
    main()