from calc  import search
from task1 import alphabet
from table import tab1
from dictionary import dicta
from shape import calc


import unittest

class TestAssignmentOne(unittest.TestCase):

    

    def test_alphabet(self):
        self.assertEqual(alphabet('mobile'), 'mbl')
        self.assertEqual(alphabet('MOBILE'), 'MBL')
        self.assertEqual(alphabet('MobIlE'), 'Mbl')

    def test_calc(self):
        self.assertEqual(search('This is javaScript','i'), [2,5,15])


    def test_table(self):
        self.assertEqual(tab1(3), [[1],[2,4],[3,6,9]])


  
    def test_dicta(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(dicta(l1), d1)




    def test_calc(self):
        self.assertEqual(calc("s", 2), 4.0)
        self.assertEqual(calc("t", 2, 3), 3.0)
        self.assertEqual(calc("c", 2), 12.56)
        self.assertEqual(calc("r", 2, 5), 10.0)

if __name__ == '__main__':
    unittest.main()