import random
import copy
random.seed(0) # You must initiate the random seed to 0 for judging purpose.

class Matrix:
    def __init__(self, data):
        # data is the list of lists of value
        self.data = data

    def row(self, r):
        # return the r-th row in the form of a list
        # r is from 0.. number of rows
        # in the exmaple above, M.row(1) would return
        # [4, 5, 6]
        return self.data[r]

    def column(self, c):
        # return a the c-th column in the form of a list.
        # in the example above, M.column(2) would return
        # [3, 6, 9]
        return [row[c] for row in self.data]

    @property
    def nrows(self):
        # return the number of rows
        return len(self.data)

    @property
    def ncolumns(self):
        # return the number of columns
        return len(self.data[0])

    def transpose(self):
        # return a new Matrix whose content is same as this
        # Matrix except the row and column positions are
        # switched.  In the example above,
        # M.transpose() would return
        # Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        # Note: use zip() to do the transpose
        newM = copy.deepcopy(self)
        newM.data = [list(i) for i in zip(*self.data)]
        return newM

    def randomize(self):
        # return another matrix whose content is the same as
        # this matrix except their positions are randomized.
        # Notice that you must reduce the dimensions of the matrix to one dimension(flatten it)
        # and then randomize it using random.shuffle, and finally form the two dimensional matrix again.
        newM = copy.deepcopy(self)
        new_list = []
        for i in self.data:
            for j in i:
                new_list.append(j)
        #print(new_list)
        random.shuffle(new_list)
        #print(new_list)
        n = self.ncolumns
        #print(n)
        shuffled_list = [new_list[i:i+n] for i in range(0, len(new_list), n)]
        #print(shuffled_list)
        newM.data = copy.deepcopy(shuffled_list)
        return newM

# For judging purpose
instantiate_M = input()
exec(instantiate_M)
randomize_M = input()
exec(randomize_M)
print_row_M = input()
exec(print_row_M)
instantiate_N = input()
exec(instantiate_N )
transpose_N = input()
exec(transpose_N )
print_row_N = input()
exec(print_row_N)