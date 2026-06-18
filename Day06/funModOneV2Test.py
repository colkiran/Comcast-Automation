from funModOne import funOne

from fileOne import funThree, data 

def test_caseThree():
    assert funOne(10) == 50

def test_caseFour():
    assert funThree() is None

def test_dataOne():
    assert 10 in data