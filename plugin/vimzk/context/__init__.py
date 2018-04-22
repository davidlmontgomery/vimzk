"""
Provides context.vim.

When when running within the vim editor, context.vim
will be the vim pseudomodule provided by the vim editor.
In other contexts (e.g., unittesting), context.vim
will be a mock object.

"""

try:
    import vim
except ImportError:
    from vimzk.context.mock_vim import MockVim
    vim = MockVim()
