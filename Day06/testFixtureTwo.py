import pytest

@pytest.fixture
def userData():
    return {
        'name':'Sudhakar',
        'role':'Trainer'
    }

def test_username(userData):
    assert userData['name'] == 'Sudhakar'

def test_role(userData):
    assert userData['role'] != 'Admin'