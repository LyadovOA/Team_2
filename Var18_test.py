import pytest
from main import count_survivors, prepare_data

data = [
    ['', '0', '', '', '', '54', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '12', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '22', '', '', '', '', '', 'Q'],
    ['', '1', '', '', '', '23', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '75', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '45', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '33', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '20', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '47', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '29', '', '', '', '', '', 'S']
]


def test_count_survivors_filter():
    filter = 30
    result = count_survivors(filter, data)

    assert result == {
        'Выживших': [2, 0, 3],
        'Пассажиров': [3, 1, 6],
        'Пункт посадки': ['C', 'Q', 'S']
    }


def test_count_survivors():
    filter = 100
    result = count_survivors(filter, data)

    assert result == {
        'Выживших': [3, 3, 0],
        'Пассажиров': [6, 3, 1],
        'Пункт посадки': ['S', 'C', 'Q']
    }


def test_count_survivors_empty():
    filter = 100
    result = count_survivors(filter, [])

    assert result == {
        'Выживших': [],
        'Пассажиров': [],
        'Пункт посадки': []
    }


def test_prepare_data():
    filter = 100
    passengers = count_survivors(filter, data)
    result = prepare_data(passengers)
    assert result == {
        'Доля выживших': [33, 40, 0],
        'Пункт посадки': ['S', 'C', 'Q']
    }
