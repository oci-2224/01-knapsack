# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

import itertools
from knapsack import KnapsackInstance, KnapsackSolver


class RecursiveSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> solver = RecursiveSolver(kp)
    >>> solver.optimal_value()
    9700

    """

    def __init__(self, instance) -> None:
        super().__init__(instance)
        # memoization table
        self._memo: dict[tuple[int, int], int] = {}

    def _knapsack_1(self, values=None, weights=None, capacity=None) -> int:
        values = self._inst.V if values is None else values
        weights = self._inst.W if weights is None else weights
        capacity = self._inst.C if capacity is None else capacity

        if len(values) == 0:
            return 0

        profit_without = self._knapsack_1(values[1:], weights[1:], capacity)
        if weights[0] <= capacity:
            remaining = capacity - weights[0]
            profit_with = (
                self._knapsack_1(values[1:], weights[1:], remaining) + values[0]
            )
        else:
            profit_with = -1

        return max(profit_with, profit_without)

    def _knapsack_2(self, k: int = 0, capacity: int = -1) -> int:
        # print(f"{k * '  '}f(k={k}, capacity={capacity}, solution={solution}")
        if k >= self._inst.size:
            return 0

        capacity = self._inst.C if capacity == -1 else capacity

        profit_without = self._knapsack_2(k + 1, capacity)
        remaining = capacity - self._inst.W[k]

        if remaining < 0:
            profit_with = -1
        else:
            profit_with = self._knapsack_2(k + 1, remaining) + self._inst.V[k]

        return max(profit_with, profit_without)
    
    
    def _knapsack_2_memo(self, k: int = 0, capacity: int = -1) -> int:
        if (k, capacity) in self._memo:
            return self._memo[(k, capacity)]
        else:
            # print(f"{k * '  '}f(k={k}, capacity={capacity}, solution={solution}")
            if k >= self._inst.size:
                return 0

            capacity = self._inst.C if capacity == -1 else capacity

            profit_without = self._knapsack_2(k + 1, capacity)
            remaining = capacity - self._inst.W[k]

            if remaining < 0:
                profit_with = -1
            else:
                profit_with = self._knapsack_2(k + 1, remaining) + self._inst.V[k]

            opt_value = max(profit_with, profit_without)
            self._memo[(k, capacity)] = opt_value
            return opt_value
    
    

    def optimal_value(self) -> int:
        return self._knapsack_2_memo()

    def solve(self) -> tuple[int, ...]:
        """
        Returns one of the optimal feasible solutions
        """

        raise NotImplementedError

def test():
    kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    solver = RecursiveSolver(kp)
    opt = solver.optimal_value()
    print("optimal value", opt)
    

if True:
    try:
        import doctest

        doctest.testmod()
    except:
        print("Unable to load doctests")
else:
    test()