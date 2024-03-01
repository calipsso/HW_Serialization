import unittest
from main import FunctionsElements
from main import ElementsStorage
class FuncElementsTesting(unittest.TestCase):
    def testEmptyStorage(self):
        fet = FunctionsElements
        self.assertEqual(fet.arithmElements(454, 10), 50)


if __name__ == "__main__":
    unittest.main()
