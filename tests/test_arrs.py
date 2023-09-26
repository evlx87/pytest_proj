from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_get_with_default():
    array = [1, 2, 3, 4, 5]
    index = 10
    default_value = "Not Found"
    result = arrs.get(array, index, default_value)
    assert result == default_value


def test_get_with_negative_index():
    array = [1, 2, 3, 4, 5]
    index = -2
    result = arrs.get(array, index)
    assert result == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_my_slice_with_negative_indices():
    coll = [1, 2, 3, 4, 5]
    start = -3
    end = -1
    result = arrs.my_slice(coll, start, end)
    assert result == [3, 4]


def test_my_slice_default_start():
    coll = [1, 2, 3, 4, 5]
    end = 3
    result = arrs.my_slice(coll, end=end)
    assert result == [1, 2, 3]


def test_my_slice_default_end():
    coll = [1, 2, 3, 4, 5]
    start = 2
    result = arrs.my_slice(coll, start=start)
    assert result == [3, 4, 5]


def test_my_slice_empty_list():
    coll = []
    result = arrs.my_slice(coll)
    assert result == []
