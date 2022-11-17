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
    def test_read3(self):
        printer = CSVPrinter("sample.csv")

