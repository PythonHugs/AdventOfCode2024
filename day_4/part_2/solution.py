from collections import Counter


def check_up_left(grid, coords):
    print('checking up left')
    x = coords[0]
    y = coords[1]
    if y >= 2 and x >= 2:
        if grid[x - 1][y - 1] == 'A':
            a_coords = (x - 1, y - 1)
            if grid[x - 2][y - 2] == 'S':
                print('found MAS')
                return 1, a_coords
    return 0, (0, 0)

def check_up_right(grid, coords):
    print('checking up right')
    x = coords[0]
    y = coords[1]
    if y <= len(grid[x]) - 3 and x >= 2:
        if grid[x - 1][y + 1] == 'A':
            a_coords = (x - 1, y + 1)
            if grid[x - 2][y + 2] == 'S':
                print('found MAS')
                return 1, a_coords
    return 0, (0, 0)

def check_down_left(grid, coords):
    print('checking down left')
    x = coords[0]
    y = coords[1]
    if y >= 2 and x <= len(grid) - 3:
        if grid[x + 1][y - 1] == 'A':
            a_coords = (x + 1, y - 1)
            if grid[x + 2][y - 2] == 'S':
                print('found MAS')
                return 1, a_coords
    return 0, (0, 0)

def check_down_right(grid, coords):
    print('checking down right')
    x = coords[0]
    y = coords[1]
    if y <= len(grid[x]) - 3 and x <= len(grid) - 3:
        if grid[x + 1][y + 1] == 'A':
            a_coords = (x + 1, y + 1)
            if grid[x + 2][y + 2] == 'S':
                print('found MAS')
                return 1, a_coords
    return 0, (0, 0)

def find_m(grid):
    m_coords = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if grid[i][j] == 'M':
                m_coords.append((i, j))
    return m_coords

def parse_input(input_file):
    # split the text file into lines and then make each line an array of integers to remove the spaces and group them
    rows = input_file.read().splitlines()
    return [list(row) for row in rows if row]

def main():
    grid = parse_input(open('input.txt'))
    for row in grid:
        print(row)
    # find all diagonal instances of MAS starting with Ms (but note the coords for As)
    m_coords = find_m(grid)
    print(m_coords)
    vert_mas_count = 0
    a_coords = []
    for coords in m_coords:
        print(coords)
        vert_mas_count, a_coord = vert_mas_count + check_up_left(grid, coords)[0], a_coords.append(check_up_left(grid, coords)[1])
        vert_mas_count, a_coord = vert_mas_count + check_up_right(grid, coords)[0], a_coords.append(check_up_right(grid, coords)[1])
        vert_mas_count, a_coord = vert_mas_count + check_down_left(grid, coords)[0], a_coords.append(check_down_left(grid, coords)[1])
        vert_mas_count, a_coord = vert_mas_count + check_down_right(grid, coords)[0], a_coords.append(check_down_right(grid, coords)[1])
    print(vert_mas_count)
    filtered_a_coords = [coord for coord in a_coords if coord != (0, 0)]
    print(filtered_a_coords)
    counter = Counter(filtered_a_coords)
    # count the number of overlapping As to find the X-MASes
    x_mas_count = 0
    for tuple, count in counter.items():
        print(f"{tuple}: {count}")
        if count == 2:
            x_mas_count += 1
    print(x_mas_count)


if __name__ == '__main__':
    main()
