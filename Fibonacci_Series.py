def generate_fibonacci(n):
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)

    return fibonacci_series[:n]


def main():
    try:
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_series = generate_fibonacci(n)
            print(f"Fibonacci sequence with {n} terms: {fibonacci_series}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
