import unittest

from speciallecture.CSVPrinter import CSVPrinter


def setUpModule():
    print('Running setUpModule')
def tearDownModule():
    print('Running tearDownModule')
class TestCSVPrinter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")
    def setUp(self):
        print("Running setUp")
    def tearDown(self):
        print("Running tearDown")
    def test_read1(self):
        print("Running test_read1")
    def test_read2(self):
        print("Running test_read2")
    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual("bbb2", line[1][1])

    # def test_read3(self):
    #     try:
    #         printer = CSVPrinter("sample2.csv")
    #         printer.read()
    #         unittest.TestCase.fail("This line should not be invoked")
    #     except FileNotFoundError as e:
    #         pass
    #
    # def test_read4(self):
    #     with self.assertRaises(FileNotFoundError):
    #         printer = CSVPrinter("sample2.csv")
    #         printer.read()
    #         unittest.TestCase.fail("This line should not be invoked")
    #     print("aaa")


