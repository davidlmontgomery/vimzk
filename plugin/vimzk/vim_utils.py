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
    is_empty = True
    for line in buf:
        if line != '':
            is_empty = False
            break
    return is_empty
