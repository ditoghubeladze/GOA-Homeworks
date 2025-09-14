def manual_map(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i)) 
    return result   


def manual_filter(func, iterable):
    result = []
    for i in iterable:
        if func(item):       
            result.append(i)
    return result

nums = [1, 2, 3, 4, 5, 6]
print(manual_filter(nums))  


