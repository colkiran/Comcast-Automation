from pytest import fixture

@fixture(scope='module')
def mySetupTeardown():
    print(f'\nsetup() called....')
    yield 
    print(f'\nteardown() called....')

def test_FunOne(mySetupTeardown):
    assert 10 + 20 == 30
    print(f'\ntest test_FunOne()....')

def test_FunTwo(mySetupTeardown):
    assert 'Some String'.lower() == 'some string'
    print(f'\ntest test_FunTwo()....')