# Использование циклов внутри функций

def func(params):
    for value in params:
        print('Got value {}'.format(value))
        if value == 1:
            print('Got 1')
            return 1
        print("Still Loping")
    return 'Could not find 1'

func([1,2,3,4,5,6])