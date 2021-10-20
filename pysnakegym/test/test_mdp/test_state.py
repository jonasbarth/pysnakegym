import pytest

from pysnakegym.game import SnakeGame
from pysnakegym.mdp.state import BooleanState, GridState

import numpy as np

@pytest.fixture
def boolean_state():
    game = SnakeGame(200, 200, 20)

    state = BooleanState(game)
    return state

@pytest.fixture
def vicinity():
    return np.array([[4, 5], [5, 4], [6, 5]])

@pytest.fixture
def snake_body():
    return np.array([[5, 5]])


def test_get_danger(boolean_state, vicinity, snake_body):
    assert(boolean_state.get_danger(vicinity, snake_body) == np.array([0, 0, 0])).all()


@pytest.fixture
def grid_state():
    game = SnakeGame(200, 200, 20)

    state = GridState(game)
    return state

def test(grid_state):
    print(grid_state.get_state())