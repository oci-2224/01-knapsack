# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

import itertools
from knapsack import KnapsackInstance, KnapsackSolver


class GreedyKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> gs = GreedyKnapsackSolver(kp)
    >>> X_sub_optimal = gs.solve()
    >>> X_sub_optimal
    (1, 1, 1, 0, 0, 0)
    >>> gs.value(X_sub_optimal)
    7800
    >>> gs.weight(X_sub_optimal)
    39
    >>> gs.weight(X_sub_optimal) <= gs._inst.C
    True

    """

    def __init__(self, instance) -> None:
        super().__init__(instance)

    def solve(self) -> tuple[int, ...]:
        """
        Returns one of the optimal feasible solutions
        """
        objects_as_tuples = list(zip(self._inst.V, self._inst.W))
        heuristic_values = list(enumerate([v / w for v, w in objects_as_tuples]))

        # solution with no object at all
        solution = [0 for _ in range(self._inst.size)]
        
        heuristic_values.sort(key=lambda x: x[1], reverse=True)
        
        remaining_capacity = self._inst.C
        
        for i, h in heuristic_values:
            if remaining_capacity - self._inst.W[i] >= 0:
                solution[i] = 1
                remaining_capacity -= self._inst.W[i]
            else:
                break
       
        return tuple(solution)


try:
    import doctest

    doctest.testmod()
except:
    print("Unable to load doctests")
