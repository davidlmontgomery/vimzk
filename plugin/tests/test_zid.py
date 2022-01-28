"""
Test zid generation.

"""
import unittest

from datetime import date

from vimzk.zid import create_zid, ZID_LENGTH, ZK_START_DATE


class ZidTests(unittest.TestCase):
    """Test zid generation."""

    @staticmethod
    def _check_zid(zid):
        """Verify zid is well formed: 8 lowercase alphanumeric chars."""
        assert len(zid) == ZID_LENGTH
        assert all(cc.isdigit() or cc.islower() for cc in zid)

    @unittest.mock.patch('vimzk.string_utils.random')
    def test_random_prefix(self, mock_zid_random):
        """Test we're calling random for prefix."""
        # Have random.choice return determined values
        mock_zid_random.choice.side_effect = ['y', '2', 'k', '9', 'q']
        zid = create_zid(date(2010, 1, 20))
        self._check_zid(zid)
        self.assertEqual(zid[0:5], 'y2k9q')

    def test_start_date(self):
        """Test for the start date."""
        self.assertEqual(ZK_START_DATE, date(2018, 4, 18))
        zid = create_zid(ZK_START_DATE)
        self.assertEqual(zid[-3:], '000')
        self._check_zid(zid)

    def test_before_start_date(self):
        """Test a date before project started."""
        zid = create_zid(date(2018, 4, 17))
        self.assertEqual(zid[-3:], '001')
        self._check_zid(zid)

    def test_apr_18_2019(self):
        """Test an arbitrary date."""
        zid = create_zid(date(2019, 4, 18))
        self.assertEqual(zid[-3:], '0a5')
        self._check_zid(zid)

    def test_jan_12_2146(self):
        """Test end of day counter range."""
        zid = create_zid(date(2146, 1, 12))
        self.assertEqual(zid[-3:], 'zzz')
        self._check_zid(zid)

    def test_jan_13_2146(self):
        """Test after day counter wraps."""
        zid = create_zid(date(2146, 1, 13))
        self.assertEqual(zid[-3:], '000')
        self._check_zid(zid)
