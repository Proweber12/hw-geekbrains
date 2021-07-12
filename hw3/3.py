def type_logger(func):

    def wrapper(*args, **kwargs):
        for x in *args, *kwargs.values():
            print(f'{func.__name__}({x}: {type(x)})', end=', ')
        res = func(*args, **kwargs)
        return res

    return wrapper

@type_logger
def calc_cube(*args: int, **kwargs: int) -> int:
   pass

a = calc_cube(5, 26, 643, 9.34, cube=27)