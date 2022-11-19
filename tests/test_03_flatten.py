import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import unittest
from flatten import flatten


class Test03Flatten(unittest.TestCase):

    def test_flatten(self):
        '''
        Tests that flatten produces the expected flattened object
        '''
        expected = {}

        input = {}

        print('Test 03: flatten method on an empty object produces the same object')
        result = flatten(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()