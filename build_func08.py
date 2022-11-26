def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    n=pow(x,2)*5*pow(y,3)+x*pow(y,2)
    return n
print(main(7,1))