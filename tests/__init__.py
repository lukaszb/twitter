import os
import sys
import unittest

# Make sure we use our twitter, not one installed on the system
THIS = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(THIS, '..')))
sys.path.insert(0, os.path.abspath(os.path.join(THIS, '..', 'twitter')))

from test_oauth import *
from test_twitter import *



def main():
    unittest.main()

if __name__ == '__main__':
    main()

