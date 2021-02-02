from abc import ABCMeta, ABC

class polynomial(ABC):
    def __init__(self, degree_lst):
        self.degree_lst = degree_lst

    def __repr__(self):
        return f"Polynomial({self.degree_lst}"

