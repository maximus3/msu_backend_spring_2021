import unittest
from custom_meta import CustomMeta


class TestClass(metaclass=CustomMeta):
    some_field = None

    def __init__():
        pass

    def some_method():
        pass


class SomeTest(unittest.TestCase):

    def test_method_rename(self):
        self.assertFalse(hasattr(TestClass, 'some_method'))
        self.assertTrue(hasattr(TestClass, 'custom_some_method'))

    def test_field_rename(self):
        self.assertFalse(hasattr(TestClass, 'some_field'))
        self.assertTrue(hasattr(TestClass, 'custom_some_field'))

    def test_magic_method_not_rename(self):
        self.assertTrue(hasattr(TestClass, '__init__'))
        self.assertFalse(hasattr(TestClass, 'custom___init__'))


if __name__ == '__main__':
    unittest.main()
