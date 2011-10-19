import unittest
from twitter import Twitter
from twitter.api import urllib_request


class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()
        #self.twitter.callable_cls = DummyTwitter()

    def test_calls_respect_request_only_argument(self):
        request = self.twitter.foo.bar(__request_only=True)
        self.assertTrue(isinstance(request, urllib_request.Request))
        self.assertEqual(request.get_full_url(),
            'https://api.twitter.com/1/foo/bar.json?')

    def test_calls_respect_method_argument(self):
        request = self.twitter.foo.bar(__request_only=True, __method='POST',
            foo='bar')
        self.assertEqual(request.get_method(), 'POST')

