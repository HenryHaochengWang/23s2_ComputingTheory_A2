import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse


class LangtonsAnt:
    def __init__(self, grid_size):
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        # 8 directions
        self.directions = ['up', 'up_right', 'right', 'down_right', 'down', 'down_left', 'left', 'up_left']
        self.direction_idx = 0
        self.x = grid_size // 2
        self.y = grid_size // 2


    def move(self):
        # change color
        color = self.grid[self.y][self.x]
        color = (color + 1) % 7
        self.grid[self.y][self.x] = color

        # change direction
        self.direction_idx = (self.direction_idx + color) % 8

        # move
        if self.directions[self.direction_idx] == 'up':
            self.y -= 1
        elif self.directions[self.direction_idx] == 'up_right':
            self.y -= 1
            self.x += 1
        elif self.directions[self.direction_idx] == 'right':
            self.x += 1
        elif self.directions[self.direction_idx] == 'down_right':
            self.y += 1
            self.x += 1
        elif self.directions[self.direction_idx] == 'down':
            self.y += 1
        elif self.directions[self.direction_idx] == 'down_left':
            self.y += 1
            self.x -= 1
        elif self.directions[self.direction_idx] == 'left':
            self.x -= 1
        elif self.directions[self.direction_idx] == 'up_left':
            self.y -= 1
            self.x -= 1

        # wrap around
        self.x = self.x % len(self.grid)
        self.y = self.y % len(self.grid)


def update(num, ant, ax):
    ant.move()
    ax.clear()
    ax.imshow(ant.grid, cmap='viridis')
    ax.text(1, 1, 'Step: {}'.format(num), color='red', va='top', ha='left')


def main(args):
    grid_size = args.grid_size
    total_steps = args.total_steps
    speed = args.speed

    default_interval = 200
    speed = max(0.01, min(speed, 200))
    interval = int(default_interval / speed)

    ant = LangtonsAnt(grid_size)

    cell_size_in_inches = 0.05
    fig, ax = plt.subplots(figsize=(grid_size * cell_size_in_inches, grid_size * cell_size_in_inches))
    # fig, ax = plt.subplots()

    if args.result_only:
        for _ in range(total_steps):
            ant.move()
        ax.imshow(ant.grid, cmap='viridis')
        plt.show()
    else:
        ani = animation.FuncAnimation(fig, update, frames=total_steps, fargs=[ant, ax], repeat=False, interval=interval)
        plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-g', '--grid_size', type=int, default=101, help='grid size')
    parser.add_argument('-ts', '--total_steps', type=int, default=10000, help='number of steps')
    parser.add_argument('-s', '--speed', type=float, default=1, help='speed of animation')
    parser.add_argument('-r', '--result_only', action='store_true', help='show result only')

    args = parser.parse_args()

    main(args)
