# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

import itertools
from knapsack import KnapsackInstance, KnapsackSolver


class BruteforceKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """

    def __init__(self, instance) -> None:
        super().__init__(instance)

    def all_solutions_1(self):
        """
        >>> kp = KnapsackInstance(W=[10, 24, 11], V=[500, 4500, 960], C=50)
        >>> bfs = BruteforceKnapsackSolver(kp)
        >>> list(bfs.all_solutions_1())[:]
        [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
        """
        n = self._inst.size
        return itertools.product([0, 1], repeat=n)

    def all_solutions_2(self):
        """
        >>> kp = KnapsackInstance(W=[10, 24, 11], V=[500, 4500, 960], C=50)
        >>> bfs = BruteforceKnapsackSolver(kp)
        >>> list(bfs.all_solutions_2())[:]
        [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
        """
        n = 0
        n_max = 2**self._inst.size
        while n < n_max:
            bits = bin(n)[2:]
            bits = (self._inst.size - len(bits)) * "0" + bits
            yield tuple(map(int, list(bits)))
            n += 1

    def solve(self) -> tuple[int, ...]:
        """
        Returns one of the optimal feasible solutions
        """
        all_solutions = self.all_solutions_1()

        v_max_index = 0
        v_max = 0
        opt_sol: tuple[int, ...] = (0,)
        for i, sol in enumerate(all_solutions):
            if self.weight(sol) <= self._inst.C:
                value = self.value(sol)
                if value > v_max:
                    v_max = value
                    v_max_index = i
                    opt_sol = sol

        return opt_sol


try:
    import doctest

    doctest.testmod()
except:
    print("Unable to load doctests")
