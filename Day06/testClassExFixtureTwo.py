'''
    Writing test cases using classes and methods
    Introducing setup and teardown methods using class methods...
'''

class TestClass:
    @classmethod
    def setup_class(cls):
        print(f'\nSetup() called....')

    @classmethod
    def teardown_class(cls):
        print(f'\nTeardown() called....')
        
    def test_methodOne(self):
        assert 10 == 10
        print('\nmethodOne()...')

    def test_methodTwo(self):
        assert 10 != 20
        print('\nmethodTwo()...')

