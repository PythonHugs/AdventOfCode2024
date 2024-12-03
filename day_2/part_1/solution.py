

def parse_input(input_file):
    # split the text file into lines and then make each line an array of integers to remove the spaces and group them
    return [list(map(int, s.split())) for s in input_file.read().splitlines()]

def check_if_increasing(num_1, num_2):
    # num 2 must be greater than num 1
    pass

def check_if_decreasing(num_1, num_2):
    # num 2 must be lesser than num 1
    pass

def check_if_gradual(num_1, num_2):
    # num 1 must be different than num 2 but not by more than 3
    pass

def main():
    print(parse_input(open('example.txt')))


if __name__ == '__main__':
    main()
