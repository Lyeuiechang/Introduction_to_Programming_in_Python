import operator as op  # You may use this module if you want


class Polynomial:
    # You may modify the following 3 methods if you want
    def __init__(self, *coeff):
        self._coeff = list(coeff)

    def __repr__(self):
        return self.__class__.__name__ + f"({', '.join(map(str, self._coeff))})"

    def evaluate(self, xvalue):
        return sum([a * xvalue ** i for i, a in enumerate(self._coeff)])

    __call__ = evaluate

    def __add__(self, RHS):
        if


    #def __sub__(self, RHS):

    # Your code here to return a new Polynomial by subtracting two Polynomial

    #def __imul__(self, scalar):


# Your code here to scale the coeff and return the original Polynomial

# For judging purpose
instantiate_f = input()
exec(instantiate_f)
instantiate_g = input()
exec(instantiate_g)
print_f_add_g = input()
exec(print_f_add_g)
print_g_sub_f = input()
exec(print_g_sub_f)
f_scale = input()
exec(f_scale)
print_f = input()
exec(print_f)
print_f_eval = input()
exec(print_f_eval)