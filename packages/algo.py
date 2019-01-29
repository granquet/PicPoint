import math

def bisect_tuple(lst, elem, fun):
    left, right = 0, len(lst)
    while(right - left > 2):
        inf = math.floor((right + left)/2)
        if ( fun(elem, lst[inf]) ):
            left = inf
        else:
            right = inf
    return (left, right)

