import unittest
from solution import is_anagram

class TestStringMethods(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(is_anagram('foefet', 'toffee'), True, 'The word foefet is an anagram of toffee')
        self.assertEqual(is_anagram('Buckethead', 'DeathCubeK'), True, 'The word Buckethead is an anagram of DeathCubeK')
        self.assertEqual(is_anagram('Twoo', 'WooT'), True, 'The word Twoo is an anagram of WooT')
        self.assertEqual(is_anagram('dumble', 'bumble'), False, 'Characters do not match for test case dumble, bumble')
        self.assertEqual(is_anagram('ound', 'round'), False, 'Missing characters for test case ound, round')
        self.assertEqual(is_anagram('apple', 'pale'), False, 'Same letters, but different count')

if __name__ == '__main__':
    unittest.main()
