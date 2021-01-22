import unittest

from hello import hello_name

"""
USING unittest
- Can be run from the command line as well: python3 test_hello.py
- Or even better can be run with pytest(functions or methods that start with test):
--> pytest test_hello.py
"""
# class TestHello(unittest.TestCase):
#
#     def test_hello_name(self):
#         self.assertEqual(hello_name('bob'), 'hello bob')
#
# if __name__ == '__main__':
#     unittest.main()

"""
USING pytest
--> pytest test_hello.py
"""
def test_hello_name():
    assert hello_name('bob') == 'hello bob'

