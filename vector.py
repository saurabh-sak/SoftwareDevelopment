import reprlib
class Vector:
    
    def __init__(self, lst):
        self._storage = lst
        
    def __len__(self):
        return len(self._storage)
    
    def __getitem__(self, i):
        return self._storage[i]

    def __add__(self, other_vector):
        try:
            sumlist = []
            for i, _ in enumerate(other_vector):
                sumlist.append(self._storage[i] + other_vector[i])
            return Vector(sumlist)
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other_vector):
        # turn other + self around
        return self + other_vector
    
    def __mul__(self, scalar):
        return Vector([item*scalar for item in self._storage])

    def __rmul__(self, scalar):
        return self*scalar

    def __repr__(self):
        components = reprlib.repr(self._storage)
        return f"Vector({components})"