import unittest
import newyear_Submission as nu

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        z,y = nu.minimumBribes([1,2,5,4,7,8,6,4])
        print(z,y)
        self.assertEqual(z,7)

if __name__ == '__main__':
    unittest.main()
