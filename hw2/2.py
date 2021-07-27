class ExceptionZero(Exception):
    pass


def div(a: float, b: float) -> float:
    try:
        if b == 0:
            raise ExceptionZero
    except ExceptionZero:
        print('Делить на ноль нельзя!')
    else:
        print(a / b)


div(14, 0)