import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class LangtonsAnt:
    grid = None
    def __init__(self, grid_size, x, y, direction_idx=0):
        if LangtonsAnt.grid is None:
            LangtonsAnt.grid = np.zeros((grid_size, grid_size), dtype=int)
        # self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.directions = ['up', 'right', 'down', 'left']
        self.direction_idx = direction_idx
        # self.x = grid_size // 2
        # self.y = grid_size // 2
        self.x = x
        self.y = y

    def move(self):
        if LangtonsAnt.grid[self.y][self.x] == 0:
            self.direction_idx = (self.direction_idx + 1) % 4
            LangtonsAnt.grid[self.y][self.x] = 1
        else:
            self.direction_idx = (self.direction_idx - 1) % 4
            LangtonsAnt.grid[self.y][self.x] = 0

        if self.directions[self.direction_idx] == 'up':
            self.y -= 1
        elif self.directions[self.direction_idx] == 'right':
            self.x += 1
        elif self.directions[self.direction_idx] == 'down':
            self.y += 1
        elif self.directions[self.direction_idx] == 'left':
            self.x -= 1

        self.x = self.x % len(LangtonsAnt.grid)
        self.y = self.y % len(LangtonsAnt.grid)

        # if self.x < 0 or self.x >= len(self.grid) or self.y < 0 or self.y >= len(self.grid):
        #     exit(0)

        # if self.x < 0:
        #     self.x = 0
        #     self.direction_idx = (self.direction_idx - 1) % 4
        # elif self.x >= len(self.grid):
        #     self.x = len(self.grid) - 1
        #     self.direction_idx = (self.direction_idx - 1) % 4
        # elif self.y < 0:
        #     self.y = 0
        #     self.direction_idx = (self.direction_idx - 1) % 4
        # elif self.y >= len(self.grid):
        #     self.y = len(self.grid) - 1
        #     self.direction_idx = (self.direction_idx - 1) % 4

        # if self.x < 0:
        #     self.x = 0
        #     self.direction_idx = (self.direction_idx + 1) % 4
        # elif self.x >= len(self.grid):
        #     self.x = len(self.grid) - 1
        #     self.direction_idx = (self.direction_idx + 1) % 4
        # elif self.y < 0:
        #     self.y = 0
        #     self.direction_idx = (self.direction_idx + 1) % 4
        # elif self.y >= len(self.grid):
        #     self.y = len(self.grid) - 1
        #     self.direction_idx = (self.direction_idx + 1) % 4

        # if self.x < 0:
        #     self.x = 0
        #     self.direction_idx = (self.direction_idx + 2) % 4
        # elif self.x >= len(self.grid):
        #     self.x = len(self.grid) - 1
        #     self.direction_idx = (self.direction_idx + 2) % 4
        # elif self.y < 0:
        #     self.y = 0
        #     self.direction_idx = (self.direction_idx + 2) % 4
        # elif self.y >= len(self.grid):
        #     self.y = len(self.grid) - 1
        #     self.direction_idx = (self.direction_idx + 2) % 4


def update(num, ants, ax, steps_per_update=50000):
    for _ in range(steps_per_update):
        for ant in ants:
            ant.move()
    ax.clear()
    ax.imshow(LangtonsAnt.grid, cmap='binary')
    ax.text(1, 1, 'Frame: {}'.format(num*steps_per_update), color='red', va='top', ha='left')

def main():
    grid_size = 1001

    ant1 = LangtonsAnt(grid_size, grid_size//4, grid_size//4, direction_idx=2)
    ant2 = LangtonsAnt(grid_size, grid_size-grid_size//4, grid_size//4, direction_idx=3)
    ant3 = LangtonsAnt(grid_size, grid_size//4, grid_size-grid_size//4, direction_idx=0)
    ant4 = LangtonsAnt(grid_size, grid_size-grid_size//4, grid_size-grid_size//4, direction_idx=1)
    # ants = [ant1]
    ants = [ant1, ant2, ant3, ant4]

    fig, ax = plt.subplots()


    ani = animation.FuncAnimation(fig, update, frames=100000, fargs=[ants, ax], repeat=False, interval=1)
    plt.show()

if __name__ == "__main__":
    main()

