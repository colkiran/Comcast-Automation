import pytest

@pytest.mark.parametrize("data1, data2, expected", [
    (10, 20, 30),
    (10, -20, -10),
    ("hello", " world", "hello world")
])
def test_Addition(data1, data2, expected):
    assert data1 + data2 == expected
