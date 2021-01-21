"""
Pytest
-- pip install pytest
-- pip install pytest-cov
"""

"""
unittest vs pytest -- unittest first
"""
# import unittest
# from hello_yo import hello_name
#
# class TestHello(unittest.TestCase):
#
#     def test_hello_name(self):
#         self.assertEqual(hello_name('bob'), 'hello bob')
#
# if __name__ == '__main__':
#     unittest.main()

"""
unittest vs pytest -- pytest
"""
from hello_yo import hello_name

def test_hello_name():
    assert hello_name('bob') == 'hello bob'


