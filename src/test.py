import unittest


class MyTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual("blub", "blub2")

    def test_true(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
