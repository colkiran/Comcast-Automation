'''
    Writing test cases using classes and methods
    Introducing setup and teardown methods...
'''

class TestClass:
    def setup_method(self):
        print(f'\nsetup method...')
    
    def teardown_method(self):
        print(f'\nteardown method...')

    def test_methodOne(self):
        assert 10 == 10
        print('\nmethodOne()...')

    def test_methodTwo(self):
        assert 10 != 20
        print('\nmethodTwo()...')

