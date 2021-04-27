import unittest
from custom_list import CustomList


class AddTest(unittest.TestCase):

    def setUp(self):
        self.basic_custom_list = CustomList([1, 2, 3])
        self.basic_list = [1, 2, 3]
        self.basic_custom_list_2 = CustomList([3, 2, 1])
        self.basic_list_2 = [3, 2, 1]
        self.big_custom_list = CustomList([i for i in range(100)])
        self.big_list = [i for i in range(100)]
        self.small_custom_list = CustomList([1, 2])
        self.small_list = [1, 2]

    def test_list_type(self):
        self.assertIsInstance(self.basic_custom_list + self.basic_custom_list,
                              CustomList)

    def test_eq(self):
        ans = CustomList([2, 4, 6])
        res = self.basic_custom_list + self.basic_custom_list
        self.assertListEqual(list(res), list(ans))

    def test_list_and_custom(self):
        ans = CustomList([4, 4, 4])
        res = self.basic_list_2 + self.basic_custom_list
        self.assertListEqual(list(res), list(ans))

    def test_custom_and_list(self):
        ans = CustomList([4, 4, 4])
        res = self.basic_custom_list_2 + self.basic_list
        self.assertListEqual(list(res), list(ans))

    def test_first_lower(self):
        ans = CustomList([1, 3] + [i for i in range(2, 100)])
        res = self.small_list + self.big_custom_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([1, 3] + [i for i in range(2, 100)])
        res = self.small_custom_list + self.big_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([1, 3] + [i for i in range(2, 100)])
        res = self.small_custom_list + self.big_custom_list
        self.assertListEqual(list(res), list(ans))

    def test_second_lower(self):
        ans = CustomList([1, 3] + [i for i in range(2, 100)])
        res = self.big_custom_list + self.small_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([1, 3] + [i for i in range(2, 100)])
        res = self.big_list + self.small_custom_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([1, 3] + [i for i in range(2, 100)])
        res = self.big_custom_list + self.small_custom_list
        self.assertListEqual(list(res), list(ans))


class SubTest(unittest.TestCase):

    def setUp(self):
        self.basic_custom_list = CustomList([1, 2, 3])
        self.basic_list = [1, 2, 3]
        self.basic_custom_list_2 = CustomList([3, 2, 1])
        self.basic_list_2 = [3, 2, 1]
        self.big_custom_list = CustomList([i for i in range(100)])
        self.big_list = [i for i in range(100)]
        self.small_custom_list = CustomList([1, 2])
        self.small_list = [1, 2]

    def test_list_type(self):
        self.assertIsInstance(self.basic_custom_list - self.basic_custom_list,
                              CustomList)

    def test_eq(self):
        ans = CustomList([0, 0, 0])
        res = self.basic_custom_list - self.basic_custom_list
        self.assertListEqual(list(res), list(ans))

    def test_list_and_custom(self):
        ans = CustomList([2, 0, -2])
        res = self.basic_list_2 - self.basic_custom_list
        self.assertListEqual(list(res), list(ans))

    def test_custom_and_list(self):
        ans = CustomList([-2, 0, 2])
        res = self.basic_custom_list - self.basic_list_2
        self.assertListEqual(list(res), list(ans))

    def test_first_lower(self):
        ans = CustomList([1, 1] + [i for i in range(-2, -100, -1)])
        res = self.small_list - self.big_custom_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([1, 1] + [i for i in range(-2, -100, -1)])
        res = self.small_custom_list - self.big_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([1, 1] + [i for i in range(-2, -100, -1)])
        res = self.small_custom_list - self.big_custom_list
        self.assertListEqual(list(res), list(ans))

    def test_second_lower(self):
        ans = CustomList([-1, -1] + [i for i in range(2, 100)])
        res = self.big_custom_list - self.small_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([-1, -1] + [i for i in range(2, 100)])
        res = self.big_list - self.small_custom_list
        self.assertListEqual(list(res), list(ans))

        ans = CustomList([-1, -1] + [i for i in range(2, 100)])
        res = self.big_custom_list - self.small_custom_list
        self.assertListEqual(list(res), list(ans))


class EqTest(unittest.TestCase):

    def test_not_eq(self):
        self.assertNotEqual(CustomList([1, 2, 3]), CustomList([1, 2, 4]))

    def test_eq(self):
        self.assertEqual(CustomList([1, 2, 3]), CustomList([1, 1, 4]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([1, 5]))
        self.assertEqual(CustomList([1, 2, 3]), CustomList([6]))

    def test_lt(self):
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([1, 1, 10]))
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([1, 500]))
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([60]))
