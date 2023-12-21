import sys


def main_func():
    with open(sys.argv[1], "r") as file:
        points = [(0, 0)]
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        nb_boundary_points = 0

        for line in file.readlines():
            dir, nb_steps, _ = line.split()
            nb_steps = int(nb_steps)
            nb_boundary_points += nb_steps
            dir_r, dir_c = dirs[dir]
            r, c = points[-1]
            points.append((r + dir_r * nb_steps, c + dir_c * nb_steps))

        # Shoe lace formula for calculating a polygon area
        area = (
            abs(
                sum(
                    points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1])
                    for i in range(len(points))
                )
            )
            // 2
        )

        # Now we need Pix formula in order to find the number of points inside of our polygon
        # "#####" our points are at the middle of suche a line which means that our area is smaller than the real one
        # Formula: Area = i + b / 2 - 1 where b is the number of boundary points and i the number of inside points
        nb_inside_points = area - (nb_boundary_points) // 2 + 1
        print(nb_inside_points + nb_boundary_points)


if __name__ == "__main__":
    main_func()
