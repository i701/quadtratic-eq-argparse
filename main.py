import argparse
import cmath
import math
from prettytable import PrettyTable


def get_descriminant(a: float | int, b: float | int, c: float | int) -> float | int:
    """
    Function to calculate and return the descriminant.
    """
    descriminant = (b**2) - (4*a*c)
    return descriminant


def get_solutions(descriminant: float, a: float | int, b: float | int) -> float | int:
    """
    Returns both positive and negative solution for the quadratic equation.
    """
    try:
        solutionOne = (-b-math.sqrt(descriminant)) / (2*a)
        solutionTwo = (-b+math.sqrt(descriminant)) / (2*a)
        return (solutionOne, solutionTwo)
    except ValueError:
        solutionOne = (-b-cmath.sqrt(descriminant)) / (2*a)
        solutionTwo = (-b+cmath.sqrt(descriminant)) / (2*a)
        return (solutionOne, solutionTwo)


def main() -> None:
    """
    Main function to print the solution.
    """
    parser = argparse.ArgumentParser(
        description="CLI tool to solve Quadratic equations.")
    parser.add_argument("-a", "--aCoefficient", metavar="a-coefficient",
                        type=float, help="Coefficient of x²")
    parser.add_argument("-b", "--bCoefficient", metavar="b-coefficient",
                        type=float, help="Coefficient of x")
    parser.add_argument("-c", "--constant", type=float, help="Constant")
    args = parser.parse_args()

    if args.aCoefficient and args.bCoefficient and args.constant:
        d = get_descriminant(
            args.aCoefficient, args.bCoefficient, args.constant)
        solutions = get_solutions(d, args.aCoefficient, args.bCoefficient)
        if solutions is None:
            print("There was an error. Try again.")
        else:
            sol1 = solutions[0]
            sol2 = solutions[1]
            x = PrettyTable()
            x.field_names = ["Solution", "Value"]
            x.add_row(["Soltion 1:", sol1])
            x.add_row(["Soltion 2:", sol2])
            print(x)


if __name__ == '__main__':
    main()
