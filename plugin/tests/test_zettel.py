"""
Test zettel.py.

"""
import unittest

from vimzk import zettel
from vimzk.context import vim


class InsertZettelTemplateTests(unittest.TestCase):
    """Test insert_zettel_template."""

    def test_zettel_note_populated(self):
        """Test buffer populated with template note content."""
        # Set up our mock buffer
        vim.current.buffer = ['']

        # Make call under test
        zid = 'abcd5003'
        title_words = ['The', 'Captivating', 'Title']
        zettel.insert_zettel_template(zid, title_words, 'n')

        # Test content
        buf = vim.current.buffer
        self.assertEqual(buf[0], '# ' + ' '.join(title_words))
        self.assertEqual(buf[1], ':{}:zkn:'.format(zid))
        self.assertEqual(buf[2], '')
        self.assertEqual(buf[3], '')
        self.assertEqual(4, len(buf))

        # Test cursor positioning
        (line, col) = vim.current.window.cursor
        self.assertAlmostEqual(line, 4, 'Cursor should be after title and metadata.')
        self.assertAlmostEqual(col, 1, 'Cursor should be at first column.')

    def test_no_change_if_nonempty(self):
        """Test buffer isn't changed if it already has content."""
        # Set up our mock buffer
        vim.current.buffer = ['content']

        # Make call under test
        zid = '5zyxw3zz'
        title_words = ['badda-bing']
        zettel.insert_zettel_template(zid, title_words, 'n')

        # Test content
        self.assertEqual(vim.current.buffer, ['content'])
