import time

def foo(x: int, y=10):
    """
    Add
    :param x: 
    :param y: 
    :return: result
    
    Example:
    print(foo(1))
    """
    return x + y


def foo2(x):
    """
    None doc in foo2
    """
    return x


if __name__ == '__main__':
    print(foo(1))
