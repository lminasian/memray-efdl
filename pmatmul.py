import matmul
from matmul import Matrix

class UserFriendlyMatrix():
    def __init__(self, mat):
        self.mat = mat

    @classmethod
    def from_list(cls, lst):
        dim_0_size = len(lst)
        assert dim_0_size > 0, "Expected list to have dim 0 non-empty"
        assert isinstance(lst[0], list), "Expected List[List[int]], got: List[%s]" % (type(lst[0]),)
        dim_1_size = len(lst[0])
        assert dim_1_size > 0, "Expected list to have dim 1 non-empty"
        for i in range(1, len(lst)):
            assert dim_1_size == len(lst[i]), "Expected all nested lists to have the same size"
        mat = matmul.empty(dim_0_size, dim_1_size)
        for i in range(dim_0_size):
            for j in range(dim_1_size):
                mat.set(i, j, lst[i][j])
        return cls(mat)

    @classmethod
    def from_matrix(cls, mat):
        return cls(mat)

    def __mult__(other):
        return PrintableMatrix(self.mat * other.mat)

    def __add__(other):
        return PrintableMatrix(self.mat + other.mat)

    def __matmul__(other):
        return PrintableMatrix(self.mat @ other.mat)

    def __repr__(self):
        s = "PrintableMatrix([\n"
        for i in range(self.nrows):
            s += "    "
            s += "["
            for j in range(self.ncols):
                s += str(self.matrix.get(i, j))
                s += ', '
            s += "],"
            s += '\n'
        s += "], size = [%d, %d])" % (self.nrows, self.ncols,)
        return s

    @property
    def nrows(self):
        return self.matrix.nrows

    @property
    def ncols(self):
        return self.matrix.ncols
