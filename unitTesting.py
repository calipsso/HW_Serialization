import unittest
from main import ElementsStorage
from main import FunctionsElements

class FuncElementsTesting(unittest.TestCase):
    def testEmptyStorage(self):
        fet = FuncElementsTesting()
        self.assertEquals(fet.arithme)


if __name__ == "__main__":
    unittest.main()
