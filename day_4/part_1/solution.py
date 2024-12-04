

def check_up_left(grid, coords):
    print('checking up left')
    x = coords[0]
    y = coords[1]
    if y >= 3 and x >= 3:
        if grid[x - 1][y - 1] == 'M':
            if grid[x - 2][y - 2] == 'A':
                if grid[x - 3][y - 3] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_up_right(grid, coords):
    print('checking up right')
    x = coords[0]
    y = coords[1]
    if y <= len(grid[x]) - 4 and x >= 3:
        if grid[x - 1][y + 1] == 'M':
            if grid[x - 2][y + 2] == 'A':
                if grid[x - 3][y + 3] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_down_left(grid, coords):
    print('checking down left')
    x = coords[0]
    y = coords[1]
    if y >= 3 and x <= len(grid) - 4:
        if grid[x + 1][y - 1] == 'M':
            if grid[x + 2][y - 2] == 'A':
                if grid[x + 3][y - 3] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_down_right(grid, coords):
    print('checking down right')
    x = coords[0]
    y = coords[1]
    if y <= len(grid[x]) - 4 and x <= len(grid) - 4:
        if grid[x + 1][y + 1] == 'M':
            if grid[x + 2][y + 2] == 'A':
                if grid[x + 3][y + 3] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_left(grid, coords):
    print('checking left')
    x = coords[0]
    y = coords[1]
    if y >= 3:
        if grid[x][y - 1] == 'M':
            if grid[x][y - 2] == 'A':
                if grid[x][y - 3] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_right(grid, coords):
    print('checking right')
    x = coords[0]
    y = coords[1]
    if y <= len(grid[x]) - 4:
        if grid[x][y + 1] == 'M':
            if grid[x][y + 2] == 'A':
                if grid[x][y + 3] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_up(grid, coords):
    print('checking up')
    x = coords[0]
    y = coords[1]
    if x >= 3:
        if grid[x - 1][y] == 'M':
            if grid[x - 2][y] == 'A':
                if grid[x - 3][y] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def check_down(grid, coords):
    print('checking down')
    x = coords[0]
    y = coords[1]
    if x <= len(grid) - 4:
        if grid[x + 1][y] == 'M':
            if grid[x + 2][y] == 'A':
                if grid[x + 3][y] == 'S':
                    print('found XMAS')
                    return 1
    return 0

def find_x(grid):
    x_coords = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if grid[i][j] == 'X':
                x_coords.append((i, j))
    return x_coords

def parse_input(input_file):
    # split the text file into lines and then make each line an array of integers to remove the spaces and group them
    rows = input_file.read().splitlines()
    return [list(row) for row in rows if row]

def main():
    grid = parse_input(open('input.txt'))
    for row in grid:
        print(row)
    x_coords = find_x(grid)
    print(x_coords)
    vert_xmas_count = 0
    for coords in x_coords:
        print(coords)
        vert_xmas_count += check_up(grid, coords)
        vert_xmas_count += check_down(grid, coords)
        vert_xmas_count += check_left(grid, coords)
        vert_xmas_count += check_right(grid, coords)
        vert_xmas_count += check_up_left(grid, coords)
        vert_xmas_count += check_up_right(grid, coords)
        vert_xmas_count += check_down_left(grid, coords)
        vert_xmas_count += check_down_right(grid, coords)
    print(vert_xmas_count)


if __name__ == '__main__':
    main()
