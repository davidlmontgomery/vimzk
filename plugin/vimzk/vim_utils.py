"""
Utilities for working with vim module.

Documentation for the vim module is here
http://vimdoc.sourceforge.net/htmldoc/if_pyth.html#python-vim

"""
from vimzk.context import vim


def buffer_is_empty(idx=-1):
    """
    Return whether indicated buffer is empty. Use current buffer for idx of -1.

    """
    buf = vim.current.buffer if idx == -1 else vim.buffers[idx]
    if len(buf) > 1:
        return False
    if len(buf) == 1 and buf[0] != '':
        return False
    return True
