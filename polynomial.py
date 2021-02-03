class Polynomial():
    def __init__(self, coeff_lst):
        self.coeff_lst = coeff_lst

    def __repr__(self):
        return f"Polynomial({self.coeff_lst})"

    def __add__(self, sec_pol):
        for deg, coeff in enumerate(self.coeff_lst):
            self.coeff_lst[deg]+=sec_pol.coeff_lst[deg]

    def __sub__(self, sec_pol):
        for deg, coeff in enumerate(self.coeff_lst):
            self.coeff_lst[deg]-=sec_pol.coeff_lst[deg]

#   How is this line colloquially invoked?
    def __neg__(self):
        for deg, coeff in enumerate(self.coeff_lst):
            self.coeff_lst[deg] *= -1

    def evaluate(self, x):
        total = 0
        for deg, coeff in enumerate(self.coeff_lst):
            total += coeff*x**deg
        return total

test = Polynomial([3,2,1])
print(test)
test + Polynomial([3,2,1])
print(test)
test - Polynomial([3,2,1])
print(test)
test.__neg__()
print(test)