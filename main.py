import pygame
import numpy as np
import random


def randomGrid(N):
    grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)
    return grid


def update(grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            # rule B678/S2345678
            if grid[i, j] == 0:
                if total == 6 or total == 7 or total == 8:
                    newGrid[i, j] = 1
            else:
                if total < 2 or total > 8:
                    newGrid[i, j] = 0

    grid[:] = newGrid[:]
    #grid[:] = sand[:]
    return grid

def draw_grid():
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, cell_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif grid[i, j] == 2:
                pygame.draw.rect(screen, wood_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif grid[i, j] == 3:
                pygame.draw.rect(screen, fire_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif grid[i, j] == 4:
                pygame.draw.rect(screen, sand_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif grid[i, j] == 5:
                pygame.draw.rect(screen, water_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            #elif grid[i, j] == 6:
             #   pygame.draw.rect(screen, dark_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            #elif grid[i, j] == 7:
             #   pygame.draw.rect(screen, light_color, (j * cell_size, i * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, bg, (j * cell_size, i * cell_size, cell_size, cell_size))

            pygame.draw.line(screen, grid_color, (0, i * cell_size), (window_size[0], i * cell_size))
            pygame.draw.line(screen, grid_color, (j * cell_size, 0), (j * cell_size, window_size[1]))


def move_wood(i, j):
    global grid

    if i < field_size[0] - 1 and grid[i + 1, j] == 0:
        # Wood falls straight down if there is space below
        grid[i, j], grid[i + 1, j] = grid[i + 1, j], grid[i, j]
    elif i < field_size[0] - 1 and grid[i + 1, j] == water and grid[i, j + 1] == 0:
        # Wood moves right if there is water below and space to the right
        grid[i, j], grid[i, j + 1] = grid[i, j + 1], grid[i, j]
    elif i < field_size[0] - 1:
        # Check if there is fire in any of the neighboring cells
        fire_neighbors = [(i + 1, j), (i, j + 1), (i, j - 1)]
        for x, y in fire_neighbors:
            if x >= 0 and x < field_size[0] and y >= 0 and y < field_size[1] and grid[x, y] == fire:
                # Wood catches fire if there is fire in any of the neighboring cells
                grid[i, j] = fire
                break


def move_fire(i, j):
    global grid

    if grid[i, j] == fire:
        # Fire turns into dark ash if it has lived long enough
    #    if grid[i,j] == wood:
     #       grid[i, j] = dark
      #      move_ash(i, j)
       #     return

        # Randomly move the fire down, left, or right
        move_options = []
        if i < field_size[0] - 1 and grid[i + 1, j] == 0:
            move_options.append((i + 1, j))
        if j > 0 and grid[i, j - 1] == 0:
            move_options.append((i, j - 1))
        if j < field_size[1] - 1 and grid[i, j + 1] == 0:
            move_options.append((i, j + 1))

        if move_options:
            new_i, new_j = random.choice(move_options)
            grid[new_i, new_j] = fire
            grid_age[new_i, new_j] = grid_age[i, j] + 1

        # Fire can turn adjacent wood into fire
        neighbors = [(i + 1, j), (i, j + 1), (i, j - 1)]
        for x, y in neighbors:
            if x >= 0 and x < field_size[0] and y >= 0 and y < field_size[1] and grid[x, y] == wood:
                grid[x, y] = fire
                grid_age[x, y] = 0

        # Fire turns into light ash if it has just spread
      #  grid_age[i, j] += 1
       # if grid_age[i, j] == 1:
        #    grid[i, j] = light
         #   move_ash(i, j)

def move_fire2(i, j):
    global grid

    if grid[i, j] == fire:
        # Fire turns into dark ash if it has lived long enough
    #    if grid[i,j] == wood:
     #       grid[i, j] = dark
      #      move_ash(i, j)
       #     return

        # Randomly move the fire down, left, or right
        move_options = []
        if i < field_size[0] - 1 and grid[i + 1, j] == 0 and grid[i + 1, j] != water:
            move_options.append((i + 1, j))
        if j > 0 and grid[i, j - 1] == 0 and grid[i, j - 1] != water:
            move_options.append((i, j - 1))
        if j < field_size[1] - 1 and grid[i, j + 1] == 0 and grid[i, j + 1] != water:
            move_options.append((i, j + 1))

        if move_options:
            new_i, new_j = random.choice(move_options)
            grid[new_i, new_j] = fire
            #grid_age[new_i, new_j] = grid_age[i, j] + 1

        # Fire can turn adjacent wood into fire
        #neighbors = [(i + 1, j), (i, j + 1), (i, j - 1)]
        #for x, y in neighbors:
         #   if x >= 0 and x < field_size[0] and y >= 0 and y < field_size[1] and grid[x, y] == wood:
          #      grid[x, y] = fire
           #     grid_age[x, y] = 0

        # Check if there is water in any of the neighboring cells
        water_neighbors = [(i + 1, j), (i, j + 1), (i, j - 1)]
        for x, y in water_neighbors:
            if x >= 0 and x < field_size[0] and y >= 0 and y < field_size[1] and grid[x, y] == water:
                # Wood catches fire if there is fire in any of the neighboring cells
                grid[i, j] = 0
                break

def move_ash(i, j):
    for i in range(field_size[0]):
        for j in range(field_size[1]):
            if grid[i, j] == dark or grid[i, j] == light:
                grid_age[i, j] -= 1
                if grid_age[i, j] <= 0:
                    grid[i, j] = 0
                    grid_age[i, j] = 0

def move_smoke(i, j):
    if i > 0 and grid[i - 1, j] == 0:
        grid[i, j], grid[i - 1, j] = grid[i - 1, j], grid[i, j]
        grid_age[i - 1, j] = grid_age[i, j] + 1  # povečaj starost premaknjenega dima za 1
        return

    directions = [(0, -1), (0, 1), (1, 0)]
    random.shuffle(directions)
    for di, dj in directions:
        if i + di < field_size[0] and j + dj < field_size[1] and grid[i + di, j + dj] == 0:
            grid[i, j], grid[i + di, j + dj] = grid[i + di, j + dj], grid[i, j]
            grid_age[i + di, j + dj] = grid_age[i, j] + 1  # povečaj starost premaknjenega dima za 1
            return

    grid_age[i, j] += 1  

def move_sand(i, j):
    if i < field_size[0] - 1 and grid[i + 1, j] == 0:
        grid[i, j], grid[i + 1, j] = grid[i + 1, j], grid[i, j]
    elif i < field_size[0] - 1 and j > 0 and grid[i + 1, j - 1] == 0 and grid[i, j - 1] == 0:
        grid[i, j], grid[i + 1, j - 1] = grid[i + 1, j - 1], grid[i, j]
    elif i < field_size[0] - 1 and j < field_size[1] - 1 and grid[i + 1, j + 1] == 0 and grid[i, j + 1] == 0:
        grid[i, j], grid[i + 1, j + 1] = grid[i + 1, j + 1], grid[i, j]
    elif i < field_size[0] - 1 and grid[i + 1, j] == water:
        grid[i, j], grid[i + 1, j] = grid[i + 1, j], grid[i, j]

def move_water(i, j):
    global grid
    height, width = grid.shape

    # Move water straight down if there is an empty cell below
    if i < height - 1 and grid[i + 1, j] == 0:
        grid[i, j], grid[i + 1, j] = grid[i + 1, j], grid[i, j]
        return

    # Calculate how much water to move left and right
    max_distance = min(j, width - j - 1)  # maximum distance to move left or right
    move_distance = random.randint(0, max_distance)
    left_distance = move_distance
    right_distance = move_distance

    if random.random() > 0.5:  # randomly choose whether to move left or right first
        left_distance -= 1
    else:
        right_distance -= 1

    # Move water left as far as possible
    while left_distance >= 0 and grid[i, j - 1] == 0:
        grid[i, j], grid[i, j - 1] = grid[i, j - 1], grid[i, j]
        j -= 1
        left_distance -= 1

    # Move water right as far as possible
    while right_distance >= 0 and j < width-1 and grid[i, j + 1] == 0:
        grid[i, j], grid[i, j + 1] = grid[i, j + 1], grid[i, j]
        j += 1
        right_distance -= 1

    # If the current row is completely filled, move to the next row
    #if all(grid[i, col] == 1 for col in range(width)):
     #   move_water5(grid, i+1, j)
      #  return

    # Check if the current row is completely filled before moving to the next row
    if all(grid[i, col] == 1 for col in range(width)):
        move_water(grid, i + 1, j)
        return

def move_water2(i, j):
    global grid
    height, width = grid.shape

    # Move water straight down if there is an empty cell below
    if i < height - 1 and grid[i + 1, j] == 0:
        grid[i, j], grid[i + 1, j] = grid[i + 1, j], grid[i, j]
        return

    # Calculate how much water to move left and right
    max_distance = min(j, width - j - 1)  # maximum distance to move left or right
    move_distance = random.randint(0, max_distance)
    left_distance = move_distance
    right_distance = move_distance

    # Randomly choose whether to move left or right first
    if random.random() > 0.5:
        left_distance -= 1
    else:
        right_distance -= 1

    # Move water left as far as possible
    while left_distance >= 0 and j > 0 and grid[i, j - 1] == 0:
        grid[i, j], grid[i, j - 1] = grid[i, j - 1], grid[i, j]
        j -= 1
        left_distance -= 1

    # Move water right as far as possible
    while right_distance >= 0 and j < width - 1 and grid[i, j + 1] == 0:
        grid[i, j], grid[i, j + 1] = grid[i, j + 1], grid[i, j]
        j += 1
        right_distance -= 1

    # If there are still moves left to make, move in the opposite direction
    while left_distance >= 0 and j > 0 and grid[i, j - 1] == 0:
        grid[i, j], grid[i, j - 1] = grid[i, j - 1], grid[i, j]
        j -= 1
        left_distance -= 1

    while right_distance >= 0 and j < width - 1 and grid[i, j + 1] == 0:
        grid[i, j], grid[i, j + 1] = grid[i, j + 1], grid[i, j]
        j += 1
        right_distance -= 1

cell_size = 10
field_size = (50, 50)
window_size = (cell_size * field_size[0], cell_size * field_size[1])

#grid = np.zeros(field_size, dtype=int)
grid_age = np.zeros(field_size, dtype=int)
wood = 2
fire = 3
sand = 4
water = 5
light = 6
dark = 7
selected = False

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Elements Simulation")

grid_color = (61,61,61)
bg = (255, 255, 255)
cell_color = (0, 0, 0)
wood_color = (94,38,18)
fire_color = (226, 0, 0)
sand_color = (227, 168, 105)
water_color = (135,206,250)
dark_color = (87, 224, 67)
light_color = (226, 224, 0)

grid = randomGrid(50)

def main():
    global selected, grid
    clock = pygame.time.Clock()
    update_timer = 0
    update_speed = 70  

    grid = update(grid, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected = True
                mouse_pos = pygame.mouse.get_pos()
                i = mouse_pos[1] // cell_size
                j = mouse_pos[0] // cell_size
                grid[i, j] = wood

            elif event.type == pygame.MOUSEBUTTONUP:
                selected = False

            elif event.type == pygame.MOUSEMOTION and selected:
                mouse_pos = pygame.mouse.get_pos()
                i = mouse_pos[1] // cell_size
                j = mouse_pos[0] // cell_size
                grid[i, j] = fire

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mouse_pos = pygame.mouse.get_pos()
                    i = mouse_pos[1] // cell_size
                    j = mouse_pos[0] // cell_size
                    grid[i, j] = sand

                elif event.key == pygame.K_DOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    i = mouse_pos[1] // cell_size
                    j = mouse_pos[0] // cell_size
                    grid[i, j] = water

        update_timer += clock.tick()
        while update_timer > update_speed:
            update_timer -= update_speed

            for i in range(field_size[0] - 1, -1, -1):
                for j in range(field_size[1]):
                    if grid[i, j] == fire:
                        move_fire2(i, j)
                    elif grid[i, j] == wood:
                        move_wood(i, j)
                    elif grid[i, j] == sand:
                        move_sand(i, j)
                    elif grid[i, j] == water:
                        move_water2(i, j)


        draw_grid()

        pygame.display.update()


if __name__ == '__main__':
    main()