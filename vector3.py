"""
The Vector class lets us do common operations such as
addition, scalar multiplications and dot products.

>>> v1 = Vector([4, 2, 7])
>>> v2 = Vector([1, -1, 3])
>>> v1 + v2
Vector([5, 1, 10])
>>> v1 + [-1, -1, 3]
Vector([3, 1, 10])
>>> [-1, -1, 3] + v1
Vector([3, 1, 10])
>>> v1 + range(3)
Vector([4, 3, 9])
>>> v1 + range(2)
Vector([4, 3, 7])
>>> range(2) + v1
Vector([4, 3, 7])
>>> λ = 3
>>> v1*λ
Vector([12, 6, 21])
>>> λ*v1
Vector([12, 6, 21])
>>> v1@v2
23
>>> v2@v1
23
>>> v1 @ [-1, -1, 3]
15
>>> [-1, -1, 3]@v1
15
"""

import reprlib
class Vector:
    
    def __init__(self, lst):
        """
        Create a Vector from a sequence.
        The memory is not copied.
        """
        self._storage = lst

    def __len__(self):
        """
        Delegate length to length of storage.
        >>> v = Vector(range(10))
        >>> len(v)
        10
        """
        return len(self._storage)
    
    def __getitem__(self, i):
        "delegate getting an index to the underlying list"
        return self._storage[i]

    def __add__(self, other_vector):
        """
        Currently truncates to the smaller of the vector
        and added sequence. FIXME.
        """
        try:
            sumlist = []
            for i, _ in enumerate(other_vector):
                sumlist.append(self._storage[i] + other_vector[i])
            return Vector(sumlist)
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other_vector):
        "add a sequence to a vector by reversing"
        # turn other + self around
        return self + other_vector
    
    def __mul__(self, scalar):
        "Multiply Vector by a scalar"
        return Vector([item*scalar for item in self._storage])

    def __rmul__(self, scalar):
        "multiply scalar by a vector"
        return self*scalar

    def __repr__(self):
        components = reprlib.repr(self._storage)
        return f"Vector({components})"



if __name__ == "__main__":
    import doctest
    doctest.testmod()