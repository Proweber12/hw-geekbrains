def val_checker(func):

        def wrapper(x):
            res = func(x)
            if x > 0:
                print(res)
            else:
                raise ValueError(f'wrong val {x}')
        return wrapper


@val_checker
def calc_cube(x):
   return x ** 3

a = calc_cube(5)