

def parse_input(input_file):
    # split the text file into lines and then make each line an array of integers to remove the spaces and group them
    return [list(map(int, s.split())) for s in input_file.read().splitlines()]

def find_distance(num_1, num_2):
    return abs(num_1 - num_2)

def create_ordered_lists(int_lists):
    list_1 = []
    list_2 = []
    for int_list in int_lists:
        list_1.append(int_list[0])
        list_2.append(int_list[1])
    list_1.sort()
    list_2.sort()
    return list_1, list_2

def main():
    ordered_list_1, ordered_list_2 = create_ordered_lists(parse_input(open('input.txt')))
    print(ordered_list_1, ordered_list_2)

    distances = []
    for i in range(len(ordered_list_1)):
        distances.append(find_distance(ordered_list_1[i], ordered_list_2[i]))
    total_distance = sum(distances)
    print(total_distance)

if __name__ == '__main__':
    main()
