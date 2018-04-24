"""
Test vim_utils.py.

"""
import unittest

from vimzk import vim_utils
from vimzk.context import vim


class BufferIsEmptyTests(unittest.TestCase):
    """Test buffer_is_empty."""

    def test_current_no_lines(self):
        """
        True for current buffer with no lines.

        Not sure this can occur in real vim module. It appears
        when you start a new file it immediately regards buffer
        as having one empty line. And even if you open a
        completely empty 0-byte file, len(vim.current.buffers)
        is 1.

        """
        vim.current.buffer = []
        self.assertEqual(vim_utils.buffer_is_empty(), True)

    def test_current_one_empty_line(self):
        """True for current buffer with one empty line."""
        vim.current.buffer = ['',]
        self.assertEqual(vim_utils.buffer_is_empty(), True)

    def test_current_one_nonempty_line(self):
        """False for current buffer with non-empty line 1."""
        vim.current.buffer = ['X',]
        self.assertEqual(vim_utils.buffer_is_empty(), False)

    def test_current_two_empty_lines(self):
        """
        False for current buffer with two empty lines.

        Such a buffer isn't a newly created, unmodified buffer.

        """
        vim.current.buffer = ['', '',]
        self.assertEqual(vim_utils.buffer_is_empty(), False)
