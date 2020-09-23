import pytest

from fizzbuzz_yo import fizzbuzz_yo

@pytest.mark.parametrize("arg, ret",[
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'FizzBuzz'),
    (16, 16),
    (1000, 'Buzz'),
    (3000, 'FizzBuzz'),
    (2001, 'Fizz'),
])

def test_fizzbuzz_yo(arg, ret):
    assert fizzbuzz_yo(arg) == ret