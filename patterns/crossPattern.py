def print_x_pattern(s):
    length = len(s)

    for i in range(length):
        for j in range(length):
            if i == j or i + j == length - 1:
                print(s[i], end='')
            else:
                print(' ', end='')
        print()

if __name__ == "__main__":
    input_str = "NAVEENKUMAR"
    print_x_pattern(input_str)
