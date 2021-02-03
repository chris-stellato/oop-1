class Polynomial():
    def __init__(self, coeff_lst):
        self.coeff_lst = coeff_lst

    def __repr__(self):
        return f"Polynomial({self.coeff_lst})"

    def __add__(self, sec_pol):
        return_lst = []
        for i, coeff in enumerate(self.coeff_lst):
            return_lst.append(self.coeff_lst[i] + sec_pol.coeff_lst[i])

        return return_lst

    def __sub__(self, sec_pol):
        return_lst = []
        for i, coeff in enumerate(self.coeff_lst):
            return_lst.append(self.coeff_lst[i] - sec_pol.coeff_lst[i])

        return return_lst

#   How is this line colloquially invoked?
    def __neg__(self):
        return_lst = []
        for i, coeff in enumerate(self.coeff_lst):
            return_lst.append(self.coeff_lst[i] * -1)

        return return_lst

    def evaluate(self, x):
        total = 0
        for deg, coeff in enumerate(self.coeff_lst):
            total += coeff*x**deg
        return total



    def __eq__(self, sec_poll):

        work_poly1 = self.coeff_lst
        work_poly2 = sec_poll.coeff_lst

        while work_poly1[-1] == 0:
            work_poly1.pop()


        while work_poly2[-1] == 0:
            work_poly2.pop()

        return work_poly1 == work_poly2


    def __str__(self):

        list_of_strings = []

        for i, val in enumerate(self.coeff_lst):
            if i == 0:
                if val > 0:
                    list_of_strings.append(f'+ {val}')
                elif val < 0:
                    list_of_strings.append(f'- {-val}')
            elif i == 1:
                if val > 0:
                    list_of_strings.append(f'+ {val}x')
                if val < 0:
                    list_of_strings.append(f'- {-val}x')
            else:
                if val > 0:
                    list_of_strings.append(f'+ {val}x^{i}')
                elif val < 0:
                    list_of_strings.append(f'- {-val}x^{i}')

        list_of_strings.reverse()

        print (list_of_strings[0])
        list_of_strings[0] = list_of_strings[0].replace("- ", "-")

        return ' '.join(list_of_strings)
        
    def __mul__(self, sec_pol):
        mul_lst = []
        for coeff in self.coeff_lst:
            for sec_coeff in sec_pol.coeff_lst:
                mul_lst.append(coeff*sec_coeff)
        return mul_lst

print(Polynomial([3,2,1]) * Polynomial([4,2]))
