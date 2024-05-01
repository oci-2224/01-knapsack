# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

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
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)

    def _all_solutions(self, n: int) -> list[tuple[int, ...]]:
        solutions = [None] * 2 ** n
        for i in range(0, 2 ** n):
            bits: str = bin(i)[2:]
            k = n - len(bits)
            bits = k * '0' + bits
            solutions[i] = tuple([int(b) for b in bits])

        return solutions
    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force
        
        n = self._inst.size
        
        # générer toutes les solutions
        solutions: list[tuple[int, ...]] = self._all_solutions(n)
        
        # éliminer toutes les solutions non faisables
        # solutions = [sol for sol in solutions if self.weight(sol) <= self._inst.C]
        
        best_solution = (0,)
        best_value = 0
        # trouver la meilleure solution
        for solution in solutions:
            if self.weight(solution) <= self._inst.C:
                value = self.value(solution)
                if value > best_value:
                    best_solution = solution
                    best_value = value
                    
        return best_solution
        
try:
    import doctest

    doctest.testmod()
except:
    print("Unable to load doctests")

def test():
    kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    bfs = BruteforceKnapsackSolver(kp)
    Xopt = bfs.solve()
    
    print("solution", Xopt)
    
