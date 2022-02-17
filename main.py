import argparse
import cmath
import math
from prettytable import PrettyTable

SUPERSCRIPT = {
    2: "²"
}


def formatNumber(num):
    return int(num) if num % 1 == 0 else num


def get_descriminant(a: float | int, b: float | int, c: float | int) -> float | int:
    """
    Function to calculate and return the descriminant.
    """
    return (b**2) - (4*a*c)


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


def get_equation(a: float | int, b: float | int, c: float | int) -> str:
    """
    Generate the equation for the given arguments.
    """
    EQUATION = f"{a}x{SUPERSCRIPT[2]} + {b}x + {c} = 0"
    if b < 0 and c < 0:
        EQUATION = f"{a}x{SUPERSCRIPT[2]} - {b*-1}x - {c*-1} = 0"
    elif b < 0:
        EQUATION = f"{a}x{SUPERSCRIPT[2]} - {b*-1}x + {c} = 0"
    elif c < 0:
        EQUATION = f"{a}x{SUPERSCRIPT[2]} + {b}x - {c*-1} = 0"

    return EQUATION


def print_solution(sol1: float | int, sol2: float | int, equation=None) -> None:
    x = PrettyTable()
    x.field_names = ["Equation", equation] if equation else [
        "Solution", "Value"]
    x.add_row(["Soltion 1:", sol2])
    x.add_row(["Soltion 2:", sol1])
    print(x)


def main() -> None:
    """
    Main function to print the solution.
    """
    parser = argparse.ArgumentParser(
        description="CLI tool to solve Quadratic equations.")
    parser.add_argument("-a", "--aCoefficient", metavar="a-coefficient", default=1,
                        type=float, help="Coefficient of x²")
    parser.add_argument("-b", "--bCoefficient", metavar="b-coefficient",
                        type=float, help="Coefficient of x")
    parser.add_argument("-c", "--constant", type=float, help="Constant")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.aCoefficient and args.bCoefficient and args.constant:
        d = get_descriminant(
            args.aCoefficient, args.bCoefficient, args.constant)
        solutions = get_solutions(d, args.aCoefficient, args.bCoefficient)

        if solutions is None:
            print("There was an error. Try again.")
        elif args.verbose:
            a = formatNumber(args.aCoefficient)
            if a == 1:
                a = ""
            b = formatNumber(args.bCoefficient)
            c = formatNumber(args.constant)
            eq = get_equation(a, b, c)
            sol1 = solutions[0]
            sol2 = solutions[1]
            print_solution(sol1, sol2, equation=eq)

        else:
            sol1 = solutions[0]
            sol2 = solutions[1]
            print_solution(sol1, sol2)
    else:
        print("Insufficient parameters provided.")


if __name__ == '__main__':
    main()
