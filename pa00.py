import sys

def factor_integer(n):
    """Return the factors of the given integer n."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def standard_io():
    """Handle standard input/output functionality."""
    try:
        n = int(input("Enter an integer to factor: "))
        print(f"Factors of {n}: {factor_integer(n)}")
    except ValueError:
        print("Please enter a valid integer.")

def arg_io(args):
    """Handle command-line argument functionality."""
    try:
        n = int(args[1])
        print(f"Factors of {n}: {factor_integer(n)}")
    except (ValueError, IndexError):
        print("Please provide a valid integer as an argument.")

def main():
    if len(sys.argv) == 2:
        # Use argument functionality if 2 args are passed (script name and one integer)
        arg_io(sys.argv)
    else:
        # Use standard input/output functionality otherwise
        standard_io()

if __name__ == "__main__":
    main()
