def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    n=2*(pow(y,3)+pow(x,2)*y)

    return n
print(main(2,4))

