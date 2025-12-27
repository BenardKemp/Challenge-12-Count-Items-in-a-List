import pytest

from challenge_12_count_items_in_a_list import count_items


def test_count_items_basic_integers():
    assert count_items([1, 2, 2, 3]) == {1: 1, 2: 2, 3: 1}


def test_count_items_strings():
    assert count_items(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_items_mixed_hashable_types():
    data = ["x", 1, "x", 1, 1, (2, 3)]
    assert count_items(data) == {"x": 2, 1: 3, (2, 3): 1}


def test_count_items_empty_list():
    assert count_items([]) == {}


def test_count_items_single_item():
    assert count_items([42]) == {42: 1}


@pytest.mark.parametrize(
    "bad_input",
    [
        "abc",
        123,
        None,
        True,
        False,
        {"a": 1},
        (1, 2, 3),
    ],
)
def test_count_items_rejects_non_list_input(bad_input):
    with pytest.raises(TypeError):
        count_items(bad_input)


@pytest.mark.parametrize(
    "bad_list",
    [
        [1, [], 2],          # list is unhashable
        [1, {}, 2],          # dict is unhashable
        [set([1]), 2],       # set is unhashable
        [{"a": 1}],          # dict is unhashable
    ],
)
def test_count_items_rejects_unhashable_items(bad_list):
    with pytest.raises(TypeError):
        count_items(bad_list)
