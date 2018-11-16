l = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']

def filt(my_list):
    l_new = [i for i in my_list if type(i) in [int, float]]
    return l_new

new_list = filt(l)
print(new_list)
f=sorted(filt(l))
print(f)
