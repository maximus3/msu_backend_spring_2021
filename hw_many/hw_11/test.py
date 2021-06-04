import unittest
from levenshtein import distance


class SomeTest(unittest.TestCase):
    def test_distances(self):
        self.assertTrue(distance("слово", "слово") == 0)
        self.assertTrue(distance("слова", "слово") == 1)
        self.assertTrue(distance("удаление", "удаленние") == 1)
        self.assertTrue(distance("вставка", "вствка") == 1)
        self.assertTrue(distance("замена", "запена") == 1)
        self.assertTrue(distance("ячсмит", "йцукен") == 6)
        self.assertTrue(distance("", "кверти") == 6)
        self.assertTrue(distance("вместе", "местее") == 2)
        self.assertTrue(distance("", "") == 0)


if __name__ == "__main__":
    unittest.main()
