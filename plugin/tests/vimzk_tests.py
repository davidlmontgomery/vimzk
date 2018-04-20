import unittest
import vimzk as sut


@unittest.skip("Don't forget to test!")
class VimzkTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vimzk_example()
        self.assertEqual("Happy Hacking", result)
