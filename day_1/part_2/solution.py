

def parse_input(input_file):
    # split the text file into lines and then make each line an array of integers to remove the spaces and group them
    return [list(map(int, s.split())) for s in input_file.read().splitlines()]

def create_lists(int_lists):
    list_1 = []
    list_2 = []
    for int_list in int_lists:
        list_1.append(int_list[0])
        list_2.append(int_list[1])
    return list_1, list_2

def main():
    list_1, list_2 = create_lists(parse_input(open('input.txt')))
    print(list_1, list_2)

    similarities = []
    for num in list_1:
        sim_count = list_2.count(num)
        similarities.append(num * sim_count)
    print(similarities)
    total_similarities = sum(similarities)
    print(total_similarities)


if __name__ == '__main__':
    main()
