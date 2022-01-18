def calculate(*args):
    result = 0
    for i in args:
        if isinstance(i,(int,float)):
            result = result + i
        else:
            pass
    return result
