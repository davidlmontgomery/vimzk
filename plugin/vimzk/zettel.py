"""
Routines for working with zettels (note files).

"""
from vimzk.context import vim
from vimzk.vim_utils import buffer_is_empty


def insert_zettel_template(zid, title_words, zktype='n'):
    """
    Modify buffer contents to initial zettel template.

    This is intended for use in creating a new zettel.
    Therefore, if the buffer already has contents, we
    leave it unmodified.

    """
    if not buffer_is_empty():
        return
    buf = vim.current.buffer

    # heading/title
    if not title_words:
        title_words = ['Untitled',]
    heading = '# ' + ' '.join(title_words)
    buf[0] = heading

    # metadata
    metadata = ':' + zid + ':zk' + zktype + ':'
    buf.append(metadata)

    # blank lines
    buf.append('')
    buf.append('')

    # position cursor
    vim.current.window.cursor = (4, 1)
