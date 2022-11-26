def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    n=pow(x,2)+pow(x,3)*6+3*x*y
    return n
print(main(5,2))