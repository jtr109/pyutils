from unittest import TestCase
import datetime


from pyutils.datetime import timestamp


class TimeStampTestCase(TestCase):

    def test_timestamp(self):
        d = datetime.datetime(2019, 6, 18, 11, 7)
        ts = timestamp(d)
        expected = 1560827220000
        self.assertEqual(ts, expected)
