import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import unittest
from flatten import flatten


class Test01Flatten(unittest.TestCase):

    def test_flatten(self):
        '''
        Tests that flatten produces the expected flattened object
        '''
        expected = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test"
        }

        input = {
            "a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "test"
            }
        }

        print('Test 01: flatten method produces a flattened object')
        result = flatten(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()