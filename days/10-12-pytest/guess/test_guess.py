"""
command line: pytest --> will run the tests
command line: pytest --cov-report term-missing --cov='.'
--> will check the coverage for how much code is being tested
"""
from unittest.mock import patch
import random, pytest

from guess import get_random_number, Game

## this allows us everytime when random module is called, to return 17
@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17

"""
Mocking user_input
"""
@patch("builtins.input", side_effect=[11, '12', 'Bob', 12, 5, -1, 21, 7, None])

def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # not a number
    with pytest.raises(ValueError):
        game.guess()
    # already guessed
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 5
    # out of range values
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 7
    # user hit enter
    with pytest.raises(ValueError):
        game.guess()

"""
Testing a program's stdout with capfd
"""
def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    # print(out)  # run with pytest -s test_guess.py --> its not capturing the output but it prints it to the console // this can be run only once per assertion if run on multiple assertions it will fail the test
    assert out.rstrip() == '1 is too low'  # run without -s to just check the percentage for passing

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'


    # assert not game._validate_guess(3)
    # assert game._validate_guess(2)


@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    """
    Modify variable in Game class back from self._answer = 6
    to self._answer = get_random_number() when done
    """
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range', '9 is too high',
                'Already guessed', '6 is correct!', 'It took you 3 guesses']
    output = [line.strip() for line in out.split('\n') if line.strip()]

    for line, exp in zip(output, expected):
        assert line == exp

@patch("builtins.input", side_effect=[None, 5, 9, 14, 11, 12])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    game()
    assert game._win is False





#
#
# @patch("builtins.input", side_effect=[11, '12', 'Bob', 12, 5,
#                                       -1, 21, 7, None])
# def test_guess(inp):
#     game = Game()
#     # good
#     assert game.guess() == 11
#     assert game.guess() == 12
#     # not a number
#     with pytest.raises(ValueError):
#         game.guess()
#     # already guessed 12
#     with pytest.raises(ValueError):
#         game.guess()
#     # good
#     assert game.guess() == 5
#     # out of range values
#     with pytest.raises(ValueError):
#         game.guess()
#     with pytest.raises(ValueError):
#         game.guess()
#     # good
#     assert game.guess() == 7
#     # user hit enter
#     with pytest.raises(ValueError):
#         game.guess()
#
#
# def test_validate_guess(capfd):
#     game = Game()
#     game._answer = 2
#
#     assert not game._validate_guess(1)
#     out, _ = capfd.readouterr()
#     assert out.rstrip() == '1 is too low'
#
#     assert not game._validate_guess(3)
#     out, _ = capfd.readouterr()
#     assert out.rstrip() == '3 is too high'
#
#     assert game._validate_guess(2)
#     out, _ = capfd.readouterr()
#     assert out.rstrip() == '2 is correct!'
#
#
# @patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
# def test_game_win(inp, capfd):
#     game = Game()
#     game._answer = 6
#
#     game()
#     assert game._win is True
#
#     out = capfd.readouterr()[0]
#     expected = ['4 is too low', 'Number not in range',
#                 '9 is too high', 'Already guessed',
#                 '6 is correct!', 'It took you 3 guesses']
#
#     output = [line.strip() for line
#               in out.split('\n') if line.strip()]
#     for line, exp in zip(output, expected):
#         assert line == exp
#
#
# @patch("builtins.input", side_effect=[None, 5, 9, 14, 11, 12])
# def test_game_lose(inp, capfd):
#     game = Game()
#     game._answer = 13
#
#     game()
#     assert game._win is False
