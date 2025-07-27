def add(a, b):
    result = a + b
    return result


def multiply(a, b):
    result = a * b
    return result


def main():
    x = 5
    y = 10

    sum_result = add(x, y)
    print(f"Sum of {x} and {y} is {sum_result}")

    product_result = multiply(x, y)
    print(f"Product of {x} and {y} is {product_result}")

    for i in range(5):
        print(f"Current value of i is {i}")
        new_value = multiply(i, x)
        print(f"New value after multiplying {i} and {x} is {new_value}")


if __name__ == "__main__":
    main()