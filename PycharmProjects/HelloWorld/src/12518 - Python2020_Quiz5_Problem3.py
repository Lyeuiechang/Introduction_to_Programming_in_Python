class Polynomial:
    def __init__(self, *coeff):
        coeff = list(coeff)
        self.L = coeff

    def evaluate(self, xvalue):
        sum = 0
        for i in range(len(self.L)):
            sum += self.L[i] * pow(xvalue, i)
        return sum

    def change_coefficient(self, i, coeff):
        self.L[i] = coeff
        return self


# MUST add the 6 lines below
instantiate_statement = input()
exec(instantiate_statement)
change_coeff_call = input()
exec(change_coeff_call)
print_evaluate = input()
exec(print_evaluate)