with open(file='data.txt') as file:
    octopi = [list(map(int, list(line))) for line in file.read().split("\n")]


COL_LENGTH = len(octopi[0])
ROW_LENGTH = len(octopi)


def get_adjacent_numbers(r, c):
    adjacent_indices = []

    if c - 1 >= 0:
        adjacent_indices.append((r, c-1))
    if c + 1 < COL_LENGTH:
        adjacent_indices.append((r, c + 1))
    if r - 1 >= 0:
        adjacent_indices.append((r-1, c))
    if r + 1 < ROW_LENGTH:
        adjacent_indices.append((r+1, c))

    if r - 1 >= 0 and c - 1 >= 0:
        adjacent_indices.append((r-1, c-1))
    if r + 1 < ROW_LENGTH and c + 1 < COL_LENGTH:
        adjacent_indices.append((r+1, c+1))
    if r - 1 >= 0 and c + 1 < COL_LENGTH:
        adjacent_indices.append((r-1, c+1))
    if r + 1 < ROW_LENGTH and c - 1 >= 0:
        adjacent_indices.append((r+1, c-1))

    return adjacent_indices


def display_grid():
    for line in octopi:
        print(line)
    print("\n")


flashes = 0
all_flashing = False
all_flashing_step = 0
curr_step = 1

for step in range(500):
    if all_flashing:
        all_flashing_step = step
        break
    indices_checked = set()
    curr_step_flashes = 0
    display_grid()

    for r, row in enumerate(octopi):
        for c, col in enumerate(row):
            if (r, c) not in indices_checked:
                octopi[r][c] += 1

                if octopi[r][c] > 9:
                    indices_checked.add((r, c))
                    flashing = get_adjacent_numbers(r, c)

                    while flashing:
                        curr_pos = flashing.pop()
                        new_r, new_c = curr_pos[0], curr_pos[1]
                        if (new_r, new_c) not in indices_checked:
                            octopi[new_r][new_c] += 1

                            if octopi[new_r][new_c] > 9:
                                indices_checked.add((new_r, new_c))
                                new_indices = get_adjacent_numbers(new_r, new_c)

                                for pos in new_indices:
                                    flashing.append(pos)

    while indices_checked:
        curr_pos = indices_checked.pop()
        r, c = curr_pos[0], curr_pos[1]
        octopi[r][c] = 0
        curr_step_flashes += 1
        if step < 100:
            flashes += 1

    if curr_step_flashes == COL_LENGTH * ROW_LENGTH:
        all_flashing = True

# part one:
print(flashes)
# part two:
print(all_flashing_step)
