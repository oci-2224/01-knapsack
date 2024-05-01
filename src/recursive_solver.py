# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class RecursiveKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> solver = RecursiveKnapsackSolver(kp)
    >>> solver.optimal_solution()
    9700

    """
    
    def __init__(self, instance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)
        
    def _knapsack(self, weights=None, values=None, capacity=None) -> int:
        weights = self._inst.W if weights is None else weights
        values = self._inst.V if values is None else values
        capacity = self._inst.C if capacity is None else capacity
        
        if len(values) == 0:
            return 0
        
        # résoudre sans l'objet (on considère la solution où )
        value_without = self._knapsack(weights[1:], values[1:], capacity)
        
        if capacity >= weights[0]:
            # résoudre avec l'objet
            value = self._knapsack(weights[1:], values[1:], capacity - weights[0])
            value_with = value + values[0]
        else:
            value_with = -1
        
        # return meilleure solution
        return max(value_without, value_with)
            
    def optimal_solution(self) -> int:
        return self._knapsack()
    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force
        
        
                    
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
    
