from __future__ import annotations
import matmul
from matmul import Matrix
from typing import List
import functools

class UserFriendlyMatrix:
    def __init__(self, mat):
        self.mat = mat

    @classmethod
    def from_list(cls, lst: List[List[int]]) -> UserFriendlyMatrix:
        dim_0_size = len(lst)
        assert dim_0_size > 0, "Expected list to have dim 0 non-empty"
        assert isinstance(lst[0], list), "Expected List[List[int]], got: List[%s]" % (type(lst[0]),)
        dim_1_size = len(lst[0])
        assert dim_1_size > 0, "Expected list to have dim 1 non-empty"
        for i in range(1, len(lst)):
            assert dim_1_size == len(lst[i]), "Expected all nested lists to have the same size"
        mat = matmul.empty((dim_0_size, dim_1_size))
        for i in range(dim_0_size):
            for j in range(dim_1_size):
                mat.set(i, j, lst[i][j])
        return cls(mat)

    @classmethod
    def from_matrix(cls, mat: Matrix) -> UserFriendlyMatrix:
        return cls(mat.copy())

    @functools.cache
    def matpow(self, n: int) -> UserFriendlyMatrix:
        if n == 1:
            return self
        if n == 0:
            return UserFriendlyMatrix(
                matmul.eye(
                    (self.nrows, self.nrows), 
                    1
                )
            )
        if (n % 2 == 0):
            return self.matpow(n // 2) @ self.matpow(n // 2)
        return self.matpow(n // 2) @ self.matpow(n // 2) @ self

    def __mult__(self, other: UserFriendlyMatrix) -> UserFriendlyMatrix:
        return self.__class__(self.mat * other.mat)

    def __add__(self, other: UserFriendlyMatrix) -> UserFriendlyMatrix:
        return self.__class__(self.mat + other.mat)

    def __matmul__(self, other: UserFriendlyMatrix) -> UserFriendlyMatrix:
        return self.__class__(self.mat @ other.mat)

    def __repr__(self) -> str:
        s = "%s([\n" % (self.__class__.__name__,)
        for i in range(self.nrows):
            s += "    "
            s += "["
            for j in range(self.ncols):
                s += str(self.mat.get(i, j))
                s += ', '
            s += "],"
            s += '\n'
        s += "], size = [%d, %d])" % (self.nrows, self.ncols,)
        return s
    
    def copy(self) -> UserFriendlyMatrix:
        return UserFriendlyMatrix(self.mat.copy())

    @property
    def nrows(self) -> int:
        return self.mat.nrows

    @property
    def ncols(self) -> int:
        return self.mat.ncols


x = UserFriendlyMatrix(matmul.rand((512, 512)))
x = x.matpow(256)