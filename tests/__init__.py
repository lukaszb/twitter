import os
import sys
import unittest

THIS = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(THIS, '..')))
sys.path.insert(0, os.path.abspath(os.path.join(THIS, '..', 'twitter')))

from test_oauth import *



def main():
    unittest.main()

if __name__ == '__main__':
    main()

