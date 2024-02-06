def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width


def main():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        result = calculate_area(length, width)

        if isinstance(result, str):
            print(result)
        else:
            print("The area of the rectangle is:", result)
    except ValueError:
        print("Please enter valid numerical values for length and width.")


if __name__ == "__main__":
    main()
