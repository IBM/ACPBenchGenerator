#!/usr/bin/env python
import sys
import random


def get_tile(row, col, num_columns):
    return "tile_" + str( row * num_columns + col)
    # return "tile_" + str(row) + "-" + str(col)


# There is an extra row below to place robots at the end


def get_objects(num_rows, num_columns, num_robots):
    #   TILES
    str_tiles = ""
    for row in range(num_rows + 1):
        for column in range(num_columns):
            str_tiles = str_tiles + get_tile(row, column + 1, num_columns) + " "
        if row != num_rows:
            str_tiles += "\n           "
    str_tiles += "- tile\n"

    # ROBOTS
    str_robots = "           "
    for robot in range(num_robots):
        str_robots += "robot" + str(robot + 1) + " "
    str_robots += "- robot\n"

    # COLORS
    str_colors = "           white black - color\n"
    return str_tiles + str_robots + str_colors


def get_init(num_rows, num_columns, num_robots):
    robot_locations = []
    str_init = "\n"

    used_cols = list(range(1, num_columns + 1))

    for robot in range(num_robots):
        posx = random.randint(0, num_rows)
        posy = random.choice(used_cols)
        robot_pos = get_tile(posx, posy, num_columns)
        robot_locations += [robot_pos]
        used_cols.remove(posy)

        str_init += "   (robot-at robot" + str(robot + 1) + " " + robot_pos + ")\n"
        if robot % 2 == 0:
            robot_color = "white"
        else:
            robot_color = "black"
        str_init += "   (robot-has robot" + str(robot + 1) + " " + robot_color + ")\n"

    str_init += "   (available-color white)\n"
    str_init += "   (available-color black)\n"

    for row in range(num_rows + 1):
        for column in range(num_columns):
            if get_tile(row, column + 1, num_columns) not in robot_locations:
                str_init += "   (clear " + get_tile(row, column + 1, num_columns) + ")\n"

    for row in range(num_rows):
        for column in range(num_columns):
            str_init += (
                "   (up "
                + get_tile(row + 1, column + 1, num_columns)
                + " "
                + get_tile(row, column + 1, num_columns)
                + ")\n"
            )
    for row in range(num_rows):
        for column in range(num_columns):
            str_init += (
                "   (down "
                + get_tile(row, column + 1, num_columns)
                + " "
                + get_tile(row + 1, column + 1, num_columns)
                + ")\n"
            )
    for row in range(num_rows + 1):
        for column in range(num_columns - 1):
            str_init += (
                "   (right "
                + get_tile(row, column + 2, num_columns)
                + " "
                + get_tile(row, column + 1, num_columns)
                + ")\n"
            )
    for row in range(num_rows + 1):
        for column in range(num_columns - 1):
            str_init += (
                "   (left "
                + get_tile(row, column + 1, num_columns)
                + " "
                + get_tile(row, column + 2, num_columns)
                + ")\n"
            )

    return str_init


def get_goals(num_rows, num_columns, num_robots):
    str_goals = "(and\n"
    for row in range(num_rows):
        for column in range(num_columns):
            if (row + column) % 2 == 0:
                str_goals += (
                    "    (painted " + get_tile(row + 1, column + 1, num_columns) + " white)\n"
                )
            else:
                str_goals += (
                    "    (painted " + get_tile(row + 1, column + 1, num_columns) + " black)\n"
                )
    return str_goals + ")"

def main(name, num_rows, num_columns, num_robots, seed = None):
    if seed:
        random.seed(seed)

    ret = str("(define (problem " + name + ")") + \
    str(" (:domain floor-tile)") + \
    str(" (:objects " + get_objects(num_rows, num_columns, num_robots) + ")") + \
    str(" (:init " + get_init(num_rows, num_columns, num_robots) + ")") + \
    str(" (:goal " + get_goals(num_rows, num_columns, num_robots) + ")") + \
    str(")")
    return ret


if __name__ == "__main__":
    # Reading the command line arguments
    try:
        name = sys.argv[1]
        num_rows = int(sys.argv[2])
        num_columns = int(sys.argv[3])
        num_robots = int(sys.argv[4])

        if len(sys.argv) == 6:
            seed = int(sys.argv[5])
        else:
            seed = None


    except BaseException:
        print(
            "Usage: "
            + sys.argv[0]
            + " <name> <num_rows> <num_columns> <num_robots> [<seed>]"
        )
        sys.exit(1)

    print(main(name, num_rows, num_columns, num_robots, seed))
