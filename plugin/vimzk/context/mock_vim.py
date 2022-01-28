"""
Provides MockVim for testing code that Vim's builtin module/singleton 'vim'.

"""
from unittest.mock import MagicMock


class MockVim(MagicMock):
    """Mock of vim for testing."""
    pass
