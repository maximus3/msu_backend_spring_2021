from itertools import zip_longest


class CustomList(list):

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __add__(self, other):
        return CustomList(
            [a + b for a, b in zip_longest(self, other, fillvalue=0)]
        )

    __radd__ = __add__

    def __sub__(self, other):
        return CustomList(
            [a - b for a, b in zip_longest(self, other, fillvalue=0)]
        )

    def __rsub__(self, other):
        return -(self - other)

    def __neg__(self):
        return CustomList(
            [-a for a in self]
        )
