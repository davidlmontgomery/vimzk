"""
Early hacking on tests for vimzk.

"""
import unittest

from vimzk import vimzk


#@unittest.skip("Don't forget to test!")
class VimzkTests(unittest.TestCase):
    """Stub TestCase for vimzk."""

    def test_example_fail(self):
        """Demo test for vimzk."""
        result = vimzk.vimzk_example()
        self.assertEqual('Happy Hacking!', result)
