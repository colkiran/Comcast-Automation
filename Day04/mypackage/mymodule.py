import msvcrt

banks = ['SBI', 'IOB', 'ICICI', 'YES Bank', 'HDFC']

cards = {'normal': 40000, 'gold': 100000, 'platinum': 300000}

amount = 5000

def get_balance():
    print(f"Balance is :{amount}")

if __name__ == '__main__':
    get_balance()

