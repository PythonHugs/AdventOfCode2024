

def parse_input(input_file):
    # split the text file into lines and then make each line an array of integers to remove the spaces and group them
    return [list(map(int, s.split())) for s in input_file.read().splitlines()]

def is_increasing(num_1, num_2):
    # num 2 must be greater than num 1
    if num_2 > num_1:
        return True
    return False

def is_gradual(num_1, num_2):
    # num 1 must be different from num 2 but not by more than 3
    if abs(num_1 - num_2) == 0:
        return False
    if abs(num_1 - num_2) <= 3:
        return True
    return False

def scan_loop(num_array):
    is_safe = True

    if is_increasing(num_array[0], num_array[1]):
        for i in range(len(num_array)):
            if i != len(num_array) - 1:
                print(num_array[i], num_array[i+1])
                if not is_gradual(num_array[i], num_array[i + 1]):
                    is_safe = False
                    break
                if not is_increasing(num_array[i], num_array[i + 1]):
                    is_safe = False
                    break

    else:
        for i in range(len(num_array)):
            if i != len(num_array) - 1:
                print(num_array[i], num_array[i + 1])
                if not is_gradual(num_array[i], num_array[i + 1]):
                    is_safe = False
                    break
                if is_increasing(num_array[i], num_array[i + 1]):
                    is_safe = False
                    break

    return is_safe

def main():
    parsed_data = parse_input(open('input.txt'))
    print(parsed_data)
    num_safe = 0
    for report in parsed_data:
        if scan_loop(report):
            num_safe += 1
            print('Safe')
        else: print('Unsafe')
    print(num_safe)


if __name__ == '__main__':
    main()
