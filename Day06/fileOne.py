data = [10, 20, 30, 40, 'Some text here', 'Whatever data']

def funOne():
    print(f'funOne()...{__name__}')

def funTwo():
    print(f'funTwo()...{__name__}')

def funThree():
    print(f'funThree()...{__name__}')

class ClassOne:
    def methodOne(self):        
        print(f'methodOne()...{__name__}')
    
    def methodTwo(self):
        print(f'methodTwo()...{__name__}')

    def methodThree(self):
        print(f'methodThree()...{__name__}')

if __name__ == '__main__':
    print(data)

    funOne()
    funTwo()
    funThree()

    obj = ClassOne()
    obj.methodOne()
    obj.methodTwo()
    obj.methodThree()

