from goph420_lab00.functions import (
    add,
    subtract,
    multiply,
    divide,
)


def main():
    x = 5
    y = 22

    print(f"add(x: {x}, y: {y}): {add(x, y)}")
    print(f"subtract(x: {x}, y: {y}): {subtract(x, y)}")
    print(f"multiply(x: {x}, y: {y}): {multiply(x, y)}")
    print(f"divide(x: {x}, y: {y}): {divide(x, y)}")


if __name__ == "__main__":
    main()
