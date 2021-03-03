import pytest
@pytest.mark.parametrize('nums, expected', [((1, 2, 3), 6),
                                            ((54, 14, 88), 156),
                                            ((22, 0, 8), 30)])
def test_sum(nums, expected):
    sum = 0
    for num in nums:
        sum += num
    assert sum == expected


@pytest.mark.parametrize('source, param', [(("a", "b", "c"), '1'),
                                                     (("d", "e", "f"), '2')])
def test_insert(source, param):
    try:
        for s in source:
            s[0]=param
    except TypeError:
        pass

@pytest.mark.parametrize('source, param, expected', [(("a", "b", "c"), ("d", "e"), ("a", "b", "c", "d", "e")),
                                                     (("d", "e", "f"), ("g", "h"), ("d", "e", "f", "g", "h"))])
def test_append(source, param, expected):
   assert source + param == expected

@pytest.mark.parametrize('num', [0, 2, 4, 6, 8, 10])

def test_even(num):
    assert num %2 == 0


@pytest.mark.parametrize('str_num, num', [("4", 4), ("8", 8), ("15", 15), ("16", 16), ("23", 23), ("42", 42)])

def test_cast(str_num, num):
    assert int(str_num) == num

def test_invalid_cast():
    try:
        assert int("test") == 0
    except ValueError:
        pass
