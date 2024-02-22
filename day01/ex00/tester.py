from give_bmi import give_bmi, apply_limit


def main():
    """
    main function calls function calculating bmi
    """
    height = []
    weight = []

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
