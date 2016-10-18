import unittest

class ListTest(unittest.TestCase):
    def test1(self):
        l = [1, 2, 3]
        with self.assertRaises(IndexError):
            l[len(l)]


if __name__ == '__main__':
    unittest.main()
