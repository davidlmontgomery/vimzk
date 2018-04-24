"""
Provides MockVim for testing code that Vim's builtin module/singleton 'vim'.

"""
import mock


class MockVim(mock.MagicMock):
    """Mock of vim for testing."""
    pass
