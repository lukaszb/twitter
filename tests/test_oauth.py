# encoding: UTF-8
import unittest
from twitter.oauth import urlencode_noplus


class TestOAuth(unittest.TestCase):

    def test_urlencode_noplus(self):
        data = {'name': u'Żąłądź'}
        self.assertEqual(urlencode_noplus(data),
            'name=%C5%BB%C4%85%C5%82%C4%85d%C5%BA')

