def f(obj):
    if type(obj) is list or type(obj) is tuple:
        print(type(obj), len(obj))
        for i in obj:
            f(i)
    else:
        print(type(obj), obj)
f([None, -34.5, ['y', 58], 'DF', '8' * 4, 47])
