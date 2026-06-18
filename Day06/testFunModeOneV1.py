from funModOne import funOne

from fileOne import funThree, data 

def test_caseOne():
    assert funOne(10) == 50

def test_caseTwo():
    assert funOne(5) != 50

